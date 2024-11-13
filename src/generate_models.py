import json
import os
from config import logger


TYPE_MAPPING = {
    "STRING": "str",
    "INTEGER": "int",
    "FLOAT": "float",
    "BOOLEAN": "bool",
    "DATE": "date",
    "TIMESTAMP": "datetime",
    "RECORD": "dict",
    "RECORD": "dict",
    "NUMERIC": "float",
    "ANY": "Any",
    "JSON": "dict"
}


def create_output_directory(output_dir):
    """
    Cria o diretório de saída e garante a presença do arquivo __init__.py.

    Args:
        output_dir (str): Caminho do diretório de saída.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    init_file = os.path.join(output_dir, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, 'w') as init_f:
            init_f.write(f"# Auto-generated init file for {output_dir}")


def generate_bigquery_class(table_name, schema):
    """
    Gera a definição de schema BigQuery para uma tabela.

    Args:
        table_name (str): Nome da tabela.
        schema (list): Esquema da tabela em formato de lista de dicionários.

    Returns:
        str: Definição da classe em formato de string.
    """
    def process_field(field):
        field_type = field['type']
        if field_type == 'RECORD' and 'fields' in field:
            subfields = ", ".join(
                [process_field(subfield) for subfield in field['fields']]
            )
            return f"bigquery.SchemaField('{field['name']}', 'RECORD', '{field.get('mode', 'NULLABLE')}', fields=[{subfields}])"
        elif field_type == 'JSON':
            return f"bigquery.SchemaField('{field['name']}', 'JSON', '{field.get('mode', 'NULLABLE')}')"
        else:
            return f"bigquery.SchemaField('{field['name']}', '{field_type}', '{field.get('mode', 'NULLABLE')}')"

    class_definition = f"{table_name} = [\n"
    for field in schema:
        class_definition += f"    {process_field(field)},\n"
    class_definition += "]\n"
    return class_definition


def process_bigquery_folder(folder_path, folder_name, output_dir):
    """
    Processa uma pasta contendo arquivos JSON e gera um arquivo de schema BigQuery.

    Args:
        folder_path (str): Caminho da pasta de entrada.
        folder_name (str): Nome da pasta de entrada.
        output_dir (str): Diretório de saída.
    """
    schemas = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                table = data.get("table")
                schema = data.get("schema")
                schema_name = os.path.splitext(filename)[0]
                formatted_class = generate_bigquery_class(schema_name, schema)
                schemas.append(f"# Dataset: {folder_name}, Table: {table}\n{formatted_class}")

    output_file_name = f"{folder_name}.py"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("from google.cloud import bigquery\n\n")
        output_file.write("\n\n".join(schemas))


def create_bigquery_schemas(directory):
    """
    Cria schemas BigQuery para todos os datasets no diretório especificado.

    Args:
        directory (str): Caminho do diretório de entrada.
    """
    output_dir = "py_schemas"
    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_bigquery_folder(folder_path, folder_name, output_dir)

    logger.info("BigQuery Schemas criados com sucesso!")


def create_class_code_pydantic(schema: dict) -> str:
    """
    Gera código de classe Pydantic a partir de um schema.

    Args:
        schema (dict): Dicionário contendo nome da tabela e schema.

    Returns:
        str: Código da classe Pydantic como string.
    """
    def process_field(field):
        if field['type'] == 'RECORD' and 'fields' in field:
            class_name = field['name'].capitalize()
            nested_class = f"class {class_name}(BaseModel):\n"
            for subfield in field['fields']:
                subfield_type = TYPE_MAPPING.get(subfield['type'], "Any")
                nested_class += f"    {subfield['name']}: {subfield_type}\n"

            return nested_class, f"{field['name']}: '{class_name}'"
        else:
            field_type = TYPE_MAPPING.get(field['type'], "Any")
            return "", f"{field['name']}: {field_type}"

    class_name = schema['table'].capitalize()
    class_code = f"class {class_name}(BaseModel):\n"
    nested_classes = []

    for field in schema['schema']:
        nested_class, field_declaration = process_field(field)
        if nested_class:
            nested_classes.append(nested_class)
        class_code += f"    {field_declaration}\n"

    if nested_classes:
        class_code += "\n\n" + "\n\n".join(nested_classes)

    class_code += "\n\n"
    return class_code


def process_pydantic_folder(folder_path, folder_name, output_dir):
    """
    Processa uma pasta com arquivos JSON e gera um arquivo de models Pydantic.

    Args:
        folder_path (str): Caminho da pasta de entrada.
        folder_name (str): Nome da pasta de entrada.
        output_dir (str): Diretório de saída.
    """
    models = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                table = data.get("table")
                schema = data.get("schema")
                class_code = create_class_code_pydantic({'table': table, 'schema': schema})
                models.append(f"# Dataset: {folder_name}, Table: {table}\n{class_code}")

    output_file_name = f"{folder_name}_models.py"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("from pydantic import BaseModel\n")
        output_file.write("from datetime import date, datetime\n")
        output_file.write("\n\n")
        output_file.write("\n\n".join(models))


def create_pydantic_models(directory):
    """
    Cria classes Pydantic para todos os datasets no diretório especificado.

    Args:
        directory (str): Caminho do diretório de entrada.
    """
    output_dir = "py_models"
    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_pydantic_folder(folder_path, folder_name, output_dir)

    logger.info("Pydantic Models criados com sucesso!")



import json
import logging
import os
from config import setup_logging

setup_logging(log_level=logging.INFO)

TYPE_MAPPING = {
    "STRING": "str",
    "INTEGER": "int",
    "FLOAT": "float",
    "BOOLEAN": "bool",
    "DATE": "date",
    "TIMESTAMP": "datetime",
    "RECORD": "dict",
    "NUMERIC": "float",
    "ANY": "Any",
    "JSON": "dict"  # Mapeamento para Pydantic
}

def create_output_directory(output_dir):
    """
    Cria um diretório para a saída e garante que o arquivo __init__.py esteja presente.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Criar arquivo __init__.py no diretório
    init_file = os.path.join(output_dir, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, 'w') as init_f:
            init_f.write(f"# Auto-generated init file for {output_dir}")

def generate_bigquery_class(table_name, schema):
    def process_field(field):
        field_type = field['type']
        if field_type == 'RECORD' and 'fields' in field:
            # Processa subcampos recursivamente para campos aninhados do tipo RECORD
            subfields = ", ".join(
                [process_field(subfield) for subfield in field['fields']]
            )
            return f"bigquery.SchemaField('{field['name']}', 'RECORD', '{field.get('mode', 'NULLABLE')}', fields=[{subfields}])"
        elif field_type == 'JSON':
            return f"bigquery.SchemaField('{field['name']}', 'JSON', '{field.get('mode', 'NULLABLE')}')"
        else:
            return f"bigquery.SchemaField('{field['name']}', '{field_type}', '{field.get('mode', 'NULLABLE')}')"

    # Monta a definição da classe como uma lista de campos BigQuery
    class_definition = f"{table_name} = [\n"
    for field in schema:
        class_definition += f"    {process_field(field)},\n"
    class_definition += "]\n"
    return class_definition

def process_bigquery_folder(folder_path, folder_name, output_dir):
    """
    Processa uma pasta contendo arquivos JSON e gera um arquivo de schema para o BigQuery.
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
    Cria schemas do BigQuery para todos os datasets em um diretório especificado.
    """
    output_dir = "py_schemas"
    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_bigquery_folder(folder_path, folder_name, output_dir)

    logging.info("BigQuery Schemas criados com sucesso!")

def create_class_code_pydantic(schema: dict) -> str:
    def process_field(field):
        if field['type'] == 'RECORD' and 'fields' in field:
            # Gera classe aninhada para o campo RECORD
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
    Processa uma pasta contendo arquivos JSON e gera um arquivo de models Pydantic.
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
    Cria classes Pydantic para todos os datasets em um diretório especificado.
    """
    output_dir = "py_models"
    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_pydantic_folder(folder_path, folder_name, output_dir)
    
    logging.info("Pydantic Models criados com sucesso!")

# Exemplo de uso
directory = './bq_schemas'
create_bigquery_schemas(directory)
create_pydantic_models(directory)

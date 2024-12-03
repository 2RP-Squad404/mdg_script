import json
import os
from google.cloud.bigquery import SchemaField
from config import ROOT_DIR, logger
import google.cloud.bigquery as bigquery

ROOT_DIR = os.getcwd()

TYPE_MAPPING = {
    'STRING': 'str',
    'INTEGER': 'int',
    'FLOAT': 'float',
    'BOOLEAN': 'bool',
    'DATE': 'date',
    'TIMESTAMP': 'datetime',
    'RECORD': 'dict',
    'RECORD': 'dict',
    'NUMERIC': 'float',
    'ANY': 'Any',
    'JSON': 'dict',
}

def create_output_directory(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def generate_bigquery_class(table_name, schema, existing_schema=None):
    """
    Gera a definição de schema BigQuery para uma tabela.

    Parâmetros:
        table_name (str): Nome da tabela.
        schema (list): Esquema da tabela em formato de lista de dicionários.
        existing_schema (list): Schema existente já definido no arquivo, se houver.

    Retorno:
        str: Definição da classe em formato de string.
    """
    def process_field(field, indent=4):
        """
        Processa um campo do schema para gerar código BigQuery SchemaField.
        """
        if isinstance(field, dict):
            field_name = field.get('name')
            field_type = field.get('type', 'STRING')
            field_mode = field.get('mode', 'NULLABLE')
            field_description = field.get('description', '')
            subfields = field.get('fields', [])
        elif isinstance(field, SchemaField):
            field_name = field.name
            field_type = field.field_type
            field_mode = field.mode
            field_description = field.description or ''
            subfields = getattr(field, 'fields', [])
        else:
            raise TypeError(f"Tipo de campo inesperado: {type(field)}")

        description_str = f", description='{field_description}'" if field_description else ""
        current_indent = ' ' * indent

        if field_type == 'RECORD' and subfields:
            subfields_code = ",\n".join(
                [process_field(subfield, indent=indent + 4) for subfield in subfields]
            )
            return (
                f"{current_indent}bigquery.SchemaField("
                f"'{field_name}', 'RECORD', '{field_mode}'{description_str},\n"
                f"{current_indent}fields=[\n{subfields_code}\n{current_indent}    ]\n"
                f"{current_indent})"
            )
        else:
            return (
                f"{current_indent}bigquery.SchemaField("
                f"'{field_name}', '{field_type}', '{field_mode}'{description_str})"
            )

    existing_field_names = (
        {field.name: field.description for field in existing_schema}
        if existing_schema
        else {}
    )

    unique_fields = set()

    class_definition = "from google.cloud import bigquery\n\n"
    class_definition += f"{table_name} = [\n"

    for field in schema:
        if isinstance(field, dict):
            field['description'] = field.get('description') or existing_field_names.get(field.get('name', ''), '')

        field_name = field.get('name') if isinstance(field, dict) else field.name
        if field_name not in unique_fields:
            unique_fields.add(field_name)
            class_definition += f"{process_field(field)},\n"

    class_definition += "]\n"
    return class_definition

def validate_json_file(file_path):
    """
    Valida se um arquivo contém JSON válido e tem a estrutura esperada.

    Parâmetros:
        file_path (str): Caminho do arquivo.

    Retorno:
        bool: True se válido e contém a chave 'table', False caso contrário.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if 'table' not in data:
            logger.error(f"Chave 'table' ausente no arquivo: {file_path}")
            return False
        return True
    except json.JSONDecodeError as e:
        logger.error(f"Erro no JSON {file_path}: {e}")
        return False


def process_bigquery_folder(folder_path, folder_name, output_dir):
    """
    Processa uma pasta contendo arquivos JSON e gera um arquivo de schema BigQuery.

    Parâmetros:
        folder_path (str): Caminho da pasta de entrada.
        folder_name (str): Nome da pasta de entrada.
        output_dir (str): Diretório de saída.
    """
    schemas = []
    existing_schemas = {}

    output_file_name = f"{folder_name}.py"
    output_file_path = os.path.join(output_dir, output_file_name)

    if os.path.exists(output_file_path):
        with open(output_file_path, 'r', encoding='utf-8') as output_file:
            content = output_file.read()
            temp_namespace = {}
            exec(content, {'bigquery': bigquery}, temp_namespace)
            for key, value in temp_namespace.items():
                if isinstance(value, list):
                    existing_schemas[key] = value

    for json_file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, json_file)
        if validate_json_file(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
                schemas.append(schema)

    for schema in schemas:
        table_name = schema.get('table')
        if not table_name:
            logger.error(f"JSON inválido. A chave 'table' está ausente no arquivo: {schema}")
            continue

        if table_name in existing_schemas:
            existing_fields = {field.name for field in existing_schemas[table_name]}
            schema['schema'] = [field for field in schema['schema'] if field['name'] not in existing_fields]
            existing_schemas[table_name].extend(schema['schema'])
        else:
            existing_schemas[table_name] = schema['schema']

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for table_name, schema in existing_schemas.items():
            output_file.write(generate_bigquery_class(table_name, schema))


def create_bigquery_schemas(directory):
    """
    Cria schemas BigQuery para todos os datasets no diretório especificado.

    Parâmetros:
        directory (str): Caminho do diretório de entrada.
    """
    output_dir = os.path.join(ROOT_DIR, 'src', 'py_schemas')

    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_bigquery_folder(folder_path, folder_name, output_dir)

    logger.info('BigQuery Schemas criados com sucesso!')


def create_class_code_pydantic(schema: dict) -> str:
    """
    Gera código de classe Pydantic a partir de um schema BigQuery.

    Parâmetros:
        schema (dict): Dicionário contendo nome da tabela e schema.

    Retorno:
        str: Código da classe Pydantic como string.
    """
    def process_field(field):
        if field['type'] == 'RECORD' and 'fields' in field:
            class_name = field['name'].capitalize()
            nested_class = f'class {class_name}(BaseModel):\n'
            for subfield in field['fields']:
                subfield_type = TYPE_MAPPING.get(subfield['type'], 'Any')
                is_list = subfield.get('mode') == 'REPEATED'
                subfield_declaration = (
                    f"    {subfield['name']}: List[{subfield_type}]"
                    if is_list else
                    f"    {subfield['name']}: {subfield_type}"
                )
                nested_class += subfield_declaration + "\n"

            return nested_class, f"{field['name']}: Optional[{class_name}]"
        else:
            field_type = TYPE_MAPPING.get(field['type'], 'Any')
            is_list = field.get('mode') == 'REPEATED'
            return '', (
                f"{field['name']}: List[{field_type}]"
                if is_list else
                f"{field['name']}: {field_type}"
            )

    class_name = schema['table'].capitalize()
    class_code = f'class {class_name}(BaseModel):\n'
    nested_classes = []

    for field in schema['schema']:
        nested_class, field_declaration = process_field(field)
        if nested_class:
            nested_classes.append(nested_class)
        class_code += f"    {field_declaration}\n"

    if nested_classes:
        class_code += '\n\n' + '\n\n'.join(nested_classes)

    class_code += '\n\n'
    return class_code


def process_pydantic_folder(folder_path, folder_name, output_dir):
    """
    Processa uma pasta com arquivos JSON e gera um arquivo de models Pydantic.

    Parâmetros:
        folder_path (str): Caminho da pasta de entrada.
        folder_name (str): Nome da pasta de entrada.
        output_dir (str): Diretório de saída.
    """
    models = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            filepath = os.path.join(folder_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    table = data.get('table')
                    schema = data.get('schema')
                    if table and schema:
                        class_code = create_class_code_pydantic({
                            'table': table,
                            'schema': schema,
                        })
                        models.append(
                            f'# Dataset: {folder_name}, Table: {table}\n{class_code}'
                        )
            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")

    output_file_name = f'{folder_name}_models.py'
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('from pydantic import BaseModel\n')
        output_file.write('from datetime import date, datetime\n')
        output_file.write('\n\n')
        output_file.write('\n\n'.join(models))


def create_pydantic_models(directory) -> None:
    """
    Cria classes Pydantic para todos os datasets no diretório especificado.

    Parâmetros:
        directory (str): Caminho do diretório de entrada.
    """
    output_dir = os.path.join(ROOT_DIR, 'src', 'py_models')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_pydantic_folder(folder_path, folder_name, output_dir)

    print("Pydantic Models criados com sucesso!")
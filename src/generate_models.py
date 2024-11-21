import json
import os

from config import ROOT_DIR, logger

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
    """
    Cria o diretório de saída e garante a presença do arquivo __init__.py.

    Parâmetros:
        output_dir (str): Caminho do diretório de saída.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    init_file = os.path.join(output_dir, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w') as init_f:
            init_f.write(f'# Auto-generated init file for {output_dir}')

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
        Processa um campo do schema, incluindo subcampos no caso de RECORD.
        """
        field_type = field['type']
        description = field.get('description', '')
        description_str = f", description='{description}'" if description else ""
        current_indent = ' ' * indent

        if field_type == 'RECORD' and 'fields' in field:
            # Processa subcampos de RECORD
            subfields = ",\n".join(
                [process_field(subfield, indent=indent + 4) for subfield in field['fields']]
            )
            return (
                f"{current_indent}bigquery.SchemaField(\n"
                f"{current_indent}    '{field['name']}', 'RECORD', '{field.get('mode', 'NULLABLE')}'{description_str},\n"
                f"{current_indent}    fields=[\n{subfields}\n{current_indent}    ]\n"
                f"{current_indent})"
            )
        else:
            # Processa campos normais
            return (
                f"{current_indent}bigquery.SchemaField("
                f"'{field['name']}', '{field_type}', '{field.get('mode', 'NULLABLE')}'{description_str})"
            )

    # Mapeia campos existentes (se houver) para reutilizar descrições
    existing_field_names = (
        {field.name: field.description for field in existing_schema}
        if existing_schema
        else {}
    )

    # Constrói a definição da classe
    class_definition = f"{table_name} = [\n"
    for field in schema:
        field_description = field.get(
            'description', existing_field_names.get(field['name'], '')
        )
        field['description'] = field_description  # Atualiza a descrição, se disponível
        class_definition += f"{process_field(field)},\n"
    class_definition += "]\n"
    return class_definition

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

    # Carrega schemas existentes, se o arquivo de saída já existe
    if os.path.exists(output_file_path):
        with open(output_file_path, 'r', encoding='utf-8') as output_file:
            content = output_file.read()
            temp_namespace = {}
            exec(content, {}, temp_namespace)
            for key, value in temp_namespace.items():
                if isinstance(value, list):  # Apenas schemas válidos
                    existing_schemas[key] = value

def format_schema(schema_fields, indent=4):
    """
    Formata os campos do schema para preservar subcampos de RECORD e garantir boa formatação.

    Parâmetros:
        schema_fields (list): Lista de campos do schema.
        indent (int): Nível de indentação.

    Retorno:
        str: Campos formatados como string.
    """
    def format_field(field, current_indent):
        if field.field_type == 'RECORD':
            subfields = format_schema(field.fields, indent=current_indent + 4)
            return (
                f"{' ' * current_indent}bigquery.SchemaField(\n"
                f"{' ' * (current_indent + 4)}'{field.name}', 'RECORD', '{field.mode}',\n"
                f"{' ' * (current_indent + 4)}description='{field.description}',\n"
                f"{' ' * (current_indent + 4)}fields=[\n{subfields}\n{' ' * (current_indent + 4)}]\n"
                f"{' ' * current_indent})"
            )
        return (
            f"{' ' * current_indent}bigquery.SchemaField("
            f"'{field.name}', '{field.field_type}', '{field.mode}', "
            f"description='{field.description}')"
        )

    return ",\n".join([format_field(f, indent) for f in schema_fields])

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
    Gera código de classe Pydantic a partir de um schema.

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
                nested_class += f"    {subfield['name']}: {subfield_type}\n"

            return nested_class, f"{field['name']}: '{class_name}'"
        else:
            field_type = TYPE_MAPPING.get(field['type'], 'Any')
            return '', f"{field['name']}: {field_type}"

    class_name = schema['table'].capitalize()
    class_code = f'class {class_name}(BaseModel):\n'
    nested_classes = []

    for field in schema['schema']:
        nested_class, field_declaration = process_field(field)
        if nested_class:
            nested_classes.append(nested_class)
        class_code += f'    {field_declaration}\n'

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
            with open(filepath, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                table = data.get('table')
                schema = data.get('schema')
                class_code = create_class_code_pydantic({
                    'table': table,
                    'schema': schema,
                })
                models.append(
                    f'# Dataset: {folder_name}, Table: {table}\n{class_code}'
                )

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

    output_dir = os.path.join(ROOT_DIR, 'src', 'py_models') # constroe o caminho para o arquivo passado como argumento tendo como base o diretório raiz

    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_pydantic_folder(folder_path, folder_name, output_dir)

    logger.info("Pydantic Models criados com sucesso!")

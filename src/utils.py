# Este arquivo possui a implementação de funções auxiliares da aplicação
import json
import logging
import os
from pathlib import Path
import sys
import time
from datetime import datetime

import pyfiglet
from google.api_core.exceptions import NotFound
from google.cloud import bigquery

from config import PROJECT_ID

TYPE_MAPPING = {
    "STRING": "str",
    "INTEGER": "int",
    "FLOAT": "float",
    "BOOLEAN": "bool",
    "DATE": "date",
    "TIMESTAMP": "datetime",
    "RECORD": "dict",  
    "ANY": "Any",
}


client = bigquery.Client(PROJECT_ID)


def create_table(client, table_id, schema):
    """
    Cria uma tabela no BigQuery com base em um schema recebido.

    Esta função tenta criar uma tabela no BigQuery. Se a tabela já existir, 
    uma mensagem é exibida indicando que a tabela já está disponível. Caso 
    contrário, a tabela será criada com base no schema fornecido.

    Parâmetros:
        client (bigquery.Client): O cliente do BigQuery usado para realizar operações.
        table_id (str): O ID completo da tabela no formato 'project_id.dataset_id.table_id'.
        schema (list[bigquery.SchemaField]): Uma lista de objetos SchemaField que define 
            o esquema da tabela.

    Exceções:
        NotFound: Lançada se a tabela não for encontrada, o que aciona a criação de uma nova tabela.
        google.api_core.exceptions.GoogleAPIError: Captura erros da API do Google BigQuery.
    
    Retorno:
        bigquery.Table: A tabela criada ou uma mensagem informando que ela já existe e o tempo local.
    """
    try:
        table = client.get_table(table_id)
        logging.info(f"Tabela {table.table_id} já existe.")
        print(f"Tabela {table.table_id} já existe.")
    except NotFound:
        try:
            table = bigquery.Table(table_id, schema=schema)
            table = client.create_table(table)
            logging.info(f"Tabela {table.table_id} criada em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Tabela {table.table_id} criada em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            return table
        except Exception as e:
            logging.error(f"Erro ao criar a tabela {table_id}: {e}")
            raise


def import_table_schema(client, dataset_id, table_id, output_dir='bq_schemas'):
    """
    Exporta o schema de uma tabela do BigQuery em um arquivo JSON no formato para 
    criar modelos com Pydantic.

    Parâmetros:
        client (bigquery.Client): O cliente do BigQuery utilizado para as operações.
        dataset_id (str): O ID do dataset.
        table_id (str): O ID da tabela.
        output_dir (str): O diretório onde o arquivo JSON será salvo. O padrão é 'bq_schemas'.
    
    Exceções:
        google.cloud.exceptions.NotFound: Se a tabela não for encontrada.

    Retorno:
        str: O caminho completo do arquivo JSON gerado e o tempo local
    """
    bq_id = dataset_id + '.' + table_id
    try:
        table = client.get_table(bq_id)
        schema = table.schema
        formatted_schema = {field.name: field.field_type for field in schema}
        os.makedirs(output_dir, exist_ok=True)
        schema_file_name = table.table_id.replace('.', '_') + '.json'
        schema_file_path = os.path.join(output_dir, schema_file_name)
        if os.path.exists(schema_file_path):
            print(f"O schema já foi importado em {schema_file_path}")
            return
        with open(schema_file_path, 'w') as file:
            json.dump(formatted_schema, file, indent=2)
            print(f"Schema importado com sucesso para: {schema_file_path} em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        with open(schema_file_path, 'r') as file:
          return json.load(file)
    except Exception as e:
        print(f"Erro ao exportar schema: {e}\n")
        raise

def send_data_to_bigquery(client, dataset_id, table_id, data):
    """
    Envia os dados mockados para tabelas no BigQuery.

    Parâmetros:
        client (bigquery.Client): instância do cliente do BigQuery.
        dataset_id (str): o ID do dataset onde a tabela está localizada.
        table_id (str): o ID da tabela onde os dados serão inseridos.
        data (dict): dados a serem enviados, no formato de lista de dicionários.

    Retorno:
        None: Apenas imprime mensagens informando o status do envio.
    """
    try:
        table_ref = client.dataset(dataset_id).table(table_id)
        table = client.get_table(table_ref)
        errors = client.insert_rows_json(table, data)
        if errors:
            print(f"Erro ao enviar: {errors}")
        else:
            print(f"{len(data)} linha(s) inserida(s) com sucesso para {table_id} em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")

    except Exception as e:
        print(f"Erro durante o envio para a tabela {table_id}: {e}")


def get_tables(dataset_id):
    """
    A função pega os nomes das tabelas e armazena em um array.

    Parâmetros:
        dataset_id (str): O nome do dataset que estão as tabelas.

    Retorno:
        list (str): Retorna os nomes em formato de lista.
    """
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)

    tables = client.list_tables(dataset_ref)

    table_list = []
    for table in tables:
        table_list.append(table.table_id)

    return table_list


def tranform_json_to_schema(file_path):
    """
    A função transforma o arquivo json em um schema do BigQuery.

    Parâmetros:
    file_path (str): O caminho do arquivo json que contém as tabelas.

    Retorno:
    list (str): Retorna os nomes em formato de lista.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    schema_big_query = []

    if 'schema' in data:
        for column in data['schema']:
            column_name = column['name']
            column_type = column['type']
            column_mode = column.get('mode', 'NULLABLE')
            schema_big_query.append(bigquery.SchemaField(column_name, column_type, mode=column_mode))
    return schema_big_query


# Geração de Bigquerry Schemas e Pydantic Models

def create_output_directory(output_dir):
    """
    Cria um diretório para a saída e garante que o arquivo __init__.py esteja presente.

    Parâmetros:
    output_dir (str): O diretório onde os arquivos serão salvos.

    Retorno:
    None: Não retorna nada.
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
        if field['type'] == 'RECORD' and 'fields' in field:
            # Trata campos aninhados recursivamente
            subfields = ", ".join(
                [f"bigquery.SchemaField('{f['name']}', '{f['type']}', '{f.get('mode', 'NULLABLE')}')" for f in field['fields']]
            )
            return f"    bigquery.SchemaField('{field['name']}', 'RECORD', '{field.get('mode', 'NULLABLE')}', fields=[{subfields}]),\n"
        else:
            return f"    bigquery.SchemaField('{field['name']}', '{field['type']}', '{field.get('mode', 'NULLABLE')}'),\n"

    class_definition = f"{table_name}_schema = [\n"
    for field in schema:
        class_definition += process_field(field)
    class_definition += "]\n"
    return class_definition

def process_bigquery_folder(folder_path, folder_name, output_dir):
    """
    Processa uma pasta contendo arquivos JSON e gera um arquivo de schema para o BigQuery.

    Parâmetros:
    folder_path (str): O caminho da pasta que contém os arquivos JSON.
    folder_name (str): O nome da pasta (dataset) a ser incluído nos comentários do arquivo de saída.
    output_dir (str): O diretório onde o arquivo de saída será salvo.

    Retorno:
    None: Não retorna nada.
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

    output_file_name = f"{folder_name}_schemas.py"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("from google.cloud import bigquery\n\n")
        output_file.write("\n\n".join(schemas))

def create_bigquery_schemas(directory='./bq_schemas'):
    """
    Cria schemas do BigQuery para todos os datasets em um diretório especificado.

    Parâmetros:
    directory (str): O caminho da pasta principal onde estão localizadas as subpastas (datasets).

    Retorno:
    None: Não retorna nada.
    """
    output_dir = "py_schemas"
    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_bigquery_folder(folder_path, folder_name, output_dir)

def create_class_code(schema: dict) -> str:
    def process_field(field):
        if field['type'] == 'RECORD' and 'fields' in field:
            # Gera classe aninhada para o campo RECORD
            class_name = field['name'].capitalize()
            nested_class = f"class {class_name}(BaseModel):\n"
            for subfield in field['fields']:
                subfield_type = TYPE_MAPPING.get(subfield['type'], "Any")
                nested_class += f"    {subfield['name']}: {subfield_type}\n"
            # Usa forward reference para campos que referenciam classes aninhadas
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

    # Adiciona classes aninhadas ao final
    if nested_classes:
        class_code += "\n\n" + "\n\n".join(nested_classes)

    class_code += "\n\n"
    return class_code


def process_pydantic_folder(folder_path, folder_name, output_dir):
    """
    Processa uma pasta contendo arquivos JSON e gera um arquivo de models Pydantic.

    Parâmetros:
    folder_path (str): O caminho da pasta que contém os arquivos JSON.
    folder_name (str): O nome da pasta (dataset) a ser incluído nos comentários do arquivo de saída.
    output_dir (str): O diretório onde o arquivo de saída será salvo.

    Retorno:
    None: Não retorna nada.
    """
    models = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                table = data.get("table")
                schema = data.get("schema")
                class_code = create_class_code({'table': table, 'schema': schema})
                models.append(f"# Dataset: {folder_name}, Table: {table}\n{class_code}")

    output_file_name = f"{folder_name}_models.py"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("from pydantic import BaseModel\n")
        output_file.write("from datetime import date, datetime\n")
        output_file.write("\n\n")
        output_file.write("\n\n".join(models))

def create_pydantic_models(directory='./bq_schemas'):
    """
    Cria classes Pydantic para todos os datasets em um diretório especificado.

    Parâmetros:
    directory (str): O caminho da pasta principal onde estão localizadas as subpastas (datasets).

    Retorno:
    None: Não retorna nada.
    """
    output_dir = "py_models"
    create_output_directory(output_dir)

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            process_pydantic_folder(folder_path, folder_name, output_dir)

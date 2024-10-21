# Este arquivo possui a implementação de funções auxiliares da aplicação
import json
import logging
import os
from pathlib import Path
from datetime import datetime
import csv
import importlib.util

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


def create_tables(client, dataset_id,table_name,schema):
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

    full_table_id = f"{client.project}.{dataset_id}.{table_name}"
    
    try:
        table = client.get_table(full_table_id)
        logging.info(f"Tabela {full_table_id} já existe.")
    except NotFound:
        try:
            table = bigquery.Table(full_table_id, schema=schema)
            table = client.create_tables(table)
            logging.info(f"Tabela {table.table_id} criada em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            logging.error(f"Erro ao criar a tabela {full_table_id}: {e}")
            raise

def load_py_schema(dataset_name):
    """
    Carrega o schema do dataset de um arquivo JSON que contém todas as tabelas.

    Parâmetros:
        schema_path (str): O caminho para o arquivo JSON do schema do dataset.

    Retorno:
        dict: Um dicionário onde as chaves são os nomes das tabelas e os valores são os schemas.
    """
    py_schema_path = os.path.join('py_schemas', f"{dataset_name}.py") # type: ignore
    if os.path.exists(py_schema_path):
        spec = importlib.util.spec_from_file_location(f"{dataset_name}", py_schema_path)
        schema_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(schema_module)
        return schema_module
    else:
        return None

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

    class_definition = f"{table_name} = [\n"
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

    output_file_name = f"{folder_name}.py"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write("from google.cloud import bigquery\n\n")
        output_file.write("\n\n".join(schemas))

def create_bigquery_schemas(directory):
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

def output_to_csv(array):
    csv_file = "dados.csv"

    with open(csv_file,mode='w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(array)
    print("Arquivo CSV salvo")

def create_dataset_and_tables():
    """
    Cria datasets e tabelas no BigQuery para cada dataset e tabela no diretório.

    Esta função cria um dataset no BigQuery para cada subpasta no diretório especificado.
    Em seguida, carrega os schemas correspondentes da outra pasta e cria as tabelas no dataset recém-criado.

    Parâmetros:
        directory (str): O caminho do diretório onde estão as subpastas que representam datasets e tabelas.
        schema_directory (str): O caminho do diretório onde estão os arquivos de schema.
    """
    client = bigquery.Client(project=PROJECT_ID)

    # Navegar pelas pastas dos datasets
    for dataset_folder in os.listdir('bq_schemas'):
        dataset_path = os.path.join('bq_schemas', dataset_folder) 

        if os.path.isdir(dataset_path):
            # Criar o dataset no BigQuery
            dataset_id = f"{PROJECT_ID}.{dataset_folder}"
            dataset = bigquery.Dataset(dataset_id)
            dataset.location = "US"
            client.create_dataset(dataset, exists_ok=True)
            print(f"Dataset criado: {dataset_id}")

            # Carregar o schema Python correspondente ao dataset
            schema_module = load_py_schema(dataset_folder)

            if schema_module:
                # Navegar pelas tabelas dentro da pasta do dataset
                for table_file in os.listdir(dataset_path):
                    table_name = table_file.replace('.json', '')
                    schema = getattr(schema_module, f"{table_name}", None)
                    
                    if schema:
                        table_id = f"{dataset_id}.{table_name}"
                        table = bigquery.Table(table_id, schema=schema)
                        client.create_table(table, exists_ok=True)
                    else:
                        print(f"Schema não encontrado para a tabela {table_name} no dataset {dataset_folder}")
            else:
                print(f"Arquivo de schema Python não encontrado para o dataset {dataset_folder}")
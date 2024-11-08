import importlib.util
import os
from datetime import date, datetime
from decimal import Decimal
import subprocess

from auth import get_bigquery_client
from google.cloud import bigquery,secretmanager
from google.oauth2 import service_account

from config import PROJECT_ID, logger


def load_py_schema(dataset_name):
    """
    Carrega o schema de um dataset a partir de um arquivo Python.

    Parâmetros:
        dataset_name (str): Nome do dataset.

    Retorno:
        Módulo importado que contém o schema, ou None se o arquivo não existir.
    """
    py_schema_path = os.path.join('py_schemas', f"{dataset_name}.py")
    if os.path.exists(py_schema_path):
        spec = importlib.util.spec_from_file_location(f"{dataset_name}", py_schema_path)
        schema_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(schema_module)
        return schema_module
    return None


def jsonl_to_bigquery(filename, table_id, dataset_id):
    """
    Carrega dados de um arquivo JSONL para o BigQuery.

    Abre um arquivo JSONL que contém dados gerados e envia para uma tabela específica
    no BigQuery, utilizando configuração de trabalho de carga.

    Exceções:
        Gera exceções caso ocorra algum erro durante o carregamento dos dados.
    """

    client = get_bigquery_client()
    jsonl_file_path = f"mock_data/{dataset_id}/{filename}"
    project_id = PROJECT_ID
    dataset_id = dataset_id
    table_id = table_id

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=False,
        ignore_unknown_values=True,
    )

    with open(jsonl_file_path, "rb") as jsonl_file:
        load_job = client.load_table_from_file(jsonl_file, table_ref, job_config=job_config)

    load_job.result()


def create_tables():
    """
    Cria tabelas no BigQuery a partir dos schemas definidos e aplica particionamento se configurado.

    Para cada dataset e tabela, carrega o schema correspondente do arquivo Python,
    exclui algumas tabelas de serem particionadas e cria a tabela no dataset no BigQuery.

    Exceções:
        Gera exceções e loga erros caso ocorra algum problema durante a criação das tabelas.
    """

    client = get_bigquery_client()

    excluded_partition_tables = ["cobranca_telefone", "acordo", "cliente"]
    datasets = list(client.list_datasets())
    datasets_created = [dataset.dataset_id for dataset in datasets]

    for dataset_folder in os.listdir('bq_schemas'):
        dataset_path = os.path.join('bq_schemas', dataset_folder)

        if os.path.isdir(dataset_path) and dataset_folder in datasets_created:
            dataset_id = f"{PROJECT_ID}.{dataset_folder}"
            schema_module = load_py_schema(dataset_folder)

            if schema_module:
                for table_file in os.listdir(dataset_path):
                    table_name = table_file.replace('.json', '')

                    schema = getattr(schema_module, f"{table_name}", None)

                    if schema:
                        table_id = f"{dataset_id}.{table_name}"
                        table = bigquery.Table(table_id, schema=schema)

                        partition_field = None
                        partition_type = None
                        if table_name not in excluded_partition_tables:
                            for field in schema:
                                if field.name.startswith("num_anomes") or field.name.startswith("production_date") or field.name.startswith("dat_referencia"):
                                    if field.field_type in ["TIMESTAMP", "DATE", "DATETIME"]:
                                        partition_field = field.name
                                        partition_type = "MONTH" if field.name.startswith("num_anomes") or field.name.startswith("production_date") else "DAY"
                                        break
                                    else:
                                        logger.error(f"O campo {field.name} na tabela {table_name} não é do tipo TIMESTAMP, DATE ou DATETIME. Particionamento ignorado.")

                            if partition_field and partition_type:
                                table.time_partitioning = bigquery.TimePartitioning(
                                    type_=partition_type,
                                    field=partition_field
                                )
                                logger.info(f"Particionamento {partition_type} configurado para {table_name} na coluna {partition_field}")
                            else:
                                logger.error(f"Tabela {table_name} sem campo de particionamento configurado.")

                        client.create_table(table, exists_ok=True)
                        update_table_descriptions_from_schemas("py_schemas")
                        logger.info(f"Tabela {table_name} criada no dataset {dataset_folder}")
                    else:
                        logger.error(f"Schema não encontrado para a tabela {table_name} no dataset {dataset_folder}")
            else:
                logger.error(f"Arquivo de schema Python não encontrado para o dataset {dataset_folder}")
        else:
            logger.error(f"Dataset {dataset_folder} não encontrado no BigQuery")


def load_schema_module(schema_file):
    """
    Carrega um módulo de schema Python a partir de um arquivo.

    Parâmetros:
        schema_file (str): Caminho para o arquivo de schema.

    Retorno:
        Módulo importado que contém o schema.
    """
    if not os.path.isfile(schema_file):
        raise FileNotFoundError(f"O arquivo '{schema_file}' não foi encontrado.")

    spec = importlib.util.spec_from_file_location("schema_module", schema_file)
    if spec is None:
        raise ImportError(f"Não foi possível criar o spec para o arquivo '{schema_file}'.")

    schema_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(schema_module)
    return schema_module


def update_table_descriptions_from_schemas(schema_directory):
    """
    Atualiza as descrições das tabelas no BigQuery usando schemas Python.

    Para cada arquivo de schema no diretório especificado, carrega o módulo e
    atualiza as descrições das tabelas no BigQuery com base nos schemas fornecidos.

    Parâmetros:
        schema_directory (str): Caminho para o diretório com os arquivos de esquema Python.

    Exceções:
        Loga erros caso ocorra algum problema ao atualizar as descrições das tabelas.
    """
    client = get_bigquery_client()

    for schema_file in os.listdir(schema_directory):
        dataset_id = schema_file.replace('.py', '')
        schema_file_path = os.path.join(schema_directory, schema_file)

        schema_module = load_schema_module(schema_file_path)
        table_schemas = {name: value for name, value in schema_module.__dict__.items() if isinstance(value, list)}

        for table_id, schema_fields in table_schemas.items():
            table_ref = f"{PROJECT_ID}.{dataset_id}.{table_id}"
            try:
                existing_table = client.get_table(table_ref)
                updated_schema = []

                for schema_field in existing_table.schema:
                    matching_field = next((f for f in schema_fields if f.name == schema_field.name), None)
                    if matching_field:
                        updated_schema.append(matching_field)
                    else:
                        updated_schema.append(schema_field)

                existing_table.schema = updated_schema
                client.update_table(existing_table, ["schema"])
                logger.info(f"Tabela '{table_ref}' atualizada com descrições.")
            except Exception as e:
                logger.error(f"Erro ao atualizar tabela '{table_ref}': {e}")

def jsonl_data(data):
    """
    Salva dados em arquivos JSONL, convertendo automaticamente datas e decimais 
    para formatos compatíveis com JSON.

    Parâmetros:
    data (dict): Dicionário onde as chaves são nomes de arrays e os valores são listas de dicionários.
    """
    # Obtendo o nome do arquivo chamador para definir o nome do dataset
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    dataset_name = os.path.splitext(os.path.basename(caller_file))[0]

    # Definindo o caminho de saída
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    output_path = os.path.join(project_root, "src/mock_data", dataset_name)
    os.makedirs(output_path, exist_ok=True)

    def serialize_data(item):
        """Converte datas, decimais e processa dados aninhados para compatibilidade JSON."""
        if isinstance(item, datetime):
            return item.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(item, date):
            return item.strftime('%Y-%m-%d')
        elif isinstance(item, Decimal):
            return float(item)
        elif isinstance(item, dict):
            return {k: serialize_data(v) for k, v in item.items()}
        elif isinstance(item, list):
            return [serialize_data(i) for i in item]
        return item

    # Salvando os dados no formato JSONL
    for array_name, array_data in data.items():
        filename = f"{array_name}.jsonl"
        filepath = os.path.join(output_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in array_data:
                serialized_item = serialize_data(item)
                json.dump(serialized_item, f, ensure_ascii=False)
                f.write('\n')

    return data


def run_command(command: str) -> str:
    """Execute a gcloud command and return the output.

    Args:
        command (str): The gcloud command to be executed.

    Returns:
        str: The standard output from the command execution.
    """
    result = subprocess.run(
        command, capture_output=True, text=True, shell=True, check=False
    )
    return result.stdout.strip()

def gcloud_list(
    resource_type: str, project_id: str, credentials: str, dataset_id: str
) -> list:
    """List various resources from Google Cloud based on the specified type.

    Args:
        resource_type (str): The type of resource to list. Options are:
            'projects', 'secrets', 'datasets', 'tables'.
        project_id (str): The project ID used for resource queries.
        credentials (str): Credentials for accessing BigQuery.
        dataset_id (str): The dataset ID, required for listing tables.

    Returns:
        list: A list of resource identifiers (e.g., project IDs, secret names,
        dataset IDs, or table IDs) based on the specified resource type.

    Raises:
        ValueError: If an unknown resource type is provided.
    """
    if resource_type == 'projects':
        command = "gcloud projects list --format='value(projectId)'"
    elif resource_type == 'secrets':
        command = f"gcloud secrets list --project={project_id} --format='value(name)'"
    elif resource_type in {'datasets', 'tables'}:
        client = bigquery.Client(credentials=credentials, project=project_id)
        if resource_type == 'datasets':
            datasets = client.list_datasets(project_id)
            return [dataset.dataset_id for dataset in datasets]
        elif resource_type == 'tables':
            tables = client.list_tables(dataset_id)
            return [table.table_id for table in tables]
    else:
        raise ValueError(f'Unknown resource type: {resource_type}')

    return run_command(command).splitlines()

def gcloud_choose(
    resource_type: str,
    project_id: str = None,
    credentials: str = None,
    dataset_id: str = None,
) -> str:
    """Prompt the user to choose a resource from a list.

    Args:
        resource_type (str): The type of resource to list and choose from.
        project_id (str, optional): The project ID used for resource queries.
        credentials (str, optional): Credentials for accessing BigQuery.
        dataset_id (str, optional): The dataset ID, required for listing tables.

    Returns:
        str: The chosen resource identifier, or None if no valid choice is made.

    Raises:
        ValueError: If an unknown resource type is provided.
    """
    choices = gcloud_list(
        resource_type=resource_type,
        project_id=project_id,
        credentials=credentials,
        dataset_id=dataset_id,
    )

    if not choices:
        return None

    logger.info(f'\033[33mAvailable {resource_type}:\033[0m')
    for i, choice in enumerate(choices, start=1):
        logger.info(f'{i}. {choice}')

    choice_index = int(input('> Enter the option number: ')) - 1
    if 0 <= choice_index < len(choices):
        return choices[choice_index]
    else:
        return None
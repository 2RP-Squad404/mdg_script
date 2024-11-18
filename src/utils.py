import importlib.util
import inspect
import os
from datetime import date, datetime
from decimal import Decimal
import subprocess
import json
import glob
import re

from auth import get_bigquery_client,secretmanager
from google.oauth2 import service_account
from google.cloud import bigquery

from config import PROJECT_ID, logger
import importlib.metadata

def jsonl_to_bigquery(filename, table_id, dataset_id):
    """
    Carrega dados de um arquivo JSONL para o BigQuery.

    Parâmetros:
        filename (str): Nome do arquivo JSONL.
        table_id (str): Nome da tabela no BigQuery.
        dataset_id (str): Nome do dataset no BigQuery.
    """

    client = get_bigquery_client()
    jsonl_file_path = filename 
    project_id = PROJECT_ID
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=False,
        ignore_unknown_values=True,
    )

    with open(jsonl_file_path, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file, table_ref, job_config=job_config
        )
    
    load_job.result()

def create_tables(dataset: str):
    """
    Cria tabelas no BigQuery para o dataset especificado, aplicando particionamento onde configurado.

    Parâmetros:
        dataset (str): Nome do dataset no qual as tabelas serão criadas.

    Exceções:
        Loga erros caso ocorra algum problema durante a criação das tabelas.
    """

    client = get_bigquery_client()  # Supondo que a função para obter o cliente já está configurada

    dataset_path = os.path.join("py_schemas", dataset)  # Caminho para os schemas do dataset
    excluded_partition_tables = ["cobranca_telefone", "acordo", "cliente", "dw_funcionario", "adesoes_pfin", 
                                 "faturas_pfin", "garantias_seguros", "motivos_cancelamentos", 
                                 "produtos_financeiros", "tipos_canais", "tipos_cancelamentos", 
                                 "v_credit_card", "v_credit_limit", "v_credit_person", 
                                 "v_debit_account", "v_debit_person", "funcionarios", "v_estabelecimento"]

    # Verifica se o diretório do dataset existe no sistema de arquivos
    if os.path.isdir(dataset_path):
        dataset_id = f"{PROJECT_ID}.{dataset}"
        schema_module = load_py_schema(dataset)  # Função que carrega o módulo de schema Python para o dataset

        if schema_module:
            # Itera sobre os arquivos no diretório do dataset
            for table_file in os.listdir(dataset_path):
                if table_file.endswith('.py'):  # Considerando que os schemas são arquivos .py
                    table_name = table_file.replace('.py', '')

                    # Obtém o schema da tabela a partir do módulo de schemas Python
                    schema = getattr(schema_module, table_name, None)

                    if schema:
                        table_id = f"{dataset_id}.{table_name}"
                        table = bigquery.Table(table_id, schema=schema)

                        partition_field = None
                        partition_type = None

                        # Configura particionamento para tabelas que não estão na lista de exclusão
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
                                logger.warning(f"Tabela {table_name} sem campo de particionamento configurado.")

                        client.create_table(table, exists_ok=True)
                        update_table_descriptions_from_schemas("py_schemas")
                        logger.info(f"Tabela {table_name} criada no dataset {dataset}")
                    else:
                        logger.error(f"Schema não encontrado para a tabela {table_name} no dataset {dataset}")
        else:
            logger.error(f"Arquivo de schema Python não encontrado para o dataset {dataset}")
    else:
        logger.info(f"Procurando schema para o dataset: {dataset} no caminho: {dataset_path}")


def load_py_schema(dataset_name):
    """
    Carrega o módulo Python do schema a partir do nome do dataset.

    Parâmetros:
        dataset_name (str): Nome do dataset.

    Retorno:
        module: Módulo Python carregado, ou None se não encontrado.
    """
    module_path = os.path.join("py_schemas", dataset_name, f"{dataset_name}.py")
    if os.path.exists(module_path):
        spec = importlib.util.spec_from_file_location(dataset_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None


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
        if os.path.isdir(os.path.join(schema_directory, schema_file)) or not schema_file.endswith('.py'):
            continue

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
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    dataset_name = os.path.splitext(os.path.basename(caller_file))[0]

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    output_path = os.path.join(project_root, "src/mock_data", dataset_name)
    os.makedirs(output_path, exist_ok=True)

    def serialize_data(item):
        """
        Converte datas, decimais e processa dados aninhados para compatibilidade JSON.

        Parâmetros:
            item (dict): Dicionário a ser serializado.

        Retorno:
            dict: Dicionário serializado.
        """
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
    """
    Executa um comando gcloud e retorna a saída.

    Parâmetro:
        command (str): Comando a ser executado.

    Returno:
        str: Saída do comando.
    """
    result = subprocess.run(
        command, capture_output=True, text=True, shell=True, check=False
    )
    return result.stdout.strip()

def gcloud_list(
    resource_type: str, project_id: str, credentials: str, dataset_id: str) -> list:
    """
    Lista recursos do Google Cloud com base no tipo especificado.

    Parâmetros:
        resource_type (str): Tipo de recurso a ser listado.
        project_id (str): ID do projeto.
        credentials (str): Arquivo de credenciais do Google Cloud.
        dataset_id (str): ID do dataset.

    Returno:
        list: Lista de recursos.
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
    """
    Prompt the user to choose a resource from a list.
    Opcionalmente, você pode especificar o tipo de recurso, projeto e credenciais

    Parâmetro:
        resource_type (str): Tipo de recurso a ser escolhido.
        project_id (str): ID do projeto.
        credentials (str): Arquivo de credenciais do Google Cloud.
        dataset_id (str): ID do dataset.

    Returno
        str: Nome do recurso escolhido.
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
    
def get_credentials(secret_name: str):
    """Retrieve service account credentials from Google Cloud Secret Manager.

    Parâmetros::
        secret_name (str): The full resource name of the secret version.

    Retorno:
        tuple: A tuple containing the credentials object and the credentials dictionary.
    """
    secret_client = secretmanager.SecretManagerServiceClient()
    response = secret_client.access_secret_version(name=secret_name)
    credentials_dict = json.loads(response.payload.data.decode('utf-8'))

    credentials = service_account.Credentials.from_service_account_info(
        credentials_dict
    )
    return credentials, credentials_dict

def list_datasets_from_folder(folder_path: str, folder_file: str) -> list:
    """
    Lista arquivos de dataset ou subpastas na pasta especificada, removendo a extensão .py dos arquivos.

    Parâmetros:
        folder_path (str): Caminho para a pasta que contém os arquivos ou subpastas.
        folder_file (str): Especifica o que listar. Use 'file' para arquivos ou 'folder' para subpastas.

    Retorno:
        list: Lista dos nomes dos arquivos sem a extensão .py ou das subpastas.
    """
    if folder_file == 'folder':
        return [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    elif folder_file == 'file':
        return [os.path.splitext(f)[0] for f in os.listdir(folder_path)
                if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.py')]
    else:
        raise ValueError("Invalid value for 'folder_file'. Use 'file' or 'folder'.")

def list_datasets_from_bigquery() -> list:
    """
    Lista os datasets disponíveis no BigQuery.

    Retorno:
        list: Lista dos nomes dos datasets no BigQuery.
    """
    client = bigquery.Client(project=PROJECT_ID)
    datasets = client.list_datasets()
    return [dataset.dataset_id for dataset in datasets]

def list_tables_from_bigquery(dataset):
    """
    Lista as tabelas do BigQuery

    Parâmetro:
        dataset (str): Nome do dataset no BigQuery.

    Returno:
        list: Lista dos nomes das tabelas no dataset.
    """
    client = bigquery.Client(project=PROJECT_ID)
    tables = client.list_tables(dataset)
    return [table.table_id for table in tables]

def list_tables_from_folder(folder_path: str) -> list:
    """
    Lista os arquivos de dataset na pasta especificada.

    Parâmetro:
        folder_path (str): Caminho para a pasta que contém os arquivos.

    Returno:
        list: Lista dos nomes dos arquivos de dataset.
    """

    return [os.path.splitext(f)[0] for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.py')]

def display_common_datasets(folder_path: str):
    """
    Exibe e permite a seleção opcional dos datasets que estão em comum entre a pasta local e o BigQuery.

    Parâmetro:
        folder_path (str): Caminho para a pasta que contém os arquivos.

    Retorno:
        list: Lista de datasets selecionados ou todos os datasets em comum, se nenhuma seleção for feita.
    """
    local_datasets = list_datasets_from_folder(folder_path,folder_file='folder')
    bq_datasets = list_datasets_from_bigquery()

    common_datasets = sorted(set(local_datasets) & set(bq_datasets))

    if not common_datasets:
        logger.info("\033[91mNenhum dataset em comum encontrado.\033[0m")
        return []

    logger.info("\033[32mDatasets em comum:\033[0m")
    for i, dataset in enumerate(common_datasets, start=1):
        print(f"{i}. {dataset}")

    user_input = input("\nDigite os números do dataset:").strip()

    if not user_input:
        return common_datasets

    selected_indexes = [int(x) - 1 for x in user_input.split(",") if x.isdigit()]
    selected_dataset = [
        common_datasets[i] for i in selected_indexes if 0 <= i < len(common_datasets)
    ]

    return selected_dataset[0]

def commom_tables(dataset_file):
    """
    Exibe e permite a seleção opcional das tabelas que estão em comum entre o diretório e o BigQuery.

    Parâmetros:
        dataset_file (str): Nome do arquivo do dataset.
    """
    from gemini_interface import run_gemini

    local_tables = list_tables_from_folder(f"mock_data/{dataset_file}")
    bigquery_tables = list_tables_from_bigquery(dataset_file)

    tables_created = sorted(set(local_tables) & set(bigquery_tables))

    if not tables_created:
        logger.info("\033[91mNenhuma tabela em comum encontrada.\033[0m")
    
    logger.info("\033[32mDatasets em comum:\033[0m")
    for table in bigquery_tables:
        if table in tables_created:
            logger.info(f"Processando tabela existente: {table}")
        else:
            logger.info(f"Tabela não encontrada localmente, gerando dados: {table}")
        
        run_gemini(PROJECT_ID, model_name="gemini-1.5-flash-002",dataset=dataset_file)

def input_num_linhas():
    """
    Gerar um número de linhas para o arquivo de saída.

    Returno:
        int: Número de linhas para o arquivo de saída.
    """
    while True:
        try:
            num_linhas = int(input("Quantas linhas deseja gerar?\n"))
            return num_linhas
        except ValueError:
            logger.info("Digite um valor inteiro")

def send_jsonl_to_bigquery(select_dataset):
    """
    Envia o arquivo JSONL para o BigQuery.

    Parâmetros:
        select_dataset (str): Nome do dataset a ser enviado.
    """
    dataset_directory = f"mock_data/{select_dataset}"
    
    if not os.path.isdir(dataset_directory):
        logger.error(f"\033[91mO diretório {dataset_directory} não existe.\033[0m")
        return

    for filename in os.listdir(dataset_directory):
        if filename.endswith(".jsonl"):
            table_id = os.path.splitext(filename)[0]

            try:
                jsonl_file_path = os.path.join(dataset_directory, filename)

                jsonl_to_bigquery(filename=jsonl_file_path, table_id=table_id, dataset_id=select_dataset)
                logger.info(f'\033[32mArquivo {filename} enviado para a tabela {table_id} no dataset {select_dataset}\033[0m')
            except Exception as e:
                logger.error(f"\033[91mErro ao enviar o arquivo {filename} para o BigQuery: {e}\033[0m")

def load_models_and_examples(dataset: str, prompt) -> str:
    """
    Carrega modelos e exemplos para o dataset especificado.

    Parâmetros:
        dataset (str): Nome do dataset.
        prompt (str): Prompt para o modelo.

    Retorno:
        str: Nome do arquivo de saída.
    """
    models_dir = f'py_models'
    models_code = []

    for filename in os.listdir(models_dir):
        if filename.endswith('.py'):
            with open(
                os.path.join(models_dir, filename), 'r', encoding='utf-8'
            ) as f:
                models_code.append(f.read())

    models_code_str = '\n\n'.join(models_code)

    json_files_pattern = f'src/data_sample_json/{dataset}/*.json'
    json_file_paths = glob.glob(json_files_pattern)
    examples_data = []

    for json_file_path in json_file_paths:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            examples_data.append(json.load(f))

    examples_data_str = json.dumps(examples_data, indent=2, ensure_ascii=False)

    # Carregar exemplo de retorno esperado (agora com o caminho fixo 'example.py')
    logger.debug(os.getcwd())
    expected_return_file = 'datagen/pfs_risco_raw_tivea.py'
    with open(expected_return_file, 'r', encoding='utf-8') as f:
        expected_return_code = f.read()

    full_prompt = prompt.replace(
        '#colocar nessa linha os modelos do py_models/{dataset}/*.py',
        models_code_str,
    )
    full_prompt = full_prompt.replace(
        '#colocar nessa linha o json com os dados de exemplo do data_sample_json/{dataset}/*.json',
        examples_data_str,
    )
    full_prompt = full_prompt.replace(
        '#colocar nessa linha algum py com um exemplo de retorno esperado do example_of_expected_return/{dataset}.py',
        expected_return_code,
    )

    return full_prompt


def save_code_from_gemini(dataset: str, content: str):
    """
    Escreve a resposta obtida do modelo no arquivo 'gemini_datagen.py'.

    Parâmetros:
    content (str): O código obtido do modelo.
    """
    content = re.sub(
        r'^```(python)?\s*', '', content
    ) 
    content = re.sub(r'```$', '', content)

    # Define o diretório e o caminho do arquivo
    pathdir = 'datagen'
    os.makedirs(pathdir, exist_ok=True)  # Cria o diretório se não existir

    file_path = os.path.join(pathdir, f'{dataset}.py')

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)

    return True


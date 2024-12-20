# Este arquivo possui a implementação de funções auxiliares da aplicação
import importlib.util
import os
from datetime import datetime

from google.cloud import bigquery

from auth import get_bigquery_client
from config import PROJECT_ID

client = get_bigquery_client()


def load_py_schema(dataset_name):
    """
    Carrega o schema do dataset de um arquivo JSON que contém todas as tabelas.

    Parâmetros:
        schema_path (str): O caminho para o arquivo JSON do schema do dataset.

    Retorno:
        dict: Um dicionário onde as chaves são os nomes das tabelas e os valores são os schemas.
    """
    py_schema_path = os.path.join('py_schemas', f"{dataset_name}.py")  # type: ignore
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
    dataset_ref = client.dataset(dataset_id)

    tables = client.list_tables(dataset_ref)

    table_list = []
    for table in tables:
        table_list.append(table.table_id)

    return table_list


def jsonl_to_bigquery(filename, table_id, dataset_id):
    """
    A função abre um arquivo jasonl que contém os dados gerados e envia para o Big Query
    """
    jsonl_file_path = f"jsonl_mock/{filename}"
    project_id = PROJECT_ID
    dataset_id = dataset_id
    table_id = table_id

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        autodetect=False,
        ignore_unknown_values=True
    )

    with open(jsonl_file_path, "rb") as jsonl_file:
        load_job = client.load_table_from_file(jsonl_file, table_ref, job_config=job_config)

    load_job.result()


def create_tables():
    """
    Cria tabelas no BigQuery para cada dataset e tabela no diretório.

    Carrega os schemas correspondentes da outra pasta e cria as tabelas no dataset que já tem criado,
    excluindo algumas tabelas de serem particionadas.
    """

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
                                        print(f"O campo {field.name} na tabela {table_name} não é do tipo TIMESTAMP, DATE ou DATETIME. Particionamento ignorado.")

                            if partition_field and partition_type:
                                table.time_partitioning = bigquery.TimePartitioning(
                                    type_=partition_type,
                                    field=partition_field
                                )
                                print(f"Particionamento {partition_type} configurado para {table_name} na coluna {partition_field}")
                            else:
                                print(f"Tabela {table_name} sem campo de particionamento configurado.")

                        client.create_table(table, exists_ok=True)
                        print(f"Tabela {table_name} criada no dataset {dataset_folder}")
                    else:
                        print(f"Schema não encontrado para a tabela {table_name} no dataset {dataset_folder}")
            else:
                print(f"Arquivo de schema Python não encontrado para o dataset {dataset_folder}")
        else:
            print(f"Dataset {dataset_folder} não encontrado no BigQuery")

def load_schema_module(schema_file):
    """Carrega o módulo de esquema Python a partir de um arquivo."""
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
    Atualiza  as descrições das tabelas do BigQuery com base nos esquemas Python do  diretório 'py_schemas'.

    Parâmetros:
    schema_directory: Caminho para o diretório com os arquivos de esquema Python
    """
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
                print(f"Tabela '{table_ref}' atualizada com descrições.")
            except Exception as e:
                print(f"Erro ao atualizar tabela '{table_ref}': {e}")

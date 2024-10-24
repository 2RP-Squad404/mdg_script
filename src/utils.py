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


def output_to_csv(array):
    csv_file = "dados.csv"

    with open(csv_file,mode='w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(array)
    print("Arquivo CSV salvo")

def create_tables():
    """
    Cria tabelas no BigQuery para cada dataset e tabela no diretório.

    Carrega os schemas correspondentes da outra pasta e cria as tabelas no dataset que já tem criado.

    Parâmetros:
        directory (str): O caminho do diretório onde estão as subpastas que representam datasets e tabelas.
        schema_directory (str): O caminho do diretório onde estão os arquivos de schema.
    """
    client = bigquery.Client(project=PROJECT_ID)

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
                        client.create_table(table, exists_ok=True)
                    else:
                        print(f"Schema não encontrado para a tabela {table_name} no dataset {dataset_folder}")
            else:
                print(f"Arquivo de schema Python não encontrado para o dataset {dataset_folder}")
        else:
            print(f"Dataset {dataset_folder} não encontrado no BigQuery")
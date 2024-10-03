# Este arquivo possui a implementação de funções auxiliares da aplicação
# Como por exemplo: Criar tabelas, Extrair schemas e Extrair dados

from google.api_core.exceptions import NotFound
from google.cloud import bigquery

from config import settings
from schemas import bigquery_schema_account, bigquery_schema_card, bigquery_schema_person

# Criar uma tabela a partir de um schema

client = bigquery.Client()

# Parâmetros do GCP
# ID do projeto
project_id = settings.PROJECT_ID

# ID do dataset
dataset_name = settings.PFS_UNIFICACAO_PEFISA_DATASET_ID

# Nome das tabelas 
table_person = f"{project_id}.{dataset_name}.mock_simple_persons"
table_account = f"{project_id}.{dataset_name}.mock_simple_account"
table_card = f"{project_id}.{dataset_name}.mock_simple_card"


def check_and_create_table(client, table_id, schema):
    try:
        client.get_table(table_id)  # Tenta pegar a tabela
        print(f"Tabela {table_id} já existe.")
    except NotFound:
        # Cria a tabela se ela não existir
        table = bigquery.Table(table_id, schema=schema)
        client.create_table(table)
        print(f"Tabela {table_id} criada com sucesso.")


check_and_create_table(client, table_person, bigquery_schema_person)
check_and_create_table(client, table_account, bigquery_schema_account)
check_and_create_table(client, table_card, bigquery_schema_card)

from google.cloud import bigquery
from auth import get_bigquery_client
from utils import create_tables,jsonl_to_bigquery

# client = get_bigquery_client()
directory = './bq_schemas'

create_tables()
# - Criar dataset e tabelas
# ...
# - Enviar dados via jsonl
jsonl_to_bigquery()
# ...


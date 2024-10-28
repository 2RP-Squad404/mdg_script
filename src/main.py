from google.cloud import bigquery
from config import PROJECT_ID
from utils import create_tables,jsonl_to_bigquery

# client = bigquery.Client('big-maxim-430019-g7')

directory = './bq_schemas'

create_tables()
# - Criar dataset e tabelas
# ...
# - Enviar dados via jsonl
jsonl_to_bigquery()
# ...


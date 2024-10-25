from google.cloud import bigquery
from config import PROJECT_ID
from utils import create_bigquery_schemas,create_dataset_and_tables,create_pydantic_models

client = bigquery.Client(PROJECT_ID)
import csv
from gemini_datagen import criar_adesao_debito_automatico
# client = bigquery.Client('big-maxim-430019-g7')

directory = './bq_schemas'

create_dataset_and_tables()
# - Criar dataset e tabelas
# ...
# - Enviar dados via csv
# ...


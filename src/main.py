from google.cloud import bigquery
from config import PROJECT_ID
from utils import create_tables

client = bigquery.Client(PROJECT_ID)
import csv
from gemini_datagen import criar_adesao_debito_automatico
# client = bigquery.Client('big-maxim-430019-g7')

directory = './bq_schemas'

create_tables()
# - Criar dataset e tabelas
# ...
# - Enviar dados via csv
# ...


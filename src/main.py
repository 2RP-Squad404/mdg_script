from google.cloud import bigquery

from config import PROJECT_ID

client = bigquery.Client(PROJECT_ID)

# Ações que o main.py irá executar:

# - Criar dataset e tabelas

# - Enviar dados via csv

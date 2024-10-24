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

# Criação do csv para envio ao BigQuery
with open('adesao_debito_automatico.csv', mode='w', newline='') as csv_file:
    table_colunms = ['hash_key', 'source', 'id', 'dataadesao', 
        'id_contadigital', 'id_contacredito', 'id_tipodebitoautomatico', 'descricaotipodebitoautomatico', 'responsavel', 
        'datacancelamento', 'responsavelcancelamento', 'dh_relatorio', 'operation', 'operation_sequence', 'production_date']
    
    csv_w = csv.DictWriter(csv_file, fieldnames=table_colunms)
    csv_w.writeheader()
    for  _ in range(100):
        csv_w.writerow(criar_adesao_debito_automatico())

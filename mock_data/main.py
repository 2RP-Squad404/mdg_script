
## ESTE ARQUIVO É RESPONSÁVEL POR ENVIAR OS DADOS PARA AS TABELAS DO BIGQUERY 
from config import settings
from google.cloud import bigquery
from datagen import generate_mock_data_test 

def send(mock_data, dataset_id, table_id):
    client = bigquery.Client()
    
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)
    
    line_mock_data = [mock_data]
    errors = client.insert_rows_json(table, line_mock_data)
    
    if errors:
        print(f"Erro ao enviar: {errors}")
    else:
        print("Dados enviados")
        
mock_data = []

for i in range(10):
    mock_data.append(generate_mock_data_test())

# for j in range(10):
#     print(mock_data[j])
dataset_id = 'mock_pfs_unificacao_pefisa'
table_id = 'mock_data'


for k in range(10):
    send(mock_data[k], dataset_id, table_id)
    

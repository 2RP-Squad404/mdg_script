import time

# from auth import client
from google.cloud import bigquery 
from config import settings
from datagen import generate_cardevent

start = time.time()
client = bigquery.Client()

num_of_lines = input("Quantas linhas você deseja inserir na tabela Card? ")

def send_to_card_table(card_mock_data, dataset_id, table_id):

    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    line_mock_data = [card_mock_data]
    errors = client.insert_rows_json(table, line_mock_data)

    if errors:
        print(f"Erro ao enviar: {errors}")


card_mock_data = []

for i in range(int(num_of_lines)):
    card_mock_data.append(generate_cardevent())

dataset_id = settings.PFS_UNIFICACAO_PEFISA_DATASET_ID
table_id = settings.MOCK_CARD_TABLE_ID


for k in range(int(num_of_lines)):
    send_to_card_table(card_mock_data[k], dataset_id, table_id)
    print("Enviando dados..." + f"Restam {int(num_of_lines) - k} linhas.")

end_code = time.time()

print(f"Envio dos dados finalizado em {(end_code - start):.2f}ms")

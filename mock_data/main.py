
from config import settings
from datagen import generate_cardevent
from google.cloud import bigquery


def send_to_card_table(card_mock_data, dataset_id, table_id):
    client = bigquery.Client()

    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)

    line_mock_data = [card_mock_data]
    errors = client.insert_rows_json(table, line_mock_data)

    if errors:
        print(f"Erro ao enviar: {errors}")
    else:
        print("Dados enviados")


card_mock_data = []

for i in range(50):
    card_mock_data.append(generate_cardevent())

# for j in range(10):
#     print(mock_data[j])
dataset_id = settings.PFS_UNIFICACAO_PEFISA_DATASET_ID
table_id = settings.MOCK_CARD_TABLE_ID


for k in range(50):
    send_to_card_table(card_mock_data[k], dataset_id, table_id)

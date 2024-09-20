from datagen import generate_cardevent
from bq_table import client, table_id

# rows to insert in table 

card_rows = [generate_cardevent()]


errors = client.insert_rows_json(table_id, generate_cardevent())

if errors == []:
    print("Dados inseridos com sucesso.")
else:
    print(f"Erros ao inserir dados: {errors}")
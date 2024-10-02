import os

# from auth import client
from main import client

schema_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schemas.py')

card_table_id = client.get_table(str(input("Insira o ID do seu Dataset e de sua tabela no formato 'dataset_id.table_id' : ")))

unformat_card_table_schema = card_table_id.schema

# print("Schema sem a formatação correta: \n")
# print(unformat_card_table_schema)

formated_card_schema = {field.name: field.field_type for field in unformat_card_table_schema}
# print("\nSchema com a formatação correta: \n")
# print(formated_card_schema)

card_schema = "card_schema = "
with open(schema_file_path, 'a') as file:
    file.write(card_schema + str(formated_card_schema))
    print("Schema importado com sucesso!")

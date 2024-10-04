import os
from google.cloud import bigquery
import json 

# Inicializa o cliente do BigQuery
client = bigquery.Client()

# Solicita o ID do dataset e tabela no formato correto
card_table_id = client.get_table(str(input("Insira o ID do seu Dataset e de sua tabela no formato 'dataset_id.table_id' : ")))

# Obtém o schema sem formatação
unformat_card_table_schema = card_table_id.schema

print("Schema sem a formatação correta: \n")
print(unformat_card_table_schema)

# Formata o schema em um dicionário {campo: tipo}
formated_card_schema = {field.name: field.field_type for field in unformat_card_table_schema}
print("\nSchema com a formatação correta: \n")
print(formated_card_schema)

# Cria o diretório 'bq_schemas/' se ele ainda não existir
schema_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bq_schemas')
os.makedirs(schema_dir, exist_ok=True)

# Gera um nome de arquivo baseado no ID da tabela (substitui '.' por '_')
schema_file_name = card_table_id.table_id.replace('.', '_') + '.json'
schema_file_path = os.path.join(schema_dir, schema_file_name)

# Conteúdo a ser escrito no arquivo
card_schema = json.dumps(formated_card_schema)

# Escreve o schema formatado em um arquivo dentro de 'bq_schemas/'
with open(schema_file_path, 'w') as file:
    file.write(card_schema)
    print(f"Schema importado com sucesso em: {schema_file_path}")

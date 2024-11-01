from utils import jsonl_to_bigquery

# client = get_bigquery_client()
directory = './bq_schemas'

# create_tables()
# - Criar dataset e tabelas
# ...
# - Enviar dados via jsonl
jsonl_to_bigquery(filename='cobranca_campo_customizavel_faker.jsonl', table_id='cobranca_campo_customizavel', dataset_id='pfs_risco_tivea')
# ...

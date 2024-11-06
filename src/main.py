from utils import jsonl_to_bigquery

# client = get_bigquery_client()
directory = './bq_schemas'

# create_tables()
# - Criar dataset e tabelas
# ...
# - Enviar dados via jsonl
jsonl_to_bigquery(filename='cliente.jsonl', table_id='cliente', dataset_id='pfs_risco_raw_tivea')
# ...

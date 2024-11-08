from utils import jsonl_to_bigquery,run_command

# create_tables()

jsonl_to_bigquery(filename='acordo.jsonl', table_id='acordo', dataset_id='pfs_risco_raw_tivea')
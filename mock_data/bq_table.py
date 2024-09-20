from config import settings
from google.cloud import bigquery
from schemas import card_schema

client = bigquery.Client()

dataset_id = settings.DATASET_ID
table_id = settings.TABLE_ID

# Create card table
card_table = bigquery.Table(table_id, schema=card_schema)
card_table = client.create_table(card_table)
print(f'Table {card_table.table_id} created successfully.')

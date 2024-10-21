from google.cloud import bigquery
from config import PROJECT_ID
from utils import create_bigquery_schemas,create_dataset_and_tables,create_pydantic_models

client = bigquery.Client(PROJECT_ID)

directory = './bq_schemas'

create_dataset_and_tables()
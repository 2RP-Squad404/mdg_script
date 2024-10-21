from utils import create_bigquery_schemas, create_pydantic_models

directory = './bq_schemas'
create_bigquery_schemas(directory)
create_pydantic_models(directory)
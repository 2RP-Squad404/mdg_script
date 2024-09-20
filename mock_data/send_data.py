from datagen import generate_account
from google.cloud import bigquery
from config import settings


project_id = settings.PROJECT_ID
dataset_id = settings.DATASET_ID
table_id = settings.TABLE_ID

client = bigquery.Client(project=project_id)


account_mock_data = [generate_account()]


table_ref = client.dataset(dataset_id).table(table_id)


errors = client.insert_rows_json(table_ref, account_mock_data)


if errors == []:
    print("sucess send")
else:
    print(f"Errors: {errors}")

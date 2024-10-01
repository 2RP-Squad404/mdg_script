import json
from google.cloud import bigquery, secretmanager
from google.oauth2 import service_account

# Primeira tentativa de autenticação com Secret Manager: 

secret_id = "bq-credential"
project_id = "big-maxim-430019-g7"

secret_client = secretmanager.SecretManagerServiceClient()

secret_name = "projects/222448658386/secrets/bq-credential/versions/latest"
response = secret_client.access_secret_version(name=secret_name)

secret_payload = response.payload.data.decode("UTF-8")
credentials_info = json.loads(secret_payload)

credentials = service_account.Credentials.from_service_account_info(credentials_info)
client = bigquery.Client(credentials=credentials, project=project_id)


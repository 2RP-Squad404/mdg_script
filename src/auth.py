import json
import logging


from google.cloud import bigquery, secretmanager
from google.oauth2 import service_account

from config import PROJECT_ID, SECRET_NAME, setup_logging

setup_logging(log_level=logging.INFO)


def get_secret(secret_name, project_id):
    """
    Busca um segredo específico no Secret Manager do Google Cloud
    usando a autenticação do CLI.
    """
    try:
        logging.info("Acessando o Secret Manager")


        client = secretmanager.SecretManagerServiceClient(client_options={"quota_project_id": project_id})


        name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": name})
        secret_string = response.payload.data.decode("UTF-8")
        return json.loads(secret_string)


    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")
        return None


def get_bigquery_client():
    """
    Autentica no BigQuery usando as credenciais armazenadas no Secret Manager.

    Essa função pega as credenciais do Secret Manager e retorna um cliente BigQuery
    autenticado com essas credenciais.
    """
    try:
        credentials_info = get_secret(SECRET_NAME, PROJECT_ID)
        if credentials_info is None:
            raise Exception("Credenciais não encontradas no Secret Manager.")

        credentials = service_account.Credentials.from_service_account_info(credentials_info)

        logging.info("Conta de serviço autenticada.")
        return bigquery.Client(credentials=credentials, project=PROJECT_ID)
    except Exception as e:
        logging.error(f"Ocorreu um erro: {e}")
        return None

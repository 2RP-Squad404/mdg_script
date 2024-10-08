from google.cloud import secretmanager, bigquery
from google.oauth2 import service_account
import json
from config import PROJECT_ID, SECRET_NAME

# Função para buscar o segredo no Secret Manager
def get_secret(secret_name, project_id):
    try:
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": name})
        secret_string = response.payload.data.decode("UTF-8")
        return json.loads(secret_string)
    except Exception as e:
        print(f"Erro ao buscar o segredo do Secret Manager: {e}")
        return None

# Função para autenticar no BigQuery usando as credenciais do Secret Manager
def get_bigquery_client():
    try:
        # Busca as credenciais do Secret Manager
        credentials_info = get_secret(SECRET_NAME, PROJECT_ID)
        if credentials_info is None:
            raise Exception("Credenciais não encontradas no Secret Manager.")
        
        # Cria as credenciais com as informações recuperadas
        credentials = service_account.Credentials.from_service_account_info(credentials_info)
        
        # Retorna o cliente do BigQuery autenticado
        return bigquery.Client(credentials=credentials, project=PROJECT_ID)
    except Exception as e:
        print(f"Erro ao autenticar no BigQuery: {e}")
        return None

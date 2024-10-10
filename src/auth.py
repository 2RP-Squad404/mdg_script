from google.cloud import secretmanager, bigquery
from google.oauth2 import service_account
import json
from config import PROJECT_ID, SECRET_NAME

def get_secret(secret_name, project_id):
    """
    Busca um segredo específico no Secret Manager do Google Cloud
    usando a autenticação do CLI.
    """
    try:
        # O cliente aqui vai usar as credenciais da conta de CLI autenticada
        print("Usando a conta autenticada via CLI para acessar o Secret Manager.")
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": name})
        secret_string = response.payload.data.decode("UTF-8")
        return json.loads(secret_string)
    except Exception as e:
        print(f"Erro ao buscar o segredo do Secret Manager: {e}")
        return None

def get_bigquery_client():
    """
    Autentica no BigQuery usando as credenciais armazenadas no Secret Manager.

    Essa função pega as credenciais do Secret Manager e retorna um cliente BigQuery
    autenticado com essas credenciais.
    """
    try:
        # Pega as credenciais do Secret Manager usando a conta do CLI
        credentials_info = get_secret(SECRET_NAME, PROJECT_ID)
        if credentials_info is None:
            raise Exception("Credenciais não encontradas no Secret Manager.")
        
        # Gera as credenciais da conta de serviço com base no segredo obtido
        credentials = service_account.Credentials.from_service_account_info(credentials_info)
        
        # Retorna o cliente do BigQuery autenticado com a conta de serviço
        print("Usando a conta de serviço para autenticar no BigQuery.")
        return bigquery.Client(credentials=credentials, project=PROJECT_ID)
    except Exception as e:
        print(f"Erro ao autenticar no BigQuery: {e}")
        return None

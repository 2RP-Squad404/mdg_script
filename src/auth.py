from google.cloud import secretmanager, bigquery
from google.oauth2 import service_account
import json
from config import PROJECT_ID, SECRET_NAME

def get_secret(secret_name, project_id):

    """
    Busca um segredo específico no Secret Manager do Google Cloud.

    Esta função acessa o Secret Manager, utilizando o nome do segredo e o ID do projeto,
    e retorna o valor do segredo como um dicionário JSON.

    Parâmetros:
        secret_name (str): O nome do segredo a ser recuperado.
        project_id (str): O ID do projeto do Google Cloud.

    Retorna:
        dict: O segredo decodificado como um dicionário JSON, se encontrado.
        None: Se houver um erro durante a recuperação do segredo.

    Exceções:
        Exception: Qualquer erro durante o acesso ao Secret Manager será tratado e 
        uma mensagem de erro será exibida no console.
    """

    try:
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

    Esta função obtém as credenciais do Secret Manager, cria um objeto de credenciais
    e retorna um cliente autenticado do BigQuery.

    Retorna:
        bigquery.Client: Um cliente autenticado para interagir com o BigQuery.
        None: Se houver um erro ao buscar as credenciais ou ao criar o cliente.

    Exceções:
        Exception: Qualquer erro durante a autenticação ou criação do cliente será
        tratado e uma mensagem de erro será exibida no console.
    """
    
    try:
        credentials_info = get_secret(SECRET_NAME, PROJECT_ID)
        if credentials_info is None:
            raise Exception("Credenciais não encontradas no Secret Manager.")
        
        credentials = service_account.Credentials.from_service_account_info(credentials_info)
        
        # Retorna o cliente do BigQuery autenticado
        return bigquery.Client(credentials=credentials, project=PROJECT_ID)
    except Exception as e:
        print(f"Erro ao autenticar no BigQuery: {e}")
        return None

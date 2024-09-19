from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Classe Settings armazena as configurações globais da API com valores padrões.
    
    Atributos:
    - API_TITLE (str): Título da API exibido na documentação
    - API_VERSION (str): Versão da API
    - API_HOST (str): Endereço da API
    - API_PORT (int): Porta da API
    - API_DESCRIPTION (str): Breve descrição da API
    """
    API_TITLE: str
    API_VERSION: str
    API_HOST: str
    API_PORT: int
    API_DESCRIPTION: str


settings = Settings(
    API_TITLE="Mock-Data App",
    API_VERSION="v1.0.0",
    API_HOST="localhost",
    API_PORT=8001,
    API_DESCRIPTION="Esta aplicação gera e dispara eventos com dados mockados para serem usados na pipeline analítica BigQuery/Dataform"
)

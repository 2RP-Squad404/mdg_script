import logging
import logging.config
import os

config_path = os.path.join(os.path.dirname(__file__), 'logging.ini')
logging.config.fileConfig(config_path)
logger = logging.getLogger('appLogger')


from pydantic_settings import BaseSettings

"""
    Classe Settings para gerenciar a configuração do projeto usando variáveis de ambiente.

    Esta classe utiliza o BaseSettings do Pydantic para ler e analisar automaticamente
    as variáveis de ambiente de um arquivo `.env`, mapeando-as para atributos de fácil acesso.

    Atributos:
        project_id (str): O ID do projeto no Google Cloud.
        secret_name (str): O nome do segredo armazenado no Secret Manager.

    Config:
        env_file (str): Caminho para o arquivo de ambiente, que pode ser "../.env" ou ".env".
        extra (str): Define que qualquer variável de ambiente adicional deve ser ignorada.
"""


class Settings(BaseSettings):
    project_id: str
    secret_name: str

    class Config:
        env_file = ["../.env", ".env"]
        extra = "ignore"


settings = Settings()

PROJECT_ID = settings.project_id
SECRET_NAME = settings.secret_name

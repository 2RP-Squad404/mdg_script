import logging
import logging.config

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
        env_file = "../.env"
        extra = "ignore"


settings = Settings()

PROJECT_ID = settings.project_id
SECRET_NAME = settings.secret_name


def setup_logging(log_level=logging.INFO):
    """Configura o logging com um formato padrão no console.

    Args:
        log_level: Nível de log (ex: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL).
    """
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(levelname)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': log_level,
                'formatter': 'standard',
            },
        },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': log_level,
                'propagate': False
            }
        }
    }

    logging.config.dictConfig(logging_config)

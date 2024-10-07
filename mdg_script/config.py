from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_id: str
    secret_name: str

    class Config:
        env_file = "../.env" or ".env"
        extra = "ignore"


settings = Settings()

PROJECT_ID=settings.project_id
SECRET_NAME=settings.secret_name
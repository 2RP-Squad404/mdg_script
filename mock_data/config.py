from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_ID: str
    DATASET_ID: str
    TABLE_ID: str


settings = Settings(


    PROJECT_ID='big-maxim-430019-g7',
    DATASET_ID='mockdatadataset',
    TABLE_ID='account'
)

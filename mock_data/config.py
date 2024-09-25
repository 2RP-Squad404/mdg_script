from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_ID: str
    PFS_UNIFICACAO_PEFISA_DATASET_ID: str
    MOCK_CARD_TABLE_ID: str


settings = Settings(
    PROJECT_ID='big-maxim-430019-g7',
    PFS_UNIFICACAO_PEFISA_DATASET_ID='mock_pfs_unificacao_pefisa',
    MOCK_CARD_TABLE_ID='mock_cartao'
)

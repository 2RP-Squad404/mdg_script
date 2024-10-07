from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    !Atenção: Esta classe esta projetada para um ambiente de teste, haverá mudanças 
    quando esta aplicação estiver em ambiente de produção. 
    
    Classe Settings é uma classe que armazena os valores de configuração da aplicação.
    
    Atributos:
    
        PROJECT_ID (str): O ID do projeto GCP onde os recursos estão localizados.
        
        PFS_UNIFICACAO_PEFISA_DATASET_ID (str): O ID do dataset no BigQuery que está sendo utilizado nos testes
        em desenvolvimento.
        
        MOCK_CARD_TABLE_ID (str): O ID de uma das tabelas de teste para armazenar dados mockados
            de cartões no BigQuery.
    """
    PROJECT_ID: str
    PFS_UNIFICACAO_PEFISA_DATASET_ID: str
    MOCK_CARD_TABLE_ID: str


settings = Settings(
    PROJECT_ID='big-maxim-430019-g7',  # Service Account usada para teste em desenvolvimento
    PFS_UNIFICACAO_PEFISA_DATASET_ID='mock_pfs_unificacao_pefisa',  # dataset usado para testes em desenvolvimento
    MOCK_CARD_TABLE_ID='mock_cartao'  # tabela usada para testes em desenvolvimento
)

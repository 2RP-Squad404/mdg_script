import sys
from pathlib import Path

from config import PROJECT_ID, SECRET_NAME, logger
from gemini_interface import run_gemini
from generate_models import create_pydantic_models,create_bigquery_schemas
from utils import (
    create_tables,
    display_common_datasets,
    jsonl_data,
    run_command,
    send_jsonl_to_bigquery,
)

def cli_option():
    bq_schemas_path = Path(__file__).resolve().parent / 'bq_schemas'
    mock_data_path = Path(__file__).resolve().parent / 'mock_data'

    create_pydantic_models(str(bq_schemas_path))
    create_bigquery_schemas(str(bq_schemas_path))

    logger.info('Funções possiveis:')
    logger.info('1 - Criar tabelas por dataset no BigQuery')
    logger.info('2 - Gerar funções Faker com Gemini')
    logger.info('3 - Gerar dados em JSONL')
    logger.info('4 - Enviar JSONL para o BigQuery')

    input_user = input('Escolha uma opção: ')

    match input_user:
        case '1':
            select_dataset = display_common_datasets(folder_path= str(bq_schemas_path))
            create_tables(select_dataset)
        case '2':
            select_dataset = display_common_datasets(folder_path= str(bq_schemas_path))
            run_gemini(
                project_id=PROJECT_ID,
                model_name='gemini-1.5-flash-002',
                dataset=select_dataset,
            )
        case '3':
            select_dataset = display_common_datasets(folder_path= str(bq_schemas_path))
            data = run_command(f'python {select_dataset}.py')
            jsonl_data(data)
        case '4':
            select_dataset = display_common_datasets(folder_path= str(mock_data_path))
            send_jsonl_to_bigquery(select_dataset)


def run_cli():
    logger.info(
        '\033[33mIdentifying active Google Cloud CLI authentication...\033[0m'
    )

    project_id = PROJECT_ID

    if not project_id:
        logger.info('\033[91mPROJECT ID: None\033[0m\n')
        sys.exit(1)
    logger.info(f'\033[32mPROJECT ID: {project_id}\033[0m\n')

    secret_name = SECRET_NAME

    if not secret_name:
        logger.info('\033[91mSECRET NAME: None\033[0m\n')
        sys.exit(1)
    logger.info(f'\033[32mSECRET NAME: {secret_name}\033[0m\n')

    logger.info('\033[33mAutenticating with Secret manager...\033[0m')

    cli_option()


run_cli()

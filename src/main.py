
import sys

from config import PROJECT_ID, SECRET_NAME, logger
from utils import display_common_datasets, create_tables, run_command, jsonl_data, send_jsonl_to_bigquery
from generate_models import create_pydantic_models
from gemini_interface import run_gemini

def cli_option():
    create_pydantic_models('./bq_schemas')
    
    logger.info("Funções possiveis:")
    logger.info("1 - Criar tabelas por dataset no BigQuery")
    logger.info("2 - Gerar funções Faker com Gemini")
    logger.info("3 - Gerar dados em JSONL")
    logger.info("4 - Enviar JSONL para o BigQuery")

    input_user = input("Escolha uma opção: ")

    match(input_user):
        case "1":
            select_dataset = display_common_datasets(folder_path='bq_schemas')
            create_tables(select_dataset)
        case "2":
            select_dataset = display_common_datasets(folder_path='bq_schemas')
            run_gemini(project_id=PROJECT_ID, model_name="gemini-1.5-flash-002",dataset=select_dataset)
        case "3":
            select_dataset = display_common_datasets(folder_path='bq_schemas')
            data = run_command(f'python {select_dataset}.py')
            jsonl_data(data)
        case "4":
            select_dataset = display_common_datasets(folder_path='mock_data')
            send_jsonl_to_bigquery(select_dataset)

def run_cli():
    logger.info(
        '\033[33mIdentifying active Google Cloud CLI authentication...\033[0m')

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
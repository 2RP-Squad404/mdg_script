import json
import sys
import time
from pathlib import Path

from config import PROJECT_ID, SECRET_NAME, logger
from gemini_interface import (
    generate_full_prompt,
    generate_functions_with_gemini,
)
from generate_models import create_bigquery_schemas, create_pydantic_models
from utils import (
    create_tables,
    display_common_datasets,
    run_command,
    send_jsonl_to_bigquery,
)

PERSISTENCE_FILE = "select_dataset.json"


def save_persistent_data(data):
    """Save persistent data to a file."""
    with open(f'src/{PERSISTENCE_FILE}', "w") as f:
        json.dump(data, f)


def load_persistent_data():
    """Load persistent data from a file."""
    try:
        with open(f'src/{PERSISTENCE_FILE}', "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def cli_option():

    persistent_data = load_persistent_data()

    select_dataset_to_generate_functions = persistent_data.get("select_dataset_to_generate_functions")

    bq_schemas_path = Path(__file__).resolve().parent / 'bq_schemas'

    logger.info('Funções possiveis:')
    logger.info('1 - Criar tabelas por dataset no BigQuery')
    logger.info('2 - Gerar o prompt completo para o Gemini')
    logger.info('3 - Gerar funções Faker com Gemini')
    logger.info('4 - Gerar dados em JSONL')
    logger.info('5 - Enviar JSONL para o BigQuery')
    logger.info('6 - Sair da aplicação')

    input_user = input('Escolha uma opção: ')

    if (input_user != '3'):
        select_dataset = display_common_datasets(folder_path=str(bq_schemas_path))

    match input_user:
        case '1':
            start_time = time.time()
            create_tables(select_dataset)
            end_time = time.time()

            process_time = end_time - start_time
            logger.info(f"\033[32mTempo de criação de tabelas: {process_time:.2f}segundos\033[0m\n")
            cli_option()

        case '2':
            generate_full_prompt(select_dataset)
            select_dataset_to_generate_functions = select_dataset
            save_persistent_data({"select_dataset_to_generate_functions": select_dataset_to_generate_functions})
        case '3':
            with open('src/full_prompt_output.txt', 'r') as arquivo:
              full_prompt = arquivo.read()

            if (select_dataset_to_generate_functions):
                logger.info(f'\033[32mDATASET: {select_dataset_to_generate_functions}\033[0m\n')
            else:
                logger.info('\033[91mDATASET: None\033[0m\n')
                return

            generate_functions_with_gemini(
                project_id=PROJECT_ID,
                model_name='gemini-1.5-flash-002',
                dataset=select_dataset_to_generate_functions,
                full_prompt=full_prompt
            )

            cli_option()

        case '4':
            logger.info("Escreve o número de linhas")

            start_time = time.time()
            run_command(f'python datagen/{select_dataset}.py')
            end_time = time.time()

            process_time = end_time - start_time
            logger.info(f"\033[32mTempo de geração de dados: {process_time:.2f}segundos\033[0m\n")
            cli_option()

        case '5':
            start_time = time.time()
            send_jsonl_to_bigquery(select_dataset)
            end_time = time.time()

            process_time = end_time - start_time
            logger.info(f"\033[32mTempo de envio dos dados: {process_time:.2f}segundos\033[0m\n")
            cli_option()

        case '6':
            logger.info("\033[32mAplicação finalizada\033[0m\n")


def run_cli():
    logger.info('\033[33mIdentifying active Google Cloud CLI authentication...\033[0m')

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

    bq_schemas_path = Path(__file__).resolve().parent / 'bq_schemas'

    create_pydantic_models(str(bq_schemas_path))
    create_bigquery_schemas(str(bq_schemas_path))

    cli_option()


run_cli()

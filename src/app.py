import os
import sys

from config import PROJECT_ID, SECRET_NAME, logger
from utils import display_common_datasets,create_tables,jsonl_to_bigquery,input_num_linhas,commom_tables,send_jsonl_to_bigquery
from datagen.pfs_risco_tivea import function_pfs_risco_tivea
from datagen.pfs_risco_raw_tivea import function_pfs_risco_raw_tivea

def show_cli():
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

    select_dataset = display_common_datasets(folder_path="datagen")

    num_linhas = input_num_linhas()

    # create_tables()

    match str(select_dataset[0]):

        case "pfs_risco_raw_tivea":
            function_pfs_risco_raw_tivea(num_linhas)

        case "pfs_risco_tivea":
            function_pfs_risco_tivea(num_linhas)

    dataset = select_dataset[0]

    # commom_tables(select_dataset[0])

    send_jsonl_to_bigquery(dataset)
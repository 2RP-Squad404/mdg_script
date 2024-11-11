import os
import sys

from config import PROJECT_ID, SECRET_NAME, logger
from utils import display_common_datasets,create_tables,jsonl_to_bigquery
from datagen import pfs_raw_conductor,pfs_risco_raw_tivea,pfs_risco_tivea

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

    select_dataset = display_common_datasets(folder_path="datagen",project_id=PROJECT_ID)

    num_linhas = logger.info(int("Quantas linhas deseja gerar?"))

    create_tables()

    match str(select_dataset[0]):
        case "pfs_risco_raw_tivea":
            pfs_risco_raw_tivea(num_linhas)
        case "pfs_risco_tivea":
            pfs_risco_tivea(num_linhas)

    for filename in os.listdir("datagen"):
        if filename.endswith(".jsonl"):
            table_id = os.path.splitext(filename)[0]
            jsonl_to_bigquery(filename=f"datagen/{filename}", table_id=table_id, dataset_id=select_dataset[0])
            logger.info(f'\033[32mArquivo {filename} enviado para a tabela {table_id} no dataset {select_dataset[0]}\033[0m')


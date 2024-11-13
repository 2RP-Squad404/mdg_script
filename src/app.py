import os
import sys

from config import PROJECT_ID, SECRET_NAME, logger
from utils import cli_option

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
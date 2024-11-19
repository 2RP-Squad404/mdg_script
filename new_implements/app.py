import sys

from utils_new import (
    gcloud_choose,
    gen_py_models,
    generate_code_with_gemini,
    get_bq_schemas_json,
    get_credentials,
    init_gemini,
    load_models_and_examples,
    prompt,
    run_command,
    save_code_from_gemini,
)

from config import logger

logger.info(
    '\033[33mIdentifying active Google Cloud CLI authentication...\033[0m'
)

gcloud_auth = run_command(
    "gcloud auth list --filter=status:ACTIVE --format='value(account)'"
)

if not gcloud_auth:
    logger.info('\033[31mNo active accounts found :(\033[0m')
    logger.info(
        '\033[0mFirst, log in using the command: \033[32mgcloud auth login\033[0m\n'
    )
    logger.info(
        '\033[0mAfter, log in using the command: \033[32mgcloud auth application-default login\033[0m\n'
    )
    sys.exit(1)

logger.info(f'\033[32mGOOGLE CLOUD AUTH: {gcloud_auth}\033[0m\n')

project_id = gcloud_choose(resource_type='projects')
if not project_id:
    logger.info('\033[91mPROJECT ID: None\033[0m\n')
    sys.exit(1)
logger.info(f'\033[32mPROJECT ID: {project_id}\033[0m\n')

secret_name = gcloud_choose(resource_type='secrets', project_id=project_id)
if not secret_name:
    logger.info('\033[91mSECRET NAME: None\033[0m\n')
    sys.exit(1)
logger.info(f'\033[32mSECRET NAME: {secret_name}\033[0m\n')

logger.info('\033[33mAutenticating with Secret manager...\033[0m')

credentials, credentials_dict = get_credentials(
    f'projects/{project_id}/secrets/{secret_name}/versions/1'
)

client_email = credentials_dict.get('client_email')
logger.info(f'\033[32mSERVICE ACCOUNT: {client_email}\033[0m\n')

dataset = gcloud_choose(
    resource_type='datasets', project_id=project_id, credentials=credentials
)
if not dataset:
    logger.info('\033[91mDATASET: None\033[0m\n')
    sys.exit(1)
logger.info(f'\033[32mDATASET: {dataset}\033[0m\n')

logger.info('\033[33mGetting BigQuery Json Schemas...\033[0m')

bq_schema_json = get_bq_schemas_json(
    project_id=project_id, credentials=credentials, dataset=dataset
)
if bq_schema_json:
    logger.info('\033[32mBQ SCHEMAS JSON: Obtained successfully.\033[0m\n')
else:
    logger.info(
        '\033[91mBQ SCHEMAS JSON: None or could not be retrieved.\033[0m'
    )
    sys.exit(1)

logger.info('\033[33mGenerating PY MODELS from BQ SCHEMAS JSON...\033[0m')

py_models = gen_py_models(dataset=dataset)
if py_models:
    logger.info('\033[32mPY MODELS: Generated successfully.\033[0m\n')
else:
    logger.info('\033[91mPY MODELS: None or could not be retrieved.\033[0m')
    sys.exit(1)

run_command('task format')

logger.info('\033[33mGenerating GEMINI CODE for Data Generator...\033[0m')

gemini_model = init_gemini(project_id=project_id, credentials=credentials)
code = generate_code_with_gemini(
    gemini_model, load_models_and_examples(dataset, prompt)
)

gemini_code = save_code_from_gemini(dataset=dataset, content=code)
if gemini_code:
    logger.info('\033[32mGEMINI CODE: Generated successfully.\033[0m\n')
else:
    logger.info('\033[91mGEMINI CODE: None or could not be retrieved.\033[0m')
    sys.exit(1)

run_command('task format')
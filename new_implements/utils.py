import glob
import json
import os
import re
import subprocess
from typing import List

from google.cloud import aiplatform, bigquery, secretmanager
from google.oauth2 import service_account
from vertexai.preview.generative_models import GenerativeModel

from config import logger


def run_command(command: str) -> str:
    """Execute a gcloud command and return the output.

    Args:
        command (str): The gcloud command to be executed.

    Returns:
        str: The standard output from the command execution.
    """
    result = subprocess.run(
        command, capture_output=True, text=True, shell=True, check=False
    )
    return result.stdout.strip()


def gcloud_list(
    resource_type: str, project_id: str, credentials: str, dataset_id: str
) -> list:
    """List various resources from Google Cloud based on the specified type.

    Args:
        resource_type (str): The type of resource to list. Options are:
            'projects', 'secrets', 'datasets', 'tables'.
        project_id (str): The project ID used for resource queries.
        credentials (str): Credentials for accessing BigQuery.
        dataset_id (str): The dataset ID, required for listing tables.

    Returns:
        list: A list of resource identifiers (e.g., project IDs, secret names,
        dataset IDs, or table IDs) based on the specified resource type.

    Raises:
        ValueError: If an unknown resource type is provided.
    """
    if resource_type == 'projects':
        command = "gcloud projects list --format='value(projectId)'"
    elif resource_type == 'secrets':
        command = f"gcloud secrets list --project={project_id} --format='value(name)'"
    elif resource_type in {'datasets', 'tables'}:
        client = bigquery.Client(credentials=credentials, project=project_id)
        if resource_type == 'datasets':
            datasets = client.list_datasets(project_id)
            return [dataset.dataset_id for dataset in datasets]
        elif resource_type == 'tables':
            tables = client.list_tables(dataset_id)
            return [table.table_id for table in tables]
    else:
        raise ValueError(f'Unknown resource type: {resource_type}')

    return run_command(command).splitlines()


def gcloud_choose(
    resource_type: str,
    project_id: str = None,
    credentials: str = None,
    dataset_id: str = None,
) -> str:
    """Prompt the user to choose a resource from a list.

    Args:
        resource_type (str): The type of resource to list and choose from.
        project_id (str, optional): The project ID used for resource queries.
        credentials (str, optional): Credentials for accessing BigQuery.
        dataset_id (str, optional): The dataset ID, required for listing tables.

    Returns:
        str: The chosen resource identifier, or None if no valid choice is made.

    Raises:
        ValueError: If an unknown resource type is provided.
    """
    choices = gcloud_list(
        resource_type=resource_type,
        project_id=project_id,
        credentials=credentials,
        dataset_id=dataset_id,
    )

    if not choices:
        return None

    logger.info(f'\033[33mAvailable {resource_type}:\033[0m')
    for i, choice in enumerate(choices, start=1):
        logger.info(f'{i}. {choice}')

    choice_index = int(input('> Enter the option number: ')) - 1
    if 0 <= choice_index < len(choices):
        return choices[choice_index]
    else:
        return None


def get_credentials(secret_name: str):
    """Retrieve service account credentials from Google Cloud Secret Manager.

    Args:
        secret_name (str): The full resource name of the secret version.

    Returns:
        tuple: A tuple containing the credentials object and the credentials dictionary.
    """
    secret_client = secretmanager.SecretManagerServiceClient()
    response = secret_client.access_secret_version(name=secret_name)
    credentials_dict = json.loads(response.payload.data.decode('utf-8'))

    credentials = service_account.Credentials.from_service_account_info(
        credentials_dict
    )
    return credentials, credentials_dict


def get_bq_schemas_json(
    project_id: str, credentials: str, dataset: str
) -> bool:
    """Get the schemas of all tables in the specified dataset and store them in JSON files."""

    client = bigquery.Client(credentials=credentials, project=project_id)
    tables = client.list_tables(dataset)

    output_dir = f'src/bq_schemas_json/{dataset}'
    os.makedirs(output_dir, exist_ok=True)

    for table in tables:
        table_name = table.table_id
        output_file = os.path.join(output_dir, f'{table_name}.json')

        table_ref = client.get_table(table)
        schema = []

        for field in table_ref.schema:
            field_info = {
                'name': field.name,
                'mode': field.mode,
                'type': field.field_type,
                'description': field.description or '',
                'fields': [],
            }
            if field.field_type == 'RECORD' and field.fields:
                field_info['fields'] = [
                    {
                        'name': subfield.name,
                        'mode': subfield.mode,
                        'type': subfield.field_type,
                        'description': subfield.description or '',
                    }
                    for subfield in field.fields
                ]

            schema.append(field_info)

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)

    return True


def gen_py_models(dataset: str):
    output_dir = f'src/py_models/{dataset}'
    os.makedirs(output_dir, exist_ok=True)

    # Carregar os esquemas do BigQuery do diretório correspondente
    schema_dir = f'src/bq_schemas_json/{dataset}'
    for filename in os.listdir(schema_dir):
        if filename.endswith('.json'):
            with open(
                os.path.join(schema_dir, filename), 'r', encoding='utf-8'
            ) as f:
                schema = json.load(f)
                class_name = filename.replace(
                    '.json', ''
                ).capitalize()  # Nome da classe
                model_code = generate_model_code(class_name, schema)

                # Escrever o código do modelo em um arquivo
                with open(
                    os.path.join(output_dir, f'{class_name}.py'),
                    'w',
                    encoding='utf-8',
                ) as model_file:
                    model_file.write(model_code)
    return True


def generate_model_code(class_name: str, schema: List[dict]) -> str:
    """Gera o código da classe Pydantic a partir do schema."""
    fields = []
    for field in schema:
        field_type = map_field_type(field['type'])
        field_name = field['name']
        is_optional = field['mode'] == 'NULLABLE'

        if is_optional:
            field_type = f'Optional[{field_type}]'

        fields.append(
            f"    {field_name}: {field_type}  # {field['description']}"
        )

    return f"""from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional

class {class_name}(BaseModel):
{os.linesep.join(fields)}
"""


def map_field_type(bq_type: str) -> str:
    """Mapeia tipos do BigQuery para tipos do Pydantic."""
    mapping = {
        'STRING': 'str',
        'INTEGER': 'int',
        'FLOAT': 'float',
        'BOOLEAN': 'bool',
        'TIMESTAMP': 'datetime',
        'DATE': 'date',
        'DATETIME': 'datetime',
        'RECORD': 'dict',  # Para subcampos de RECORD, mais complexidade seria necessária
        'NUMERIC': 'float',  # Para subcampos de RECORD, mais complexidade seria necessária
        'ANY': 'Any',  # Para subcampos de RECORD, mais complexidade seria necessária
    }

    return mapping.get(bq_type, 'Any')


def init_gemini(project_id: str, credentials: str):
    """
    Inicia a comunicação com Gemini API.

    Parâmetros:
    project_id (str): Id do projeto GCP.
    model_name (str): O nome do modelo do Vertex IA que será usado.
    """
    aiplatform.init(project=project_id, credentials=credentials)
    return GenerativeModel('gemini-1.5-flash-002')


def generate_code_with_gemini(model, prompt: str):
    """
    Envia o prompt para o modelo e retorna o código de resposta.

    Parâmetros:
    model (GenerativeModel): Modelo que será usado.
    prompt (str): Texto do prompt que será enviado ao modelo.
    """
    response = model.generate_content(prompt)
    return response.text


def save_code_from_gemini(dataset: str, content: str):
    """
    Escreve a resposta obtida do modelo no arquivo 'gemini_datagen.py'.

    Parâmetros:
    content (str): O código obtido do modelo.
    """
    # Remover qualquer marcação de código extra (como ``` ou ```python) no início e final
    content = re.sub(
        r'^```(python)?\s*', '', content
    )  # Remover ```python ou apenas ```
    content = re.sub(r'```$', '', content)  # Remover ```

    # Define o diretório e o caminho do arquivo
    pathdir = 'src/gm_functions'
    os.makedirs(pathdir, exist_ok=True)  # Cria o diretório se não existir

    # Define o caminho do arquivo
    file_path = os.path.join(pathdir, f'{dataset}.py')

    # Abre o arquivo para escrita
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)  # Escreve o conteúdo diretamente

    return True


def load_models_and_examples(dataset: str, prompt) -> str:
    # Carregar modelos Pydantic
    models_dir = f'src/py_models/{dataset}'
    models_code = []

    for filename in os.listdir(models_dir):
        if filename.endswith('.py'):
            with open(
                os.path.join(models_dir, filename), 'r', encoding='utf-8'
            ) as f:
                models_code.append(f.read())

    models_code_str = '\n\n'.join(models_code)

    # Carregar todos os exemplos JSON do diretório
    json_files_pattern = f'src/data_sample_json/{dataset}/*.json'
    json_file_paths = glob.glob(json_files_pattern)
    examples_data = []

    for json_file_path in json_file_paths:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            examples_data.append(json.load(f))

    # Converter todos os dados JSON em uma string
    examples_data_str = json.dumps(examples_data, indent=2, ensure_ascii=False)

    # Carregar exemplo de retorno esperado (agora com o caminho fixo 'example.py')
    expected_return_file = 'src/example_of_expected_return/example.py'
    with open(expected_return_file, 'r', encoding='utf-8') as f:
        expected_return_code = f.read()

    # Concatenar tudo
    full_prompt = prompt.replace(
        '#colocar nessa linha os modelos do py_models/{dataset}/*.py',
        models_code_str,
    )
    full_prompt = full_prompt.replace(
        '#colocar nessa linha o json com os dados de exemplo do data_sample_json/{dataset}/*.json',
        examples_data_str,
    )
    full_prompt = full_prompt.replace(
        '#colocar nessa linha algum py com um exemplo de retorno esperado do example_of_expected_return/{dataset}.py',
        expected_return_code,
    )

    return full_prompt


prompt = """Você é um assistente especializado em gerar código Python de alta qualidade e aderente às melhores práticas. Você segue as instruções com precisão, sem fornecer explicações ou informações extras além do código solicitado.

Exemplo generico de como deve ser as funções que você irá gerar:

Observação 1: se algum atributo for id você deve preencher com:
next(id_serial).

Observação 2: se algum atributo for data ou coisa do tipo você deve preencher as datas com a seguinte formatação:
strftime('%Y-%m-%d %H:%M:%S')

Observação 3: Em nenhuma hipotese, use acentos em palavras, escreva sem o acento mesmo.

Observação 4: Colunas que nao tiverem amostras de dados no exemplo,  você deve criar uma função fake correspondente para cada uma delas tomando como base o tipo e o nome da coluna.

def criar_<nome_do_modelo>_faker():
    id_serial = itertools.count(start=0)
    return {{
        "id": next(id_serial),
        "nome_do_atributo": função_fake_correspondente,
    }}
Dado o seguinte modelo Pydantic, crie uma função Python que instancia um objeto estritamente deste modelo e preencha os atributos com valores gerados por funções adequadas da biblioteca Faker. A função deve retornar o objeto como um dicionário. Use as funções Faker que melhor correspondem a cada tipo de dado. Retorne apenas a função Python, sem explicações adicionais, importações de bibliotecas, tratamento de exceções, apenas a implementação da função.
para criar a função para o model abaixo, utilize do mapping que estou enviando:


utilize exatamente este modelo Pydantic:
#colocar nessa linha os modelos do py_models/{dataset}/*.py

abaixo está um exemplo de como deveria ser os dados que satisfazem cada coluna desta tabela: 
#colocar nessa linha o json com os dados de exemplo do data_sample_json/{dataset}.json!!

abaixo está um exemplo de retorno esperado de um outro dataset para você se basear:
#colocar nessa linha algum py com um exemplo de retorno esperado do example_of_expected_return/example.py
"""

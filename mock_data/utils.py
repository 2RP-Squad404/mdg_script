# Este arquivo possui a implementação de funções auxiliares da aplicação
import json
import logging
import os
from datetime import datetime

from google.api_core.exceptions import NotFound
from google.cloud import bigquery

# Mapeamento de tipos para interface BigQuery
TYPE_MAPPING = {
    "STRING": "str",
    "TIMESTAMP": "datetime"
}

# Instância do client BigQuery para efetuar a interação com a API GCP BQ
client = bigquery.Client()


def create_table(client, table_id, schema):
    """
    Cria uma tabela no BigQuery com base em um schema recebido.

    Esta função tenta criar uma tabela no BigQuery. Se a tabela já existir, 
    uma mensagem é exibida indicando que a tabela já está disponível. Caso 
    contrário, a tabela será criada com base no schema fornecido.

    Parâmetros:
        client (bigquery.Client): O cliente do BigQuery usado para realizar operações.
        table_id (str): O ID completo da tabela no formato 'project_id.dataset_id.table_id'.
        schema (list[bigquery.SchemaField]): Uma lista de objetos SchemaField que define 
            o esquema da tabela.

    Exceções:
        NotFound: Lançada se a tabela não for encontrada, o que aciona a criação de uma nova tabela.
        google.api_core.exceptions.GoogleAPIError: Captura erros da API do Google BigQuery.
    
    Retorno:
        bigquery.Table: A tabela criada ou uma mensagem informando que ela já existe e o tempo local.
    """
    try:
        table = client.get_table(table_id)
        logging.info(f"Tabela {table.table_id} já existe.")
        print(f"Tabela {table.table_id} já existe.")
    except NotFound:
        try:
            table = bigquery.Table(table_id, schema=schema)
            table = client.create_table(table)
            logging.info(f"Tabela {table.table_id} criada em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
            print(f"Tabela {table.table_id} criada em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

            return table
        except Exception as e:
            logging.error(f"Erro ao criar a tabela {table_id}: {e}")
            raise


def export_table_schema(client, table_id, output_dir='bq_schemas'):
    """
    Exporta o schema de uma tabela do BigQuery em um arquivo JSON no formato para 
    criar modelos com Pydantic.

    Parâmetros:
        client (bigquery.Client): O cliente do BigQuery utilizado para as operações.
        table_id (str): O ID da tabela no formato 'dataset_id.table_id'.
        output_dir (str): O diretório onde o arquivo JSON será salvo. O padrão é 'bq_schemas'.
    
    Exceções:
        google.cloud.exceptions.NotFound: Se a tabela não for encontrada.

    Retorno:
        str: O caminho completo do arquivo JSON gerado e o tempo local
    """
    try:
        table = client.get_table(table_id)
        schema = table.schema
        formatted_schema = {field.name: field.field_type for field in schema}
        os.makedirs(output_dir, exist_ok=True)
        schema_file_name = table.table_id.replace('.', '_') + '.json'
        schema_file_path = os.path.join(output_dir, schema_file_name)
        with open(schema_file_path, 'w') as file:
            json.dump(formatted_schema, file, indent=2)
            print(f"Schema exportado com sucesso para: {schema_file_path} em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")

        return schema_file_path
    except Exception as e:
        print(f"Erro ao exportar schema: {e}")
        raise


def create_class_code(schema: dict, class_name: str) -> str:
    """
    Gera o código de uma classe Pydantic baseada em um schema fornecido.

    Parâmetros:
        schema (dict): Dicionário contendo os campos e seus tipos.
        class_name (str): Nome da classe que será gerada.

    Retorno:
        str: Código Python gerado para a classe.
    """
    class_code = f"class {class_name}(BaseModel):\n"

    for field_name, field_type in schema.items():
        python_type = TYPE_MAPPING.get(field_type, "Any")
        class_code += f"    {field_name}: {python_type}\n"

    return class_code


def write_class_to_file(schema: dict, class_name: str, file_path: str):
    """
    Escreve o código gerado de uma classe Pydantic em um arquivo Python.

    Parâmetros:
        schema (dict): Dicionário contendo os campos e seus tipos.
        class_name (str): Nome da classe que será gerada.
        file_path (str): Caminho completo para salvar o arquivo Python contendo a classe.
    """
    class_code = create_class_code(schema, class_name)

    with open(file_path, "w") as file:
        file.write(class_code)
        print(f"Classe {class_name} gerada com sucesso no arquivo: {file_path}")

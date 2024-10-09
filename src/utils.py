# Este arquivo possui a implementação de funções auxiliares da aplicação
import json
import logging
import os
import sys
import time
from datetime import datetime

import pyfiglet
from google.api_core.exceptions import NotFound
from google.cloud import bigquery

TYPE_MAPPING = {
    "STRING": "str",
    "TIMESTAMP": "datetime"
}

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


def import_table_schema(client, dataset_id, table_id, output_dir='bq_schemas'):
    """
    Exporta o schema de uma tabela do BigQuery em um arquivo JSON no formato para 
    criar modelos com Pydantic.

    Parâmetros:
        client (bigquery.Client): O cliente do BigQuery utilizado para as operações.
        dataset_id (str): O ID do dataset.
        table_id (str): O ID da tabela.
        output_dir (str): O diretório onde o arquivo JSON será salvo. O padrão é 'bq_schemas'.
    
    Exceções:
        google.cloud.exceptions.NotFound: Se a tabela não for encontrada.

    Retorno:
        str: O caminho completo do arquivo JSON gerado e o tempo local
    """
    bq_id = dataset_id + '.' + table_id
    try:
        table = client.get_table(bq_id)
        schema = table.schema
        formatted_schema = {field.name: field.field_type for field in schema}
        os.makedirs(output_dir, exist_ok=True)
        schema_file_name = table.table_id.replace('.', '_') + '.json'
        schema_file_path = os.path.join(output_dir, schema_file_name)
        if os.path.exists(schema_file_path):
            print(f"O schema já foi importado em {schema_file_path}")
            return
        with open(schema_file_path, 'w') as file:
            json.dump(formatted_schema, file, indent=2)
            print(f"Schema importado com sucesso para: {schema_file_path} em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")

        return schema_file_path
    except Exception as e:
        print(f"Erro ao exportar schema: {e}\n")
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


def send_data_to_bigquery(client, dataset_id, table_id, data):
    """
    Envia os dados mockados para tabelas no BigQuery.

    Parâmetros:
        client (bigquery.Client): instância do cliente do BigQuery.
        dataset_id (str): o ID do dataset onde a tabela está localizada.
        table_id (str): o ID da tabela onde os dados serão inseridos.
        data (dict): dados a serem enviados, no formato de lista de dicionários.

    Retorno:
        None: Apenas imprime mensagens informando o status do envio.
    """
    try:
        table_ref = client.dataset(dataset_id).table(table_id)
        table = client.get_table(table_ref)
        errors = client.insert_rows_json(table, data)
        if errors:
            print(f"Erro ao enviar: {errors}")
        else:
            print(f"{len(data)} linha(s) inserida(s) com sucesso para {table_id} em {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.")

    except Exception as e:
        print(f"Erro durante o envio para a tabela {table_id}: {e}")


def loading_bar(duration=5.0, bar_length=30):
    """
    Exibe uma barra de carregamento sofisticada com porcentagem e tempo estimado.

    Parâmetros:
        duration (float): Duração total da barra de carregamento em segundos.
        bar_length (int): Comprimento da barra de carregamento.
    """
    start_time = time.time()
    sys.stdout.write("Loading: [")
    sys.stdout.flush()
    for i in range(bar_length):
        progress = (i + 1) / bar_length
        percentage = int(progress * 100)
        sys.stdout.write("ø")
        sys.stdout.flush()
        elapsed_time = time.time() - start_time
        remaining_time = (1 - progress) * duration
        sys.stdout.write(f"] {percentage}% | Tempo restante: {remaining_time:.1f}s")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
        sys.stdout.write("\rCarregando: [")
    sys.stdout.write("." * bar_length + "] 100% | Carregamento concluído!\n")
    sys.stdout.flush()


def main_menu():
    """
    Exibe o menu principal com as opções disponíveis.
    """
    sys.stdout.flush()
    print("1. Importar schema do BigQuery")
    print("2. Exibir tabelas")
    print("3. Enviar dados")
    print('S. Sair')


def cli_start(word="MDG Script", delay=0.3):
    """
    Exibe uma barra de carregamento seguida pela palavra em ASCII Art com uma animação linha por linha.

    Parâmetros:
        word (str): A palavra que será exibida com letras grandes.
        delay (float): Tempo de atraso entre a exibição de cada linha (em segundos).
    """
    loading_bar(duration=5.0, bar_length=30)
    ascii_art = pyfiglet.figlet_format(word)
    ascii_lines = ascii_art.split("\n")
    sys.stdout.flush()
    for line in ascii_lines:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(delay)


def show_tables(dir='bq_schemas/'):
    """
    Exibe o c
    schemas salvos na pasta 'bq_schemas'

    Parâmetros:
        dir (str): Diretório onde estão salvos os schemas das tabelas
        já importadas.
    """
    # if (os.listdir(dir).count == 1):
    #     print('Ainda não há tabelas salvas.')
    #     sys.exit()
    # else:
    print("Estas são as tabelas salvas: \n")
    print(os.listdir(dir))

def get_tables(dataset_id):
    """
    A função pega os nomes das tabelas e armazena num array, sendo uma leitura
    independente de quantas diver ou nome.

    Parâmetros:
        O nome do dataset que estão as tabelas

    Returns:
        Retorna os nomes em formato de array
    """
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)

    tables = client.list_tables(dataset_ref)

    table_list = []
    for table in tables:
        table_list.append(table.table_id)

    return table_list
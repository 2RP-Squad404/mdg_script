import inspect
import json
import os
from datetime import date, datetime
from decimal import Decimal
from venv import logger


def jsonl_data(data):
    """
    Salva dados em arquivos JSONL, convertendo automaticamente datas e decimais 
    para formatos compatíveis com JSON.

    Parâmetros:
    data (dict): Dicionário onde as chaves são nomes de arrays e os valores são listas de dicionários.
    """
    # Obtendo o nome do arquivo chamador para definir o nome do dataset
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    dataset_name = os.path.splitext(os.path.basename(caller_file))[0]

    # Definindo o caminho de saída
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    output_path = os.path.join(project_root, "src/mock_data", dataset_name)
    os.makedirs(output_path, exist_ok=True)

    def serialize_data(item):
        """Converte datas, decimais e processa dados aninhados para compatibilidade JSON."""
        if isinstance(item, datetime):
            return item.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(item, date):
            return item.strftime('%Y-%m-%d')
        elif isinstance(item, Decimal):
            return float(item)
        elif isinstance(item, dict):
            return {k: serialize_data(v) for k, v in item.items()}
        elif isinstance(item, list):
            return [serialize_data(i) for i in item]
        return item

    for array_name, array_data in data.items():
        filename = f"{array_name}.jsonl"
        filepath = os.path.join(output_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in array_data:
                serialized_item = serialize_data(item)
                json.dump(serialized_item, f, ensure_ascii=False)
                f.write('\n')

    return data

def input_num_linhas():
    """
    Gerar um número de linhas para o arquivo de saída.

    Returno:
        int: Número de linhas para o arquivo de saída.
    """
    while True:
        try:
            num_linhas = int(input("Quantas linhas deseja gerar?\n"))
            return num_linhas
        except ValueError:
            logger.info("Digite um valor inteiro")
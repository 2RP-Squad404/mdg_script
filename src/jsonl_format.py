import inspect 
import os
import gemini_datagen
import json
from decimal import Decimal
from gemini_datagen import criar_Acordo

NUM_LINES = 1
OUTPUT_DIR = 'jsonl_mock'

def create_jsonL(faker_func, num_lines):
    """
    Cria um arquivo JSONL com dados gerados pelo Faker.

    Esta função invoca a função Faker fornecida para gerar um número específico de 
    linhas de dados e grava esses dados em um arquivo JSONL. O nome do arquivo é 
    derivado do nome da função Faker, utilizando a parte do nome após o primeiro 
    sublinhado.

    Parâmetros:
    faker_func (function): Uma função que gera um dicionário com dados 
                           falsos. A função deve retornar um dicionário onde 
                           as chaves representam os campos do JSONL.
    num_lines (int): O número de linhas a serem geradas e escritas no arquivo JSONL.
    """
    os.makedirs(OUTPUT_DIR,exist_ok=True)

    filename = os.path.join(OUTPUT_DIR, faker_func.__name__.split('_', 1)[1] + '.jsonl') 

    with open(filename, mode='w', encoding='utf-8') as arquivo_jsonl:
        for _ in range(num_lines):
            datamock = faker_func()  
            datamock = convert_decimals(datamock)
            arquivo_jsonl.write(json.dumps(datamock) + '\n')

def convert_decimals(obj):
    """
    Converte todos os valores Decimal em um dicionário para float, 
    garantindo compatibilidade com JSON.
    """
    if isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_decimals(item) for item in obj]
    elif isinstance(obj, Decimal):
        return float(obj)
    return obj

create_jsonL(criar_Acordo,NUM_LINES)


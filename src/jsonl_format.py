import inspect 
import os
import json
from decimal import Decimal
from datetime import datetime, date
from gemini_datagen_pfs_risco_tivea import criar_cobranca_campo_customizavel_faker

NUM_LINES = 1000
OUTPUT_DIR = 'jsonl_mock'

# def serialize_dates_old(row):
#     for key, value in row.items():
#         if isinstance(value, datetime):
#             row[key] = value.isoformat()  # Converte datetime para string
#     return row

def serialize_dates(data):
    """
    Converte todas as instâncias de datetime e date no dicionário para strings formatadas.
    """
    for key, value in data.items():
        if isinstance(value, datetime):
            data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(value, date):
            data[key] = value.strftime('%Y-%m-%d')
        elif isinstance(value, dict):
            # Processa valores aninhados
            data[key] = serialize_dates(value)
        elif isinstance(value, list):
            # Processa listas de valores, aplicando a função em cada item
            data[key] = [serialize_dates(item) if isinstance(item, dict) else item for item in value]
    return data


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
            datamock = serialize_dates(datamock)
            # print(datamock)
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


create_jsonL(faker_func=criar_cobranca_campo_customizavel_faker,num_lines=NUM_LINES)


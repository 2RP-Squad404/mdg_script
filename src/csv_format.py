import csv 
import inspect 
import os
import gemini_datagen

NUM_LINES = 150
OUTPUT_DIR = 'csv_mock'

## Criação do csv para envio ao BigQuery
def create_csv(faker_func, num_lines):
    """
    Cria um arquivo CSV com dados gerados pelo Faker.

    Esta função invoca a função Faker fornecida para gerar um número específico de 
    linhas de dados e grava esses dados em um arquivo CSV. O nome do arquivo é 
    derivado do nome da função Faker, utilizando a parte do nome após o primeiro 
    sublinhado.

    Parâmetros:
    faker_func (function): Uma função que gera um dicionário com dados 
                           falsos. A função deve retornar um dicionário onde 
                           as chaves representam os campos do CSV.
    num_lines (int): O número de linhas a serem geradas e escritas no arquivo CSV.
    """
    first_dict = faker_func() 
    filename = os.path.join(OUTPUT_DIR, faker_func.__name__.split('_', 1)[1] + '.csv') 
    campos = first_dict.keys()  
    with open(filename, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for _ in range(num_lines):
            datamock = faker_func()  
            escritor_csv.writerow(datamock)

for func_name, obj in inspect.getmembers(gemini_datagen):
    if inspect.isfunction(obj):
        create_csv(obj, NUM_LINES)

import csv 
import inspect 
import gemini_datagen

NUM_LINES = 150

## Criação do csv para envio ao BigQuery
def create_csv(faker_func, num_lines):
    # Gera um dicionário inicial para obter os campos
    first_dict = faker_func()  # Chama a função para obter o primeiro dicionário
    filename = faker_func.__name__.split('_', 1)[1] + '.csv'  # Define o nome do arquivo
    campos = first_dict.keys()  
    
    # Cria e escreve no arquivo CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for _ in range(num_lines):
            datamock = faker_func()  # Chama a função para gerar os dados
            escritor_csv.writerow(datamock)

# Itera sobre todas as funções no módulo gemini_datagen
for func_name, obj in inspect.getmembers(gemini_datagen):
    if inspect.isfunction(obj):
        create_csv(obj, NUM_LINES)  # Passa a referência da função

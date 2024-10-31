"""import json
from faker import Faker
from datetime import date, datetime
import os

faker = Faker('pt_BR')

# As funções abaixo são responsáveis por criar dados mock para o dataset pfs_risco_raw_tivea
# observe que as funções correspondem a tabelas presentes no dataset.

def DataGen(num_records, output_dir="src/mock_data"):

    Insira os Arrays dos Dicionários    

    data = {'arrays':[], ...}

    for _ in range(num_records):
        

    Insira as funções faker

    # Obtendo o nome do dataset
    dataset_name = os.path.splitext(os.path.basename(__file__))[0]

    # Obtendo o caminho absoluto do diretório raiz do projeto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    output_path = os.path.join(project_root, output_dir, dataset_name)

    os.makedirs(output_path, exist_ok=True)

    # Salvando os dados
    for array_name, array_data in data.items():
        filename = f"{array_name}.jsonl"
        filepath = os.path.join(output_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in array_data:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')

    return data

num_records = 100
generated_data = DataGen(num_records)"""

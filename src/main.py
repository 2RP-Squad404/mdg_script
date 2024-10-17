import sys

from google.cloud import bigquery
from config import PROJECT_ID
from utils import cli_start, import_table_schema, main_menu, get_tables,write_class_to_file,get_all_schemas,create_tables_with_schemas

client = bigquery.Client(PROJECT_ID)

cli_start()
main_menu()

while True:
    choice = input("\nEscolha uma opção (1-4): \n" + "> ")
    print("1. Importar schema do BigQuery")
    print("2. Exibir tabelas")
    print("3. Enviar dados")
    print("4. Criar tabelas via json")
    print('S. Sair')
    if choice == "1":
            print("\nOpção 1 selecionada: Importar um schema do BigQuery\n")
            dataset = input("Insira o ID do dataset:\n")
            table = input("Insira o ID da tabela:\n")
            schemas = import_table_schema(client=client, dataset_id=dataset, table_id=table)
            write_class_to_file(schemas,table,)
            print("\n")
    elif choice == "2":
            print("\nOpção 2 selecionada: Exibir tabelas\n")
            get_tables()
    elif choice == "3":
            print("\nOpção 3 selecionada: Enviar dados\n")
    elif choice == "4":
            while True:
                print("\nOpção 4 selecionada: Criar tabelas via json\n")
                dataset_number = input("\nSelecione qual dataset irá ser gerado os dados\n1. pfs_raw_conductor\n2. pfs_unificacao_pefisa\n")
                
                if dataset_number == "1":
                        directory_schema = "bq_schemas/pfs_raw_conductor"
                        dataset_id = 'pfs_raw_conductor'
                elif dataset_number == "2":
                        directory_schema = "bq_schemas/pfs_unificacao_pefisa"
                        dataset_id = 'pfs_unificacao_pefisa'
                else:
                        print("\nOpção inválida")
                
                schemas = get_all_schemas(directory_schema)
                create_tables_with_schemas(schemas, dataset_id)
                for schema_info in schemas:
                        table_name = schema_info['filename'].replace('.json', '')
    elif choice == 'S' or choice == 's':
            print('Encerrando aplicação...')
            sys.exit()
    else:
            print("\nOpção inválida. Tente novamente.\n")


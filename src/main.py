
import sys

from google.cloud import bigquery
from utils import cli_start, import_table_schema, main_menu, show_tables, write_class_to_file
project_id = 'sapient-cycling-434419-u0'

client = bigquery.Client(project = project_id)

cli_start()
main_menu()

while True:
    choice = input("\nEscolha uma opção (1-3): \n" + "> ")
    print("1. Importar schema do BigQuery")
    print("2. Exibir tabelas")
    print("3. Enviar dados")
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
            show_tables()
    elif choice == "3":
            print("\nOpção 3 selecionada: Enviar dados\n")
    elif choice == 'S' or choice == 's':
            print('Encerrando aplicação...')
            sys.exit()
    else:
            print("\nOpção inválida. Tente novamente.\n")


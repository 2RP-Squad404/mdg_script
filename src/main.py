
import sys

from google.cloud import bigquery
from utils import cli_start, import_table_schema, main_menu, show_tables,inspect_table_schema, write_class_to_file,get_all_schemas,create_tables_with_schemas

client = bigquery.Client(project="just-lore-435816-v8")
dataset_id = 'just-lore-435816-v8.json_data'


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
            show_tables()
    elif choice == "3":
            print("\nOpção 3 selecionada: Enviar dados\n")
    elif choice == "4":
            print("\nOpção 4 selecionada: Criar tabelas via json\n")
            schemas = get_all_schemas("json_files")
            create_tables_with_schemas(schemas, dataset_id)
            for schema_info in schemas:
                table_name = schema_info['filename'].replace('.json', '')
                inspect_table_schema(dataset_id, table_name)
    elif choice == 'S' or choice == 's':
            print('Encerrando aplicação...')
            sys.exit()
    else:
            print("\nOpção inválida. Tente novamente.\n")


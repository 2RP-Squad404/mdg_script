
import sys

from google.cloud import bigquery
from utils import (
    cli_start,
    import_table_schema,
    main_menu,
    show_tables
)

client = bigquery.Client()

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
            import_table_schema(client=client, dataset_id=dataset, table_id=table)
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

# num_of_lines = input("Quantas linhas você deseja inserir na tabela Card? ")
# def send_to_card_table(card_mock_data, dataset_id, table_id):
#     table_ref = client.dataset(dataset_id).table(table_id)
#     table = client.get_table(table_ref)
#     line_mock_data = [card_mock_data]
#     errors = client.insert_rows_json(table, line_mock_data)
#     if errors:
#         print(f"Erro ao enviar: {errors}")
# card_mock_data = []
# for i in range(int(num_of_lines)):
#     card_mock_data.append(generate_cardevent())
# dataset_id = settings.PFS_UNIFICACAO_PEFISA_DATASET_ID
# table_id = settings.MOCK_CARD_TABLE_ID
# for k in range(int(num_of_lines)):
#     send_to_card_table(card_mock_data[k], dataset_id, table_id)
#     print("Enviando dados..." + f"Restam {int(num_of_lines) - k} linhas.")
# end_code = time.time()
# print(f"Envio dos dados finalizado em {(end_code - start):.2f}ms")

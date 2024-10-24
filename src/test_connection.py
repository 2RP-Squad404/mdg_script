import logging
from auth import get_bigquery_client

"""
Este script autentica no BigQuery usando credenciais armazenadas no Google Secret Manager
e executa uma query simples para verificar a conexão.

Funções principais:
- `get_bigquery_client`: Função importada do módulo `auth` que autentica usando
  credenciais obtidas do Secret Manager e retorna um cliente do BigQuery.

Passos:
1. Autentica no BigQuery com o cliente retornado por `get_bigquery_client`.
2. Se a autenticação for bem-sucedida, executa uma query para obter a data atual.
3. Registra os resultados da query no log, indicando que a conexão foi bem-sucedida.
4. Registra no log qualquer erro que ocorra ao executar a query ou se a autenticação falhar.

"""

logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')

client = get_bigquery_client()

if client is not None:
    try:
        query = "SELECT current_date() as today"
        query_job = client.query(query)

        for row in query_job:
            logging.info(f"Conexão bem-sucedida! Data de hoje: {row['today']}")
            logging.info("Autenticado com a conta de serviço.")
    except Exception as e:
        logging.error(f"Erro ao executar a query: {e}")
else:
    logging.error("Falha ao autenticar.")

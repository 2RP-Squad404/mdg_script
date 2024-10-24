import logging
from auth import get_bigquery_client

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

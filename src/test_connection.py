from auth import get_bigquery_client

# Inicializa o cliente do BigQuery
client = get_bigquery_client()

if client is not None:
    try:
        # Executa uma query simples para verificar a autenticação
        query = "SELECT current_date() as today"
        query_job = client.query(query)
        
        # Verifica se a query foi executada com sucesso
        for row in query_job:
            print(f"Conexão bem-sucedida! Data de hoje: {row['today']}")
            print("BigQuery está autenticado com a conta de serviço.")
    except Exception as e:
        print(f"Erro ao executar a query: {e}")
else:
    print("Falha ao autenticar o cliente do BigQuery.")

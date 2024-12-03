from google.cloud import bigquery

segmentacao_cliente = [
    bigquery.SchemaField('data_processamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_cpf', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('ind_comprou_03m', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('ind_comprou_06m', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('ind_comprou_12m', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('ind_comprou_24m', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('qtd_compras_ult_24m', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('ticket_medio_ult_24m', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('r', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('f', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('v', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cod_segmento_rfv', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('segmento_rfv', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('mes_processamento', 'DATE', 'NULLABLE'),
]

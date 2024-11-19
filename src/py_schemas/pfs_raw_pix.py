from google.cloud import bigquery

# Dataset: pfs_raw_pix, Table: v_dict_direto
v_dict_direto = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção do registro.'),
    bigquery.SchemaField('account', 'RECORD', 'NULLABLE', description='Informações da conta.'),
    bigquery.SchemaField('clearingAcknowledgeTimestampUtc', 'STRING', 'NULLABLE', description='Carimbo de data/hora UTC do reconhecimento da compensação.'),
    bigquery.SchemaField('clearingEndClaimTimestampUtc', 'STRING', 'NULLABLE', description='Carimbo de data/hora UTC do fim da compensação.'),
    bigquery.SchemaField('confirmationToken', 'STRING', 'NULLABLE', description='Token de confirmação.'),
    bigquery.SchemaField('holder', 'RECORD', 'NULLABLE', description='Informações do titular da conta.'),
    bigquery.SchemaField('key', 'RECORD', 'NULLABLE', description='Chave de identificação.'),
    bigquery.SchemaField('newStatus', 'RECORD', 'NULLABLE', description='Novo status.'),
    bigquery.SchemaField('newStatusUtcTimestamp', 'STRING', 'NULLABLE', description='Carimbo de data/hora UTC da atualização do status.'),
    bigquery.SchemaField('reason', 'STRING', 'NULLABLE', description='Motivo da atualização.')
]

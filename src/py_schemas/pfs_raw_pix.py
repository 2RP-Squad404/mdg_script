from google.cloud import bigquery

# Dataset: pfs_raw_pix, Table: v_dict_direto
v_dict_direto = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção do registro.'),
    bigquery.SchemaField('account', 'RECORD', 'NULLABLE', description='Informações da conta.', fields=[
        bigquery.SchemaField('branch', 'STRING', 'NULLABLE', description='Nome ou código da agência.'),
        bigquery.SchemaField('accountNumber', 'STRING', 'NULLABLE', description='Número da conta.'),
        bigquery.SchemaField('accountType', 'STRING', 'NULLABLE', description='Tipo de conta.'),
        bigquery.SchemaField('openingDate', 'STRING', 'NULLABLE', description='Data de abertura da conta.')
    ]),
    bigquery.SchemaField('clearingAcknowledgeTimestampUtc', 'STRING', 'NULLABLE', description='Carimbo de data/hora UTC do reconhecimento da compensação.'),
    bigquery.SchemaField('clearingEndClaimTimestampUtc', 'STRING', 'NULLABLE', description='Carimbo de data/hora UTC do fim da compensação.'),
    bigquery.SchemaField('confirmationToken', 'STRING', 'NULLABLE', description='Token de confirmação.'),
    bigquery.SchemaField('holder', 'RECORD', 'NULLABLE', description='Informações do titular da conta.', fields=[
        bigquery.SchemaField('name', 'STRING', 'NULLABLE', description='Nome completo do titular.'),
        bigquery.SchemaField('tradeName', 'STRING', 'NULLABLE', description='Nome comercial do titular (se aplicável).'),
        bigquery.SchemaField('taxId', 'STRING', 'NULLABLE', description='CPF ou CNPJ do titular.')
    ]),
    bigquery.SchemaField('key', 'RECORD', 'NULLABLE', description='Chave de identificação.', fields=[
        bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID da chave.'),
        bigquery.SchemaField('value', 'STRING', 'NULLABLE', description='Valor da chave.'),
        bigquery.SchemaField('type', 'STRING', 'NULLABLE', description='Tipo da chave.')
    ]),
    bigquery.SchemaField('newStatus', 'RECORD', 'NULLABLE', description='Novo status.', fields=[
        bigquery.SchemaField('id', 'INTEGER', 'NULLABLE', description='ID do status.'),
        bigquery.SchemaField('description', 'STRING', 'NULLABLE', description='Descrição do status.')
    ]),
    bigquery.SchemaField('newStatusUtcTimestamp', 'STRING', 'NULLABLE', description='Carimbo de data/hora UTC da atualização do status.'),
    bigquery.SchemaField('reason', 'STRING', 'NULLABLE', description='Motivo da atualização.')
]

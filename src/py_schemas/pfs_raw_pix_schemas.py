from google.cloud import bigquery

# Dataset: pfs_raw_pix, Table: v_dict_direto
v_dict_direto_schema = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('account', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('branch', 'STRING', 'NULLABLE'), bigquery.SchemaField('accountNumber', 'STRING', 'NULLABLE'), bigquery.SchemaField('accountType', 'STRING', 'NULLABLE'), bigquery.SchemaField('openingDate', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('clearingAcknowledgeTimestampUtc', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('clearingEndClaimTimestampUtc', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('confirmationToken', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('holder', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('name', 'STRING', 'NULLABLE'), bigquery.SchemaField('tradeName', 'STRING', 'NULLABLE'), bigquery.SchemaField('taxId', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('key', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'STRING', 'NULLABLE'), bigquery.SchemaField('value', 'STRING', 'NULLABLE'), bigquery.SchemaField('type', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('newStatus', 'RECORD', 'NULLABLE', fields=[bigquery.SchemaField('id', 'INTEGER', 'NULLABLE'), bigquery.SchemaField('description', 'STRING', 'NULLABLE')]),
    bigquery.SchemaField('newStatusUtcTimestamp', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('reason', 'STRING', 'NULLABLE'),
]

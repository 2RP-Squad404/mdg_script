from google.cloud import bigquery

# Dataset: pfs_raw_pix, Table: v_dict_direto
v_dict_direto_schema = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('account', 'RECORD', 'NULLABLE'),
    bigquery.SchemaField('clearingAcknowledgeTimestampUtc', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('clearingEndClaimTimestampUtc', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('confirmationToken', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('holder', 'RECORD', 'NULLABLE'),
    bigquery.SchemaField('key', 'RECORD', 'NULLABLE'),
    bigquery.SchemaField('newStatus', 'RECORD', 'NULLABLE'),
    bigquery.SchemaField('newStatusUtcTimestamp', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('reason', 'STRING', 'NULLABLE'),
]

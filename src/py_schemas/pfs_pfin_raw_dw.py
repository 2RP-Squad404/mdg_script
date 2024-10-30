from google.cloud import bigquery

# Dataset: pfs_pfin_raw_dw, Table: dw_funcionario
dw_funcionario = [
    bigquery.SchemaField('sk_funcionario', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_chapa_so', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nom_funcionario', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('sk_local', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('sk_cargo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dat_dia_admissao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_dia_demissao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_dia_ini_afastamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_dia_fim_afastamento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('des_email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dat_inc_dw', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_ult_alt_dw', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dat_exc_dw', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('sk_situacao_funcionario', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('num_cpf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('num_rg', 'STRING', 'NULLABLE'),
]

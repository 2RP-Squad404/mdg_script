from google.cloud import bigquery

dw_funcionario = [
    bigquery.SchemaField('sk_funcionario', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('num_chapa_so', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('nom_funcionario', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('sk_local', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('sk_cargo', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_dia_admissao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_dia_demissao', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_dia_ini_afastamento', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_dia_fim_afastamento', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('des_email', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_inc_dw', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_ult_alt_dw', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('dat_exc_dw', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('sk_situacao_funcionario', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('num_cpf', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('num_rg', 'STRING', 'NULLABLE', description='None'),
]

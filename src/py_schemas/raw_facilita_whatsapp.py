from google.cloud import bigquery

# Dataset: raw_facilita_whatsapp, Table: revendedor
revendedor = [
    bigquery.SchemaField('id_revendedor', 'INTEGER', 'NULLABLE', description='None'),
    bigquery.SchemaField('nome_revendedor', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('cpf_cnpj_revendedor', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('telefone_revendedor', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('email_revendedor', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('datahora_cadastro', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('datahora_aceite', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('cep', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('cod_loja', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('dth_inc', 'TIMESTAMP', 'NULLABLE', description='None'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE', description='None'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='None')
]

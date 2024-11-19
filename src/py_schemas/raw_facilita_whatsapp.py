from google.cloud import bigquery

# Dataset: raw_facilita_whatsapp, Table: revendedor
revendedor = [
    bigquery.SchemaField('id_revendedor', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nome_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cpf_cnpj_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('telefone_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('email_revendedor', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('datahora_cadastro', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('datahora_aceite', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cep', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cod_loja', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_inc', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE')
]

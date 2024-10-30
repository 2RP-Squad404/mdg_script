from google.cloud import bigquery

# Dataset: pfs_risco_raw_neurotech, Table: proposta
proposta = [
    bigquery.SchemaField('hash_key', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('codigooperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('codigoproposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nomepolitica', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('resultado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('instante_data', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('mensagem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('sucesso', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('versaopolitica', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('tempo_execucao_msec', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('instantefim', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('instanceinicio', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_raw_neurotech, Table: proposta_consultas
proposta_consultas = [
    bigquery.SchemaField('hash_key', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('codigooperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('status', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('retornos', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('datarealizacao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dhfim', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('entradas', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('idlog', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dhinicio', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('descricao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('instante_data', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
]


# Dataset: pfs_risco_raw_neurotech, Table: proposta_detalhe
proposta_detalhe = [
    bigquery.SchemaField('hash_key', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('codigooperacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('entradas', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('calculadas', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('outros', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('retornos', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('variaveis', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('fluxo_regras', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('banco', 'JSON', 'NULLABLE'),
    bigquery.SchemaField('instante_data', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
]

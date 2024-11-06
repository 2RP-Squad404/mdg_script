from google.cloud import bigquery

# Dataset: pfs_risco_raw_neurotech, Table: proposta
proposta = [
    bigquery.SchemaField('hash_key', 'STRING', 'NULLABLE', description='Chave hash única para o registro.'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE', description='Origem do dado.'),
    bigquery.SchemaField('codigooperacao', 'STRING', 'NULLABLE', description='Código da operação.'),
    bigquery.SchemaField('codigoproposta', 'STRING', 'NULLABLE', description='Código da proposta.'),
    bigquery.SchemaField('nomepolitica', 'STRING', 'NULLABLE', description='Nome da política de risco aplicada.'),
    bigquery.SchemaField('resultado', 'STRING', 'NULLABLE', description='Resultado da avaliação de risco (aprovado/reprovado).'),
    bigquery.SchemaField('instante_data', 'TIMESTAMP', 'NULLABLE', description='Data e hora da avaliação.'),
    bigquery.SchemaField('mensagem', 'STRING', 'NULLABLE', description='Mensagem de retorno da avaliação.'),
    bigquery.SchemaField('sucesso', 'STRING', 'NULLABLE', description='Indicador de sucesso (sim/não).'),
    bigquery.SchemaField('versaopolitica', 'STRING', 'NULLABLE', description='Versão da política de risco.'),
    bigquery.SchemaField('dth_inclusao', 'TIMESTAMP', 'NULLABLE', description='Data e hora de inclusão do registro.'),
    bigquery.SchemaField('tempo_execucao_msec', 'FLOAT', 'NULLABLE', description='Tempo de execução em milissegundos.'),
    bigquery.SchemaField('instantefim', 'TIMESTAMP', 'NULLABLE', description='Data e hora do fim da avaliação.'),
    bigquery.SchemaField('instanceinicio', 'TIMESTAMP', 'NULLABLE', description='Data e hora do início da avaliação.'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção do dado.')
]


# Dataset: pfs_risco_raw_neurotech, Table: proposta_consultas
proposta_consultas = [
    bigquery.SchemaField('hash_key', 'STRING', 'NULLABLE', description='Chave hash única para o registro.'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE', description='Origem do dado.'),
    bigquery.SchemaField('codigooperacao', 'STRING', 'NULLABLE', description='Código da operação.'),
    bigquery.SchemaField('status', 'STRING', 'NULLABLE', description='Status da consulta.'),
    bigquery.SchemaField('retornos', 'JSON', 'NULLABLE', description='Retornos da consulta em formato JSON.'),
    bigquery.SchemaField('datarealizacao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da realização da consulta.'),
    bigquery.SchemaField('dhfim', 'TIMESTAMP', 'NULLABLE', description='Data e hora do fim da consulta.'),
    bigquery.SchemaField('entradas', 'JSON', 'NULLABLE', description='Entradas da consulta em formato JSON.'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE', description='ID da consulta.'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE', description='Nome da consulta.'),
    bigquery.SchemaField('idlog', 'STRING', 'NULLABLE', description='ID do log.'),
    bigquery.SchemaField('origem', 'STRING', 'NULLABLE', description='Origem da consulta.'),
    bigquery.SchemaField('dhinicio', 'TIMESTAMP', 'NULLABLE', description='Data e hora do início da consulta.'),
    bigquery.SchemaField('descricao', 'STRING', 'NULLABLE', description='Descrição da consulta.'),
    bigquery.SchemaField('instante_data', 'TIMESTAMP', 'NULLABLE', description='Data e hora do registro.'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção do dado.')
]


# Dataset: pfs_risco_raw_neurotech, Table: proposta_detalhe
proposta_detalhe = [
    bigquery.SchemaField('hash_key', 'STRING', 'NULLABLE', description='Chave hash única para o registro.'),
    bigquery.SchemaField('source', 'STRING', 'NULLABLE', description='Origem do dado.'),
    bigquery.SchemaField('codigooperacao', 'STRING', 'NULLABLE', description='Código da operação.'),
    bigquery.SchemaField('entradas', 'JSON', 'NULLABLE', description='Dados de entrada em formato JSON.'),
    bigquery.SchemaField('calculadas', 'JSON', 'NULLABLE', description='Dados calculados em formato JSON.'),
    bigquery.SchemaField('outros', 'JSON', 'NULLABLE', description='Outros dados em formato JSON.'),
    bigquery.SchemaField('retornos', 'JSON', 'NULLABLE', description='Dados de retorno em formato JSON.'),
    bigquery.SchemaField('variaveis', 'JSON', 'NULLABLE', description='Variáveis em formato JSON.'),
    bigquery.SchemaField('fluxo_regras', 'JSON', 'NULLABLE', description='Fluxo de regras em formato JSON.'),
    bigquery.SchemaField('banco', 'JSON', 'NULLABLE', description='Dados do banco em formato JSON.'),
    bigquery.SchemaField('instante_data', 'TIMESTAMP', 'NULLABLE', description='Data e hora do registro.'),
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE', description='Data de produção do dado.')
]

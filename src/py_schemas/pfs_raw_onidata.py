from google.cloud import bigquery

v_credito_pessoal_contratos = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('dth_inclusao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('assinatura_info', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('browser', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('data', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('ip', 'STRING', 'NULLABLE')
        ]
    ),
    bigquery.SchemaField('canal', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nome', 'STRING', 'NULLABLE')
        ]
    ),
    bigquery.SchemaField('canal_atendimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cargo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('ccb_original_html', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('ccb_original_pdf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cliente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cliente_info_no_contrato', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('cargo', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('conjuge', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('cpf', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('data_nascimento', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('documento', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('data_emissao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('emissor', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('foto', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('numero', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('uf', 'STRING', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('email', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('endereco', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('bairro', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('cep', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('cidade', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('complemento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('foto', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('logradouro', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('numero', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('pais', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('residencia_tempo', 'INTEGER', 'NULLABLE'),
            bigquery.SchemaField('residencia_tipo', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('uf', 'STRING', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('escolaridade', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('estado_civil', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nacionalidade', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nascimento_uf', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nome', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nome_mae', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nome_pai', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('pagamento', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('agencia', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('agencia_dac', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('banco', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('banco_nome', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('cliente_desde', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('cnpj_responsavel', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('conta', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('conta_dac', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('cpf_responsavel', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('individual_ou_conjunta', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('nome_gerente', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('nome_titular', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('praca', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('telefone', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo', 'STRING', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('resourcetype', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('salario', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('salario_bruto', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('salario_liquido', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('sexo', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('sobrenome', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('telefone_celular', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('telefone_fixo', 'STRING', 'NULLABLE')
        ]
    ),
    bigquery.SchemaField('cpf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cpf_operador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_efetivacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_nascimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_pagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_primeiro_vencimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_solicitacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_ultimo_vencimento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dias_cobranca_multa', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('documentacao_comprovacao', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('identidade_frente', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('alterado_em', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('data_aprovacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('motivo_negado', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('status_documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo', 'STRING', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('identidade_verso', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('alterado_em', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('data_aprovacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('motivo_negado', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('status_documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo', 'STRING', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('renda', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('alterado_em', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('data_aprovacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('motivo_negado', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('status_documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo', 'STRING', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('residencia', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('alterado_em', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('data_aprovacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('motivo_negado', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('status_documento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo', 'STRING', 'NULLABLE')
            ]
        )
        ]
    ),
    bigquery.SchemaField('email', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('escolaridade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('estado_civil', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('financeira', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('cnpj', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('nome_fantasia', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('razao_social', 'STRING', 'NULLABLE')
        ]
    ),
    bigquery.SchemaField('financeira_valor_a_pagar', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('gerado_em', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('localizador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('METADADOS', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('PEFISA', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('codigoProduto', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('codigoLoja', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('idContaCredito', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('idPessoa', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('usuarioLogado', 'STRING', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('PEFISA_FGTS', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('operador_comissao', 'STRING', 'NULLABLE')
            ]
        )
        ]
    ),
    bigquery.SchemaField('modalidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nacionalidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nascimento_uf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nome', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nome_mae', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nome_operador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nome_pai', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('origem', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('parcelas_info', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('em_atraso', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('recebiveis', 'JSON', 'REPEATED'),
            bigquery.SchemaField('total', 'FLOAT', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('pagas', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('recebiveis', 'JSON', 'REPEATED'),
            bigquery.SchemaField('total', 'FLOAT', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('pendentes', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('recebiveis', 'JSON', 'REPEATED'),
            bigquery.SchemaField('total', 'FLOAT', 'NULLABLE')
            ]
        )
        ]
    ),
    bigquery.SchemaField('prazo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('salario_bruto', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('salario_liquido', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('saldo_devedor', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('sexo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('sobrenome', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('status', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('status_alterado_em', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxa_cet_mes', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('taxa_contrato', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('taxa_iof', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('taxa_iof_complementar', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('taxa_irr', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('taxa_multa', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('taxa_permanencia', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('telefone_celular', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('telefone_fixo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_financiado', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_iof', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_juros', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_liberado', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_parcela', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_recebivel', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_seguro', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_tarifas', 'FLOAT', 'NULLABLE'),
]

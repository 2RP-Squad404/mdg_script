from google.cloud import bigquery

v_contrato = [
    bigquery.SchemaField('production_date', 'DATE', 'NULLABLE'),
    bigquery.SchemaField('codigo_do_produto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numero_operacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numero_pedido', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numero_proposta', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tipo_operacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('banco_portabilidade', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('numero_carteira', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('produto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('descricao_convenio', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('modalidade_produto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('login_chapa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_base', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_emissao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_vencimento_operacao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('status_contrato', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('estornado_em', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('status_pagamento_funcao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_troco', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tipo_de_pagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('empresa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('matriz', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('regional', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('promotora', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('empregador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('orgao', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('a1O2', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('seguro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('agente_certificado_chapa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('agente_certificado_cpf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('representante_legal_cpf', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('representante_legal_nome', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('correspondente', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('digitador', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('qtde_parcelas_em_aberto', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('qtde_parcelas_pagas', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('qtde_parcelas_em_atraso', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('taxa_juros_cl_ano', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxa_juros_cl_mes', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxa_apropriacao_ano', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxa_apropriacao_mes', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxa_cet_mes', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxa_iof', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('taxa_iof_complementar', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_principal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_juros_contratado', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_TAC', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_bruto', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_IOF', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_mora', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_perc_mora', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_multa', 'FLOAT', 'NULLABLE'),
    bigquery.SchemaField('valor_perc_multa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_do_iof_vencido', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('valor_saldo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dados_cliente', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('nome', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('documento_cliente', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('matricula', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('email', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('sexo', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('ddd_celular', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('telefone_celular', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('data_nascimento', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('banco_pagamento', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('agencia_pagamento', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('conta_corrente_pagamento', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('digito_conta_corrente', 'STRING', 'NULLABLE')
        ]
    ),
    bigquery.SchemaField('parcelas_abertas', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('data_vencimento', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('movimentacoes', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('baixa_parcela_sn', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('data_movimentacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('mes_referencia', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo_de_movimentacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valor_iof_atraso_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_juros_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_mora_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_multa_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('id_pagamento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valor_principal_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_total_pago', 'FLOAT', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('numero_parcela', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('qtde_atraso', 'INTEGER', 'NULLABLE'),
        bigquery.SchemaField('dias_cobranca_multa', 'INTEGER', 'NULLABLE'),
        bigquery.SchemaField('desconto_antecipacao_concedido', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('cancelado', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('saldo_devedor', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_despesa', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_iof_atraso', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_juros_parcela', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_mora', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_multa', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_parcela', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_presente', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_principal_parcela', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_tarifa', 'FLOAT', 'NULLABLE')
        ]
    ),
    bigquery.SchemaField('parcelas_liquidadas', 'RECORD', 'NULLABLE',
    fields=[
        bigquery.SchemaField('data_liquidacao', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('data_vencimento', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('dias_cobranca_multa', 'INTEGER', 'NULLABLE'),
        bigquery.SchemaField('desconto_antecipacao_concedido', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('cancelado', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('movimentacoes', 'RECORD', 'NULLABLE',
        fields=[
            bigquery.SchemaField('baixa_parcela_sn', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('data_movimentacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('mes_referencia', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('tipo_de_movimentacao', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valor_iof_atraso_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_juros_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_mora_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_multa_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('valor_principal_pago', 'FLOAT', 'NULLABLE'),
            bigquery.SchemaField('id_pagamento', 'STRING', 'NULLABLE'),
            bigquery.SchemaField('valor_total_pago', 'FLOAT', 'NULLABLE')
            ]
        ),
        bigquery.SchemaField('numero_parcela', 'STRING', 'NULLABLE'),
        bigquery.SchemaField('valor_juros_parcela', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_parcela', 'FLOAT', 'NULLABLE'),
        bigquery.SchemaField('valor_principal_parcela', 'FLOAT', 'NULLABLE')
        ]
    ),
]
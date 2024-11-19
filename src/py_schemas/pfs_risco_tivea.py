from google.cloud import bigquery

# Dataset: pfs_risco_tivea, Table: cartao
cartao = [
    bigquery.SchemaField('id_cartao', 'INTEGER', 'NULLABLE', description='ID único do cartão.'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE', description='ID do produto do cartão.'),
    bigquery.SchemaField('num_cartao', 'STRING', 'NULLABLE', description='Número do cartão.'),
    bigquery.SchemaField('num_seq_via_cartao', 'INTEGER', 'NULLABLE', description='Número sequencial da via do cartão.'),
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE', description='ID da conta associada ao cartão.'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE', description='CPF do cliente.'),
    bigquery.SchemaField('cod_tip_portador', 'INTEGER', 'NULLABLE', description='Código do tipo de portador.'),
    bigquery.SchemaField('num_bin', 'INTEGER', 'NULLABLE', description='Número de identificação do banco (BIN).'),
    bigquery.SchemaField('cod_loja_emis_cartao', 'INTEGER', 'NULLABLE', description='Código da loja emissora do cartão.'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE', description='ID do cliente no sistema.'),
    bigquery.SchemaField('dth_emis_cartao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da emissão do cartão.'),
    bigquery.SchemaField('dth_embs_cartao', 'TIMESTAMP', 'NULLABLE', description='Data e hora do embossing do cartão.'),
    bigquery.SchemaField('dth_valid_cartao', 'TIMESTAMP', 'NULLABLE', description='Data e hora de validade do cartão.'),
    bigquery.SchemaField('dth_desbloqueio', 'TIMESTAMP', 'NULLABLE', description='Data e hora do desbloqueio do cartão.'),
    bigquery.SchemaField('cod_sit_cartao', 'INTEGER', 'NULLABLE', description='Código da situação do cartão.'),
    bigquery.SchemaField('des_sit_cartao', 'STRING', 'NULLABLE', description='Descrição da situação do cartão.'),
    bigquery.SchemaField('dth_sit_cartao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da alteração da situação do cartão.'),
    bigquery.SchemaField('cod_estagio_cartao', 'INTEGER', 'NULLABLE', description='Código do estágio do cartão.'),
    bigquery.SchemaField('des_estagio_cartao', 'STRING', 'NULLABLE', description='Descrição do estágio do cartão.'),
    bigquery.SchemaField('dth_estagio_cartao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da alteração do estágio do cartão.'),
    bigquery.SchemaField('flg_embs_loja', 'STRING', 'NULLABLE', description='Embossing na loja (S/N).'),
    bigquery.SchemaField('flg_cartao_cancelado', 'STRING', 'NULLABLE', description='Cartão cancelado (S/N).'),
    bigquery.SchemaField('flg_cartao_provisorio', 'STRING', 'NULLABLE', description='Cartão provisório (S/N).'),
    bigquery.SchemaField('flg_conta_cancelada', 'STRING', 'NULLABLE', description='Conta cancelada (S/N).'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última atualização no sistema.'),
    bigquery.SchemaField('num_seq_ult_alteracao', 'INTEGER', 'NULLABLE', description='Número sequencial da última alteração.'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE', description='Data e hora de inclusão do registro.'),
    bigquery.SchemaField('num_anomes_emis_cartao', 'DATE', 'NULLABLE', description='Ano e mês da emissão do cartão.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_acordo
cobranca_acordo = [
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE', description='ID único do acordo de cobrança.'),
    bigquery.SchemaField('id_cliente_externo', 'INTEGER', 'NULLABLE', description='ID do cliente na base externa.'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE', description='CPF ou CNPJ do cliente.'),
    bigquery.SchemaField('id_cobrador', 'STRING', 'NULLABLE', description='ID do cobrador.'),
    bigquery.SchemaField('nom_cobrador', 'STRING', 'NULLABLE', description='Nome do cobrador.'),
    bigquery.SchemaField('tip_modalidade_acordo', 'STRING', 'NULLABLE', description='Tipo de modalidade do acordo.'),
    bigquery.SchemaField('num_acordo', 'INTEGER', 'NULLABLE', description='Número do acordo.'),
    bigquery.SchemaField('num_parcelas', 'INTEGER', 'NULLABLE', description='Número de parcelas do acordo.'),
    bigquery.SchemaField('dat_operacao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da operação do acordo.'),
    bigquery.SchemaField('dat_emissao', 'TIMESTAMP', 'NULLABLE', description='Data e hora de emissão do acordo.'),
    bigquery.SchemaField('dth_processamento', 'TIMESTAMP', 'NULLABLE', description='Data e hora do processamento do acordo.'),
    bigquery.SchemaField('dth_inclusao_origem', 'TIMESTAMP', 'NULLABLE', description='Data e hora de inclusão na origem.'),
    bigquery.SchemaField('dth_alteracao_origem', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última alteração na origem.'),
    bigquery.SchemaField('dat_vencimento', 'DATE', 'NULLABLE', description='Data de vencimento do acordo.'),
    bigquery.SchemaField('ind_situacao', 'STRING', 'NULLABLE', description='Situação do acordo.'),
    bigquery.SchemaField('val_taxa_operacao', 'NUMERIC', 'NULLABLE', description='Valor da taxa da operação.'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE', description='Valor principal do acordo.'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE', description='Valor dos juros.'),
    bigquery.SchemaField('val_atributo', 'NUMERIC', 'NULLABLE', description='Valor do atributo.'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE', description='Valor total do acordo.'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE', description='Valor do desconto.'),
    bigquery.SchemaField('val_saldo_principal', 'NUMERIC', 'NULLABLE', description='Saldo do principal.'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE', description='Saldo total.'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE', description='Saldo atual.'),
    bigquery.SchemaField('qtd_dias_atraso', 'INTEGER', 'NULLABLE', description='Quantidade de dias em atraso.'),
    bigquery.SchemaField('dat_atraso_orig_acordo', 'DATE', 'NULLABLE', description='Data do atraso original do acordo.'),
    bigquery.SchemaField('id_acordo_usuario', 'INTEGER', 'NULLABLE', description='ID do usuário que criou o acordo.'),
    bigquery.SchemaField('nom_acordo_usuario', 'STRING', 'NULLABLE', description='Nome do usuário que criou o acordo.'),
    bigquery.SchemaField('id_acordo_assessoria', 'INTEGER', 'NULLABLE', description='ID da assessoria envolvida no acordo.'),
    bigquery.SchemaField('nom_acordo_assessoria', 'STRING', 'NULLABLE', description='Nome da assessoria envolvida no acordo.'),
    bigquery.SchemaField('id_acordo_negociacao', 'INTEGER', 'NULLABLE', description='ID da negociação do acordo.'),
    bigquery.SchemaField('nom_acordo_negociacao', 'STRING', 'NULLABLE', description='Nome da negociação do acordo.'),
    bigquery.SchemaField('tip_acordo_meio_pagto', 'STRING', 'NULLABLE', description='Tipo de meio de pagamento do acordo.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_assessoria
cobranca_assessoria = [
    bigquery.SchemaField('id_assessoria', 'STRING', 'NULLABLE', description='ID da assessoria.'),
    bigquery.SchemaField('nom_assessoria', 'STRING', 'NULLABLE', description='Nome da assessoria.'),
    bigquery.SchemaField('id_cliente_cobranca', 'STRING', 'NULLABLE', description='ID do cliente em cobrança.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_campo_customizavel
cobranca_campo_customizavel = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE', description='ID do cliente em cobrança.'),
    bigquery.SchemaField('nom_campo', 'STRING', 'NULLABLE', description='Nome do campo customizável.'),
    bigquery.SchemaField('val_campo', 'STRING', 'NULLABLE', description='Valor do campo customizável.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_cliente
cobranca_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE', description='ID único do cliente em cobrança.'),
    bigquery.SchemaField('id_cliente_externo', 'STRING', 'NULLABLE', description='ID do cliente na base externa.'),
    bigquery.SchemaField('tip_pessoa', 'STRING', 'NULLABLE', description='Tipo de pessoa (física ou jurídica).'),
    bigquery.SchemaField('tip_situacao', 'STRING', 'NULLABLE', description='Situação do cliente.'),
    bigquery.SchemaField('nom_cliente', 'STRING', 'NULLABLE', description='Nome do cliente.'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE', description='CPF ou CNPJ do cliente.'),
    bigquery.SchemaField('nom_uf', 'STRING', 'NULLABLE', description='UF do cliente.'),
    bigquery.SchemaField('cod_rating', 'STRING', 'NULLABLE', description='Código de rating do cliente.'),
    bigquery.SchemaField('des_marcador', 'STRING', 'NULLABLE', description='Descrição do marcador.'),
    bigquery.SchemaField('num_dias_maior_atraso', 'INTEGER', 'NULLABLE', description='Número de dias do maior atraso.'),
    bigquery.SchemaField('dat_maior_atraso', 'TIMESTAMP', 'NULLABLE', description='Data e hora do maior atraso.'),
    bigquery.SchemaField('val_saldo_atraso', 'NUMERIC', 'NULLABLE', description='Valor do saldo em atraso.'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE', description='Valor do saldo atual.'),
    bigquery.SchemaField('val_saldo_contabil', 'NUMERIC', 'NULLABLE', description='Valor do saldo contábil.'),
    bigquery.SchemaField('val_saldo_provisao', 'NUMERIC', 'NULLABLE', description='Valor do saldo de provisão.'),
    bigquery.SchemaField('qtd_dias_atraso', 'INTEGER', 'NULLABLE', description='Quantidade de dias em atraso.'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE', description='Valor total do saldo.'),
    bigquery.SchemaField('val_saldo_total_atraso', 'NUMERIC', 'NULLABLE', description='Valor total do saldo em atraso.'),
    bigquery.SchemaField('dth_modificacao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última modificação.'),
    bigquery.SchemaField('num_ddd_cel', 'INTEGER', 'NULLABLE', description='DDD do celular.'),
    bigquery.SchemaField('num_tel_cel', 'INTEGER', 'NULLABLE', description='Número do celular.'),
    bigquery.SchemaField('num_ddd_res', 'INTEGER', 'NULLABLE', description='DDD do residencial.'),
    bigquery.SchemaField('num_tel_res', 'INTEGER', 'NULLABLE', description='Número do residencial.'),
    bigquery.SchemaField('num_ddd_com', 'INTEGER', 'NULLABLE', description='DDD do comercial.'),
    bigquery.SchemaField('num_tel_com', 'INTEGER', 'NULLABLE', description='Número do comercial.'),
    bigquery.SchemaField('nom_email', 'STRING', 'NULLABLE', description='Email.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_email_cliente
cobranca_email_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE', description='ID do cliente em cobrança.'),
    bigquery.SchemaField('nom_email', 'STRING', 'NULLABLE', description='Email do cliente.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_endereco_cliente
cobranca_endereco_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE', description='ID do cliente em cobrança.'),
    bigquery.SchemaField('id_cliente_externo', 'STRING', 'NULLABLE', description='ID do cliente na base externa.'),
    bigquery.SchemaField('id_endereco_cobranca', 'INTEGER', 'NULLABLE', description='ID do endereço de cobrança.'),
    bigquery.SchemaField('tip_endereco_princ', 'BOOLEAN', 'NULLABLE', description='Endereço principal (true/false).'),
    bigquery.SchemaField('nom_logradouro', 'STRING', 'NULLABLE', description='Nome do logradouro.'),
    bigquery.SchemaField('num_logradouro', 'STRING', 'NULLABLE', description='Número do logradouro.'),
    bigquery.SchemaField('nom_complemento', 'STRING', 'NULLABLE', description='Complemento do endereço.'),
    bigquery.SchemaField('num_cep', 'INTEGER', 'NULLABLE', description='CEP.'),
    bigquery.SchemaField('nom_bairro', 'STRING', 'NULLABLE', description='Nome do bairro.'),
    bigquery.SchemaField('nom_cidade', 'STRING', 'NULLABLE', description='Nome da cidade.'),
    bigquery.SchemaField('nom_uf', 'STRING', 'NULLABLE', description='Sigla da UF.'),
    bigquery.SchemaField('ind_tipo', 'STRING', 'NULLABLE', description='Tipo de endereço.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_liquidacao_parc_acordo
cobranca_liquidacao_parc_acordo = [
    bigquery.SchemaField('id_liqd_parc_acordo', 'INTEGER', 'NULLABLE', description='ID da liquidação da parcela do acordo.'),
    bigquery.SchemaField('id_parcela_acordo', 'INTEGER', 'NULLABLE', description='ID da parcela do acordo.'),
    bigquery.SchemaField('num_parcela_acordo', 'INTEGER', 'NULLABLE', description='Número da parcela do acordo.'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE', description='Valor principal da parcela.'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE', description='Valor total da parcela.'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE', description='Valor dos juros da parcela.'),
    bigquery.SchemaField('val_encargos', 'NUMERIC', 'NULLABLE', description='Valor dos encargos da parcela.'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE', description='Valor do desconto na parcela.'),
    bigquery.SchemaField('val_distorcao', 'NUMERIC', 'NULLABLE', description='Valor da distorção.'),
    bigquery.SchemaField('ind_tipo_liqd', 'STRING', 'NULLABLE', description='Tipo de liquidação.'),
    bigquery.SchemaField('id_pagto_acordo', 'INTEGER', 'NULLABLE', description='ID do pagamento do acordo.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_origem_acordo
cobranca_origem_acordo = [
    bigquery.SchemaField('id_origem_acordo', 'STRING', 'NULLABLE', description='ID da origem do acordo.'),
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE', description='ID do acordo de cobrança.'),
    bigquery.SchemaField('num_contrato', 'STRING', 'NULLABLE', description='Número do contrato.'),
    bigquery.SchemaField('num_ordem_contrato', 'STRING', 'NULLABLE', description='Número da ordem do contrato.'),
    bigquery.SchemaField('id_parcela', 'STRING', 'NULLABLE', description='ID da parcela.'),
    bigquery.SchemaField('num_parcela', 'INTEGER', 'NULLABLE', description='Número da parcela.'),
    bigquery.SchemaField('dat_vencimento', 'TIMESTAMP', 'NULLABLE', description='Data e hora do vencimento.'),
    bigquery.SchemaField('id_situacao', 'STRING', 'NULLABLE', description='ID da situação.'),
    bigquery.SchemaField('qtd_dias_atr_cont', 'INTEGER', 'NULLABLE', description='Quantidade de dias em atraso.'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE', description='Valor principal.'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE', description='Valor total.'),
    bigquery.SchemaField('val_permanencia', 'NUMERIC', 'NULLABLE', description='Valor de permanência.'),
    bigquery.SchemaField('val_multa', 'NUMERIC', 'NULLABLE', description='Valor da multa.'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE', description='Valor dos juros.'),
    bigquery.SchemaField('val_tarifa', 'NUMERIC', 'NULLABLE', description='Valor da tarifa.'),
    bigquery.SchemaField('val_adicionado', 'NUMERIC', 'NULLABLE', description='Valor adicionado.'),
    bigquery.SchemaField('val_atual', 'NUMERIC', 'NULLABLE', description='Valor atual.'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE', description='Valor do desconto.'),
    bigquery.SchemaField('val_desc_principal', 'NUMERIC', 'NULLABLE', description='Valor do desconto no principal.'),
    bigquery.SchemaField('val_desc_juros', 'NUMERIC', 'NULLABLE', description='Valor do desconto nos juros.'),
    bigquery.SchemaField('val_desc_multa', 'NUMERIC', 'NULLABLE', description='Valor do desconto na multa.'),
    bigquery.SchemaField('val_desc_permanencia', 'NUMERIC', 'NULLABLE', description='Valor do desconto na permanência.'),
    bigquery.SchemaField('val_desconto_total', 'NUMERIC', 'NULLABLE', description='Valor total do desconto.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_pagamento_acordo
cobranca_pagamento_acordo = [
    bigquery.SchemaField('id_pagto_acordo', 'INTEGER', 'NULLABLE', description='ID do pagamento do acordo.'),
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE', description='ID do acordo de cobrança.'),
    bigquery.SchemaField('dat_processamento', 'TIMESTAMP', 'NULLABLE', description='Data e hora do processamento do pagamento.'),
    bigquery.SchemaField('dat_liquidacao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da liquidação do pagamento.'),
    bigquery.SchemaField('dat_credito', 'TIMESTAMP', 'NULLABLE', description='Data e hora do crédito do pagamento.'),
    bigquery.SchemaField('dat_cnab', 'TIMESTAMP', 'NULLABLE', description='Data e hora do registro no CNAB.'),
    bigquery.SchemaField('dat_operacao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da operação do pagamento.'),
    bigquery.SchemaField('dth_horainclusao', 'TIMESTAMP', 'NULLABLE', description='Data e hora de inclusão do registro.'),
    bigquery.SchemaField('ind_forma_liquidacao', 'STRING', 'NULLABLE', description='Forma de liquidação.'),
    bigquery.SchemaField('val_recebido', 'NUMERIC', 'NULLABLE', description='Valor recebido.'),
    bigquery.SchemaField('val_desconto', 'NUMERIC', 'NULLABLE', description='Valor do desconto.'),
    bigquery.SchemaField('val_encargos', 'NUMERIC', 'NULLABLE', description='Valor dos encargos.'),
    bigquery.SchemaField('val_distorcao', 'NUMERIC', 'NULLABLE', description='Valor da distorção.'),
    bigquery.SchemaField('ind_situacao', 'STRING', 'NULLABLE', description='Situação do pagamento.'),
    bigquery.SchemaField('ind_integracao', 'STRING', 'NULLABLE', description='Integração.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_parcela_acordo
cobranca_parcela_acordo = [
    bigquery.SchemaField('id_parcela_acordo', 'INTEGER', 'NULLABLE', description='ID da parcela do acordo.'),
    bigquery.SchemaField('id_acordo_cobranca', 'INTEGER', 'NULLABLE', description='ID do acordo de cobrança.'),
    bigquery.SchemaField('num_parcela_acordo', 'INTEGER', 'NULLABLE', description='Número da parcela do acordo.'),
    bigquery.SchemaField('dat_vencimento', 'TIMESTAMP', 'NULLABLE', description='Data e hora do vencimento.'),
    bigquery.SchemaField('ind_situacao', 'STRING', 'NULLABLE', description='Situação da parcela.'),
    bigquery.SchemaField('num_nossonumero', 'STRING', 'NULLABLE', description='Nosso número.'),
    bigquery.SchemaField('val_principal', 'NUMERIC', 'NULLABLE', description='Valor principal.'),
    bigquery.SchemaField('val_juros', 'NUMERIC', 'NULLABLE', description='Valor dos juros.'),
    bigquery.SchemaField('val_tarifa', 'NUMERIC', 'NULLABLE', description='Valor da tarifa.'),
    bigquery.SchemaField('val_adicionado', 'NUMERIC', 'NULLABLE', description='Valor adicionado.'),
    bigquery.SchemaField('val_total', 'NUMERIC', 'NULLABLE', description='Valor total.'),
    bigquery.SchemaField('val_tributo', 'NUMERIC', 'NULLABLE', description='Valor do tributo.'),
    bigquery.SchemaField('val_base_tributo', 'NUMERIC', 'NULLABLE', description='Valor da base do tributo.'),
    bigquery.SchemaField('val_permanencia', 'NUMERIC', 'NULLABLE', description='Valor de permanência.'),
    bigquery.SchemaField('val_saldo_principal', 'NUMERIC', 'NULLABLE', description='Saldo do principal.'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE', description='Saldo total.'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE', description='Saldo atual.'),
    bigquery.SchemaField('ind_registrado', 'STRING', 'NULLABLE', description='Registrado (S/N).'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_telefone
cobranca_telefone = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE', description='ID do cliente em cobrança.'),
    bigquery.SchemaField('id_telefone_cobranca', 'INTEGER', 'NULLABLE', description='ID do telefone em cobrança.'),
    bigquery.SchemaField('id_telefone_externo', 'INTEGER', 'NULLABLE', description='ID do telefone externo.'),
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE', description='CPF ou CNPJ do cliente.'),
    bigquery.SchemaField('num_ddd', 'INTEGER', 'NULLABLE', description='DDD.'),
    bigquery.SchemaField('num_telefone', 'INTEGER', 'NULLABLE', description='Número do telefone.'),
    bigquery.SchemaField('tip_telefone', 'STRING', 'NULLABLE', description='Tipo de telefone.'),
    bigquery.SchemaField('flg_principal', 'STRING', 'NULLABLE', description='Telefone principal (S/N).'),
    bigquery.SchemaField('des_obsercacao', 'STRING', 'NULLABLE', description='Observação.'),
    bigquery.SchemaField('num_ranking', 'INTEGER', 'NULLABLE', description='Ranking.'),
    bigquery.SchemaField('dat_modificacao', 'INTEGER', 'NULLABLE', description='Data da modificação.'),
    bigquery.SchemaField('dat_inclusao_reg', 'INTEGER', 'NULLABLE', description='Data de inclusão do registro.')
]

# Dataset: pfs_risco_tivea, Table: cobranca_telefone_cliente
cobranca_telefone_cliente = [
    bigquery.SchemaField('id_cliente_cobranca', 'INTEGER', 'NULLABLE', description='ID do cliente em cobrança.'),
    bigquery.SchemaField('num_ddd_celular', 'INTEGER', 'NULLABLE', description='DDD do celular.'),
    bigquery.SchemaField('num_tel_celular', 'INTEGER', 'NULLABLE', description='Número do celular.'),
    bigquery.SchemaField('num_ddd_residencial', 'INTEGER', 'NULLABLE', description='DDD do residencial.'),
    bigquery.SchemaField('num_tel_residencial', 'INTEGER', 'NULLABLE', description='Número do residencial.'),
    bigquery.SchemaField('num_ddd_comercial', 'INTEGER', 'NULLABLE', description='DDD do comercial.'),
    bigquery.SchemaField('num_tel_comercial', 'INTEGER', 'NULLABLE', description='Número do comercial.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: cobr_cliente_atraso
cobr_cliente_atraso = [
    bigquery.SchemaField('num_cpf_cnpj_cliente', 'INTEGER', 'NULLABLE', description='CPF ou CNPJ do cliente.'),
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE', description='ID da conta do cliente.'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE', description='ID do cliente no sistema.'),
    bigquery.SchemaField('num_cartao', 'STRING', 'NULLABLE', description='Número do cartão do cliente (se aplicável).'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE', description='ID do produto do cartão (se aplicável).'),
    bigquery.SchemaField('nom_cliente', 'STRING', 'NULLABLE', description='Nome do cliente.'),
    bigquery.SchemaField('tip_pessoa', 'STRING', 'NULLABLE', description='Tipo de pessoa (física ou jurídica).'),
    bigquery.SchemaField('tip_situacao', 'STRING', 'NULLABLE', description='Situação do cliente (ex: ativo, inativo).'),
    bigquery.SchemaField('nom_uf', 'STRING', 'NULLABLE', description='UF do cliente.'),
    bigquery.SchemaField('cod_rating', 'STRING', 'NULLABLE', description='Código de rating de crédito do cliente.'),
    bigquery.SchemaField('des_marcador', 'STRING', 'NULLABLE', description='Descrição do marcador do cliente.'),
    bigquery.SchemaField('val_saldo_atual', 'NUMERIC', 'NULLABLE', description='Valor do saldo atual da conta.'),
    bigquery.SchemaField('val_saldo_atraso', 'NUMERIC', 'NULLABLE', description='Valor do saldo em atraso.'),
    bigquery.SchemaField('val_saldo_contabil', 'NUMERIC', 'NULLABLE', description='Valor do saldo contábil.'),
    bigquery.SchemaField('val_saldo_provisao', 'NUMERIC', 'NULLABLE', description='Valor do saldo de provisão.'),
    bigquery.SchemaField('val_saldo_total', 'NUMERIC', 'NULLABLE', description='Valor total do saldo.'),
    bigquery.SchemaField('val_saldo_total_atraso', 'NUMERIC', 'NULLABLE', description='Valor total do saldo em atraso.'),
    bigquery.SchemaField('qtd_dias_atraso', 'INTEGER', 'NULLABLE', description='Quantidade de dias em atraso.'),
    bigquery.SchemaField('qtd_parcela_aberta', 'INTEGER', 'NULLABLE', description='Quantidade de parcelas abertas.'),
    bigquery.SchemaField('dth_modificacao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última modificação no registro.'),
    bigquery.SchemaField('nom_assessoria', 'STRING', 'NULLABLE', description='Nome da assessoria responsável (se aplicável).'),
    bigquery.SchemaField('num_ddd_cel', 'INTEGER', 'NULLABLE', description='DDD do telefone celular.'),
    bigquery.SchemaField('num_tel_cel', 'INTEGER', 'NULLABLE', description='Número do telefone celular.'),
    bigquery.SchemaField('num_ddd_res', 'INTEGER', 'NULLABLE', description='DDD do telefone residencial.'),
    bigquery.SchemaField('num_tel_res', 'INTEGER', 'NULLABLE', description='Número do telefone residencial.'),
    bigquery.SchemaField('num_ddd_com', 'INTEGER', 'NULLABLE', description='DDD do telefone comercial.'),
    bigquery.SchemaField('num_tel_com', 'INTEGER', 'NULLABLE', description='Número do telefone comercial.'),
    bigquery.SchemaField('nom_email', 'STRING', 'NULLABLE', description='Email do cliente.'),
    bigquery.SchemaField('cod_loja', 'STRING', 'NULLABLE', description='Código da loja.'),
    bigquery.SchemaField('cod_colmar', 'STRING', 'NULLABLE', description='Código Colmar.'),
    bigquery.SchemaField('cod_colchao', 'STRING', 'NULLABLE', description='Código Colchão.'),
    bigquery.SchemaField('cod_contr_orig', 'STRING', 'NULLABLE', description='Código do contrato original.'),
    bigquery.SchemaField('cod_dist_assessoria', 'STRING', 'NULLABLE', description='Código de distribuição da assessoria.'),
    bigquery.SchemaField('cod_dist_assess_mar', 'STRING', 'NULLABLE', description='Código de distribuição da assessoria e marcador.'),
    bigquery.SchemaField('cod_dist_escob', 'STRING', 'NULLABLE', description='Código de distribuição da equipe de cobrança.'),
    bigquery.SchemaField('cod_estrategia1', 'STRING', 'NULLABLE', description='Código da estratégia 1.'),
    bigquery.SchemaField('cod_estrategia2', 'STRING', 'NULLABLE', description='Código da estratégia 2.'),
    bigquery.SchemaField('cod_estrategia3', 'STRING', 'NULLABLE', description='Código da estratégia 3.'),
    bigquery.SchemaField('cod_estrategia4', 'STRING', 'NULLABLE', description='Código da estratégia 4.'),
    bigquery.SchemaField('cod_estrategia5', 'STRING', 'NULLABLE', description='Código da estratégia 5.'),
    bigquery.SchemaField('cod_fpd', 'STRING', 'NULLABLE', description='Código FPD.'),
    bigquery.SchemaField('cod_var_aux', 'STRING', 'NULLABLE', description='Código da variável auxiliar.'),
    bigquery.SchemaField('cod_faixa_atraso_b', 'STRING', 'NULLABLE', description='Código da faixa de atraso B.'),
    bigquery.SchemaField('dat_referencia', 'DATE', 'NULLABLE', description='Data de referência.')
]

# Dataset: pfs_risco_tivea, Table: conta
conta = [
    bigquery.SchemaField('id_conta', 'INTEGER', 'NULLABLE', description='ID único da conta.'),
    bigquery.SchemaField('id_produto_cartao', 'INTEGER', 'NULLABLE', description='ID do produto do cartão associado à conta.'),
    bigquery.SchemaField('tip_produto', 'STRING', 'NULLABLE', description='Tipo de produto (ex: cartão de crédito).'),
    bigquery.SchemaField('num_cpf_cliente', 'INTEGER', 'NULLABLE', description='CPF do cliente titular da conta.'),
    bigquery.SchemaField('cod_loja_ads_conta', 'INTEGER', 'NULLABLE', description='Código da loja onde a conta foi aberta.'),
    bigquery.SchemaField('nom_canal_ads_conta', 'STRING', 'NULLABLE', description='Nome do canal de aquisição da conta (ex: agência, internet).'),
    bigquery.SchemaField('nom_politica', 'STRING', 'NULLABLE', description='Nome da política de risco aplicada à conta.'),
    bigquery.SchemaField('nom_mod_score', 'STRING', 'NULLABLE', description='Nome do modelo de score utilizado na aprovação da conta.'),
    bigquery.SchemaField('val_score_aprov_conta', 'INTEGER', 'NULLABLE', description='Pontuação do score na aprovação da conta.'),
    bigquery.SchemaField('cod_operacao_proposta_so', 'STRING', 'NULLABLE', description='Código da operação da proposta no sistema.'),
    bigquery.SchemaField('id_proposta', 'INTEGER', 'NULLABLE', description='ID da proposta de abertura da conta.'),
    bigquery.SchemaField('nom_colab_proposta', 'STRING', 'NULLABLE', description='Nome do colaborador que propôs a conta.'),
    bigquery.SchemaField('id_chapa_colab_proposta', 'STRING', 'NULLABLE', description='ID da chapa do colaborador que propôs a conta.'),
    bigquery.SchemaField('des_origem_entrada_proposta', 'STRING', 'NULLABLE', description='Descrição da origem da proposta da conta.'),
    bigquery.SchemaField('id_cliente_so', 'INTEGER', 'NULLABLE', description='ID do cliente no sistema.'),
    bigquery.SchemaField('id_ori_comercial', 'INTEGER', 'NULLABLE', description='ID da origem comercial da conta.'),
    bigquery.SchemaField('dth_ads_conta', 'TIMESTAMP', 'NULLABLE', description='Data e hora de adesão à conta.'),
    bigquery.SchemaField('dth_prim_ads_conta', 'TIMESTAMP', 'NULLABLE', description='Data e hora da primeira adesão à conta.'),
    bigquery.SchemaField('dth_prim_ads_cred', 'TIMESTAMP', 'NULLABLE', description='Data e hora da primeira adesão ao crédito.'),
    bigquery.SchemaField('cod_sit_conta', 'INTEGER', 'NULLABLE', description='Código da situação da conta.'),
    bigquery.SchemaField('des_sit_conta', 'STRING', 'NULLABLE', description='Descrição da situação da conta.'),
    bigquery.SchemaField('dth_sit_conta', 'TIMESTAMP', 'NULLABLE', description='Data e hora da alteração da situação da conta.'),
    bigquery.SchemaField('num_dia_vencto_fatura', 'INTEGER', 'NULLABLE', description='Dia do mês de vencimento da fatura.'),
    bigquery.SchemaField('dth_prox_vencto_real', 'TIMESTAMP', 'NULLABLE', description='Data e hora do próximo vencimento real.'),
    bigquery.SchemaField('dth_prox_vencto_padrao', 'TIMESTAMP', 'NULLABLE', description='Data e hora do próximo vencimento padrão.'),
    bigquery.SchemaField('dth_ult_alt_vencto', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última alteração do vencimento.'),
    bigquery.SchemaField('flg_conta_bloqueada', 'STRING', 'NULLABLE', description='Conta bloqueada (S/N).'),
    bigquery.SchemaField('flg_conta_cancelada', 'STRING', 'NULLABLE', description='Conta cancelada (S/N).'),
    bigquery.SchemaField('id_produto_cartao_ant', 'INTEGER', 'NULLABLE', description='ID do produto do cartão anterior.'),
    bigquery.SchemaField('dth_ult_grade_produto_cartao', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última atualização da grade de produtos do cartão.'),
    bigquery.SchemaField('cod_banco', 'INTEGER', 'NULLABLE', description='Código do banco.'),
    bigquery.SchemaField('cod_agencia', 'INTEGER', 'NULLABLE', description='Código da agência.'),
    bigquery.SchemaField('dv_agencia', 'INTEGER', 'NULLABLE', description='Dígito verificador da agência.'),
    bigquery.SchemaField('cod_conta_corrente', 'STRING', 'NULLABLE', description='Número da conta corrente.'),
    bigquery.SchemaField('dv_conta_corrente', 'STRING', 'NULLABLE', description='Dígito verificador da conta corrente.'),
    bigquery.SchemaField('dth_adesao_prod_flex', 'TIMESTAMP', 'NULLABLE', description='Data e hora da adesão ao produto flex.'),
    bigquery.SchemaField('dth_cancel_adesao_prod_flex', 'TIMESTAMP', 'NULLABLE', description='Data e hora do cancelamento da adesão ao produto flex.'),
    bigquery.SchemaField('id_adesao_carteira_digital_so', 'INTEGER', 'NULLABLE', description='ID da adesão à carteira digital no sistema.'),
    bigquery.SchemaField('dt_adesao_carteira_digital', 'TIMESTAMP', 'NULLABLE', description='Data e hora da adesão à carteira digital.'),
    bigquery.SchemaField('dt_cancelamento_carteira_digital', 'TIMESTAMP', 'NULLABLE', description='Data e hora do cancelamento da carteira digital.'),
    bigquery.SchemaField('nm_usr_adesao_carteira_digital', 'STRING', 'NULLABLE', description='Nome do usuário que fez a adesão à carteira digital.'),
    bigquery.SchemaField('nm_usr_cancelamento_carteira_digital', 'STRING', 'NULLABLE', description='Nome do usuário que cancelou a carteira digital.'),
    bigquery.SchemaField('flg_overlimit_disp', 'STRING', 'NULLABLE', description='Overlimit disponível (S/N).'),
    bigquery.SchemaField('flg_indicacao_amigo_revendedor', 'STRING', 'NULLABLE', description='Indicado por amigo/revendedor (S/N).'),
    bigquery.SchemaField('flg_conta_revendedor', 'STRING', 'NULLABLE', description='Conta de revendedor (S/N).'),
    bigquery.SchemaField('num_cpf_indicador', 'INTEGER', 'NULLABLE', description='CPF do indicador.'),
    bigquery.SchemaField('dth_ult_atu_so', 'TIMESTAMP', 'NULLABLE', description='Data e hora da última atualização no sistema.'),
    bigquery.SchemaField('num_seq_ult_alteracao', 'INTEGER', 'NULLABLE', description='Número sequencial da última alteração.'),
    bigquery.SchemaField('dat_referencia', 'INTEGER', 'NULLABLE', description='Data de referência.'),
    bigquery.SchemaField('dth_inclusao_reg', 'TIMESTAMP', 'NULLABLE', description='Data e hora de inclusão do registro.'),
    bigquery.SchemaField('num_anomes_ads_conta', 'DATE', 'NULLABLE', description='Ano e mês de adesão à conta.')
]

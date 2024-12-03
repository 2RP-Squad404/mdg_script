from faker import Faker
from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')

def pfs_unificacao_pefisa(num_records):
    dados = {'produto_cartao': [], 'conta_debito': [], 'v_tipo_ajuste': [], 'boleto': [], 'seguro_parcela': [], 'v_produto_cartao': [], 'meta_dia_pfin': [], 'v_tipo_operacao': [], 'v_cota_produto_financeiro': [], 'evento_compra_saque': [], 'cartao_hist': [], 'v_status_autorizacao_evento_externo': [], 'grade_produto': [], 'cartao': [], 'conta': [], 'seguro_adesao': []}

    for _ in range(num_records):
        produto_cartao = {
            'nom_processadora': faker.company(),
            'nom_parceiro': faker.company(),
            'id_produto_cartao': faker.random_int(),
            'nom_produto_cartao': faker.word(),
            'id_band_produto_cartao': faker.random_int(),
            'des_band_produto_cartao': faker.word(),
            'num_bin': faker.random_number(digits=6),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
        }
        dados['produto_cartao'].append(produto_cartao)

        conta_debito = {
            'id_conta_multiplo': faker.random_int(),
            'id_produto_cartao': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11),
            'id_conta_debito_so': faker.random_int(),
            'dth_ads_conta_debito': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'des_sit_conta_debito': faker.word(),
            'cod_sit_conta_debito': faker.random_int(),
            'num_conta_corrente': faker.iban(),
            'dv_conta_corrente': faker.random_digit(),
            'cod_banco': faker.random_int(),
            'num_agencia_conta_corrente': faker.random_int(),
            'dv_agencia_conta_corrente': faker.random_digit(),
            'num_dia_vencimento': faker.random_int(min=1, max=31),
            'dth_prox_vencto_padrao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_prox_vencto_real': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'id_cliente_debito_so': faker.random_int(),
            'id_cliente_multiplo_so': faker.random_int(),
            'flg_conta_saldo_apartado': faker.random_element(elements=('S', 'N')),
            'id_pacote_tarifa_debito': faker.random_int(),
            'des_tipo_pacote_tarifa_debito': faker.word(),
            'des_pacote_tarifa_debito': faker.word(),
            'des_tipo_endereco_entrega': faker.word(),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'num_anomes_ads_conta_debito': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['conta_debito'].append(conta_debito)

        v_tipo_ajuste = {
            'hash_key': faker.uuid4(),
            'ta_id_ajuste': faker.random_int(),
            'ta_descricao': faker.sentence(),
            'ta_flagcredito': faker.boolean(),
            'ta_flagtransacaodisputa': faker.boolean(),
            'ta_flagpagamentolojista': faker.boolean(),
            'ta_toleranciavalorminimoextrato': faker.pyfloat(),
            'ta_flagsistema': faker.random_int(),
            'ta_tipoeventoexternooriginal': faker.word(),
            'dh_relatorio': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'operation': faker.word(),
            'operation_sequence': faker.random_int(),
            'production_date': faker.date_this_decade().strftime('%Y-%m-%d'),
            'seq': faker.random_int()
        }
        dados['v_tipo_ajuste'].append(v_tipo_ajuste)

        boleto = {
            'id_boleto': str(faker.random_int()),
            'id_conta': faker.random_int(),
            'id_produto_conta': faker.random_int(),
            'id_tipo_boleto': faker.random_int(),
            'des_tipo_boleto': faker.word(),
            'nro_nosso_numero': faker.random_number(digits=10),
            'dth_emissao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_vencimento': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'des_situacao_boleto': faker.word(),
            'des_sts_boleto': faker.word(),
            'val_boleto': faker.pyfloat(),
            'num_cpf_cliente': faker.random_number(digits=11),
            'id_cliente_so': faker.random_int(),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'des_origem': faker.word(),
            'num_anomes_emis_bol': faker.date_this_decade().strftime('%Y-%m-%d')

        }
        dados['boleto'].append(boleto)

        seguro_parcela = {
            'id_adesao_seguro': faker.random_int(),
            'id_produto_financeiro': faker.random_int(),
            'nom_produto_financeiro': faker.word(),
            'des_tip_origem_pfin': faker.word(),
            'num_parcela': faker.random_int(),
            'val_parcela': faker.pyfloat(),
            'dth_vencimento_parcela': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_tip_situacao': faker.random_int(),
            'des_tip_situacao': faker.word(),
            'dth_situacao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_emissao_parcela': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_cancelamento': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S') if faker.boolean() else None,
            'des_motivo_cancelamento': faker.word() if faker.boolean() else None,
            'cod_tip_situacao_cobranca': faker.random_int(),
            'des_tip_situacao_cobranca': faker.word(),
            'cod_tip_situacao_transferencia': faker.random_int(),
            'des_tip_situacao_transferencia': faker.word(),
            'dth_liquidacao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S') if faker.boolean() else None,
            'dth_real_liquidacao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S') if faker.boolean() else None,
            'dth_envio_cobranca': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S') if faker.boolean() else None,
            'dth_postagem_parcela': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S') if faker.boolean() else None,
            'num_cpf_cliente': faker.random_number(digits=11),
            'num_apolice_seguro': faker.bothify(text='??????????'),
            'cod_canal_venda': faker.random_int(),
            'des_canal_venda': faker.word(),
            'num_seq_recebe_bau': faker.random_int(),
            'num_serie_bau': faker.bothify(text='????????'),
            'num_carne_bau': faker.bothify(text='??????'),
            'ind_serie_pnb_bau': faker.random_element(elements=('S', 'N')),
            'tipo_operacao_bau': faker.word(),
            'nm_local_pagamento_bau': faker.word(),
            'cod_estabelecimento_lote': faker.random_int(),
            'nm_estabelecimento_lote': faker.word(),
            'tip_recebimento_lote': faker.word(),
            'dat_lote': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'num_lote': faker.random_int(),
            'num_seq_lote': faker.random_int(),
            'cod_operador': faker.bothify(text='??'),
            'num_bordero': faker.random_int(),
            'tip_negociacao': faker.random_int(),
            'dat_ano_mes_apuracao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_atualizacao_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'des_tip_origem_adesao': faker.word(),
            'cod_forma_pagto': faker.random_int(),
            'des_forma_pagto': faker.word(),
            'num_anomes_vencimento': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['seguro_parcela'].append(seguro_parcela)

        v_produto_cartao = {
            'id_produto_cartao': faker.random_int(),
            'nom_produto_cartao': faker.word(),
            'id_band_produto_cartao': faker.random_int(),
            'des_band_produto_cartao': faker.word(),
            'num_bin': faker.random_number(digits=6),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
        }
        dados['v_produto_cartao'].append(v_produto_cartao)

        meta_dia_pfin = {
            'dat_dia': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_estabelecimento': faker.random_int(),
            'cod_produto_financeiro': faker.random_int(),
            'qtd_prev_venda': faker.pyfloat(),
            'qtd_real_venda': faker.pyfloat(),
            'val_prev_venda': faker.pyfloat(),
            'val_real_venda': faker.pyfloat(),
            'qtd_prev_receb': faker.pyfloat(),
            'qtd_real_receb': faker.pyfloat(),
            'val_prev_receb': faker.pyfloat(),
            'val_real_receb': faker.pyfloat(),
            'per_prev_receb': faker.pyfloat(),
            'per_real_receb': faker.pyfloat(),
            'per_real_receb_acm': faker.pyfloat(),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['meta_dia_pfin'].append(meta_dia_pfin)

        v_tipo_operacao = {
            'hash_key': faker.uuid4(),
            'tos_id_operacao': faker.random_int(),
            'tos_nomeoperacao': faker.word(),
            'tos_descricaooperacao': faker.sentence(),
            'tos_id_emissor': faker.random_int(),
            'tos_remuneracaoemissor': faker.pyfloat(),
            'tos_condicionadorliquidacao': faker.random_int(),
            'tos_tipoliquidacao': faker.random_int(),
            'tos_dataliquidacao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'tos_tipodebito': faker.random_int(),
            'tos_tipocontrato': faker.random_int(),
            'tos_tipocalculoprestacao': faker.random_int(),
            'tos_flagrefinanciamento': faker.boolean(),
            'tos_tipopagamento': faker.random_int(),
            'tos_parcelasdefault': faker.random_int(),
            'tos_id_tabela': faker.random_int(),
            'tos_valoroperacao': faker.pyfloat(),
            'tos_quantidadeparcelas': faker.random_int(),
            'tos_valorparcela': faker.pyfloat(),
            'tos_tipocompra': faker.random_int(),
            'tos_id_credordefault': faker.random_int(),
            'tos_flagcobraprorata': faker.boolean(),
            'tos_diasafastamento': faker.random_int(),
            'tos_remuneracaoemissorperc': faker.pyfloat(),
            'tos_remuneracaoemissorfixa': faker.pyfloat(),
            'tos_definicaocondicao': faker.word(),
            'tos_financiavel': faker.random_int(),
            'tos_tipotransacaoajuste': faker.random_int(),
            'tos_tipooperacao': faker.word(),
            'tos_tipoplano': faker.word(),
            'tos_flagjuros': faker.boolean(),
            'tos_planominimo': faker.random_int(),
            'tos_planomaximo': faker.random_int(),
            'tos_valorminimo': faker.pyfloat(),
            'tos_valormaximo': faker.pyfloat(),
            'tos_excedentepermitido': faker.pyfloat(),
            'tos_tipoexcedentepermitido': faker.word(),
            'tos_id_tabelajuros': faker.random_int(),
            'tos_flagposproximovencimento': faker.random_int(),
            'tos_codproccancelamento': faker.bothify(text='??'),
            'tos_toleranciavalorminimoextrato': faker.pyfloat(),
            'tos_flagparcelado': faker.boolean(),
            'tos_codigoarquivoseguro': faker.random_int(),
            'tos_valortac': faker.pyfloat(),
            'tos_percentualtac': faker.pyfloat(),
            'tos_flagcredito': faker.random_int(),
            'tos_taxajuros': faker.pyfloat(),
            'tos_flagcobratarifa': faker.boolean(),
            'tos_codigoprocessamento': faker.bothify(text='??'),
            'tos_id_grupostransacoeslojista': faker.random_int(),
            'tos_percentualdeflacao': faker.pyfloat(),
            'tos_id_operacaoorigem': faker.random_int(),
            'tos_flagverenderecobloq': faker.boolean(),
            'tos_tarifa': faker.pyfloat(),
            'tos_flagplanospagamento': faker.random_int(),
            'tos_flagtiratac': faker.boolean(),
            'tos_regravalidacaosenha': faker.random_int(),
            'tos_regraoperacaodigitada': faker.random_int(),
            'tos_flagisentatarifa': faker.boolean(),
            'tos_descricaoabreviada': faker.word(),
            'tos_respeitavalidacaoregrasenha': faker.random_int(),
            'tos_flagposmobile': faker.boolean(),
            'tos_flagfinanciada': faker.boolean(),
            'tpo_id_tipooperacao': faker.uuid4(),
            'tpo_descricao': faker.sentence(),
            'tpo_operacaovisa': faker.boolean(),
            'dh_relatorio': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'operation': faker.word(),
            'operation_sequence': faker.random_int(),
            'production_date': faker.date_this_decade().strftime('%Y-%m-%d'),
            'seq': faker.random_int()
        }
        dados['v_tipo_operacao'].append(v_tipo_operacao)

        v_cota_produto_financeiro = {
            'dat_dia': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_estabelecimento': faker.random_int(),
            'nom_estabelecimento': faker.company(),
            'dat_inauguracao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'nom_fantasia_mkt': faker.company(),
            'cod_corporacao': faker.random_int(),
            'nom_razao_social': faker.company(),
            'cod_regional': faker.random_int(),
            'des_regional': faker.word(),
            'nom_gerente': faker.name(),
            'cod_micro_regiao': faker.random_int(),
            'des_micro_regiao': faker.word(),
            'cod_produto_financeiro': faker.random_int(),
            'des_produto_financeiro': faker.word(),
            'qtd_cota_venda': faker.pyfloat(),
            'val_cota_venda': faker.pyfloat(),
            'qtd_cota_recebimento': faker.pyfloat(),
            'val_cota_recebimento': faker.pyfloat(),
            'per_cota_recebimento': faker.pyfloat(),
            'per_cota_recb_acum': faker.pyfloat(),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
        }
        dados['v_cota_produto_financeiro'].append(v_cota_produto_financeiro)

        evento_compra_saque = {
            'id_evento_compra_saque': faker.random_int(),
            'id_cartao_credito_so': faker.random_int(),
            'des_funcao_cartao': faker.word(),
            'num_cartao_credito': faker.credit_card_number(),
            'id_conta_cartao_credito': faker.random_int(),
            'id_cliente_so': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11),
            'cod_tipo_operacao': faker.bothify(text='??'),
            'des_tipo_operacao': faker.word(),
            'id_estab_so': faker.random_int(),
            'cod_estab': faker.random_int(),
            'flg_trans_ofs': faker.random_element(elements=('S', 'N')),
            'cod_status': faker.random_int(),
            'des_status': faker.word(),
            'des_categoria_autorizacao': faker.word(),
            'dth_trans': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'val_trans': faker.pyfloat(),
            'qtd_parcela': faker.random_int(),
            'val_parcela': faker.pyfloat(),
            'cod_moeda': faker.random_int(),
            'des_moeda': faker.currency_code(),
            'per_taxa_juro': faker.pyfloat(),
            'val_trans_origem': faker.pyfloat(),
            'val_trans_destino': faker.pyfloat(),
            'cod_moeda_dest': faker.random_int(),
            'des_moeda_dest': faker.currency_code(),
            'cod_origem': faker.bothify(text='??'),
            'des_origem': faker.word(),
            'cod_ori_resolucao': faker.bothify(text='??'),
            'des_ori_resolucao': faker.word(),
            'id_estab_exter': faker.random_int(),
            'nom_estab_exter': faker.company(),
            'cod_tipo_estab_mcc': faker.random_int(),
            'des_tipo_estab_mcc': faker.word(),
            'dth_vencto_prim_par_ep': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_estimada_vencto_ult_par_ep': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'id_autorizacao': faker.random_int(),
            'cod_autorizacao': faker.bothify(text='??'),
            'val_tac': faker.pyfloat(),
            'val_iof': faker.pyfloat(),
            'val_juro': faker.pyfloat(),
            'val_financiado': faker.pyfloat(),
            'val_taxa': faker.pyfloat(),
            'dth_vencimento_padrao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'des_tipo_transacao': faker.word(),
            'des_origem_informacao': faker.word(),
            'id_evento_original': faker.random_int(),
            'id_transacao_uuid': faker.uuid4(),
            'cod_reference_number': faker.bothify(text='??'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'des_sistema_origem': faker.word(),
            'num_anomes_compra_saque': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['evento_compra_saque'].append(evento_compra_saque)

        cartao_hist = {
            'id_cartao': faker.random_int(),
            'id_produto_cartao': faker.random_int(),
            'num_cartao': faker.credit_card_number(),
            'num_seq_via_cartao': faker.random_int(),
            'des_modo_cartao': faker.word(),
            'flg_cartao_atual': faker.random_element(elements=('S', 'N')),
            'id_conta': faker.random_int(),
            'id_conta_debito': faker.random_int(),
            'id_produto_cartao_debito': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11),
            'cod_tip_portador': faker.random_int(),
            'num_bin': faker.random_number(digits=6),
            'cod_loja_emis_cartao': faker.random_int(),
            'id_cliente_so': faker.random_int(),
            'dth_emis_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_embs_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_valid_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_desbloqueio': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_sit_cartao': faker.random_int(),
            'des_sit_cartao': faker.word(),
            'dth_sit_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_agrp_sit_cartao': faker.random_int(),
            'des_agrp_sit_cartao': faker.word(),
            'cod_estagio_cartao': faker.random_int(),
            'des_estagio_cartao': faker.word(),
            'dth_estagio_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'flg_embs_loja': faker.random_element(elements=('S', 'N')),
            'flg_cartao_cancelado': faker.random_element(elements=('S', 'N')),
            'flg_cartao_provisorio': faker.random_element(elements=('S', 'N')),
            'flg_conta_cancelada': faker.random_element(elements=('S', 'N')),
            'flg_conta_debito_cancelada': faker.random_element(elements=('S', 'N')),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_anomes_emis_cartao': faker.random_int(),
            'pt_nomeplastico': faker.word(),
            'ca_arquivolote': faker.file_path(),
            'ca_id_imagem': faker.random_int(),
            'bc_responsavel': faker.name(),
            'ca_codigocancelamento': faker.bothify(text='??'),
            'ca_flaggeracartasenha': faker.random_int(),
            'pt_id_imagem': faker.random_int(),
            'id_cartao_hist_dock': faker.random_int(),
            'id_conta_hist_dock': faker.random_int(),
            'id_cliente_hist_dock': faker.random_int(),
            'flg_cartao_migrado': faker.random_element(elements=('S', 'N')),
            'dth_cartao_migrado': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'des_origem': faker.word(),
            'dat_referencia': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['cartao_hist'].append(cartao_hist)

        v_status_autorizacao_evento_externo = {
            'hash_key': faker.uuid4(),
            'sae_id_statusautorizacoeseventosexternos': faker.random_int(),
            'sae_status': faker.random_int(),
            'sae_descricao': faker.sentence(),
            'sae_flagpagamentovalidocorrespondente': faker.random_int(),
            'sae_flagpermitealteracaostatuscorrespondente': faker.random_int(),
            'sae_flagpermitecancelamentocorrespondente': faker.random_int(),
            'dh_relatorio': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'operation': faker.word(),
            'operation_sequence': faker.random_int(),
            'production_date': faker.date_this_decade().strftime('%Y-%m-%d'),
            'seq': faker.random_int()
        }
        dados['v_status_autorizacao_evento_externo'].append(v_status_autorizacao_evento_externo)

        grade_produto = {
            'id_grade_produto': str(faker.random_int()),
            'id_conta_cartao_credito': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11),
            'id_produto_ccred_origem': faker.random_int(),
            'id_produto_ccred_destino': faker.random_int(),
            'id_estabelecimento_grade': str(faker.random_int()),
            'nom_estabelecimento_grade': faker.company(),
            'id_chapa_colaborador_grade': str(faker.random_int()),
            'nom_colaborador_grade': faker.name(),
            'cod_status_grade_produto': faker.random_int(),
            'des_status_grade_produto': faker.word(),
            'dth_solicitacao_grade_produto': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_migracao_grade_produto': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'val_limite_anterior_ccred': faker.pyfloat(),
            'val_limite_novo_ccred': faker.pyfloat(),
            'flg_origem_web_service': faker.random_element(elements=('S', 'N')),
            'des_responsavel': faker.name(),
            'flg_grade_automatico': faker.random_element(elements=('S', 'N')),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'des_origem': faker.word(),
            'num_anomes_mig_grade': faker.date_this_decade().strftime('%Y-%m-%d'),
            'dat_referencia': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['grade_produto'].append(grade_produto)

        cartao = {
            'id_cartao': faker.random_int(),
            'id_produto_cartao': faker.random_int(),
            'num_cartao': faker.credit_card_number(),
            'num_seq_via_cartao': faker.random_int(),
            'des_modo_cartao': faker.word(),
            'flg_cartao_atual': faker.random_element(elements=('S', 'N')),
            'id_conta': faker.random_int(),
            'id_conta_debito': faker.random_int(),
            'id_produto_cartao_debito': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'cod_tip_portador': faker.random_int(),
            'num_bin': faker.random_number(digits=6, fix_len=True),
            'cod_loja_emis_cartao': faker.random_int(),
            'id_cliente_so': faker.random_int(),
            'dth_emis_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_embs_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_valid_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_desbloqueio': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_sit_cartao': faker.random_int(),
            'des_sit_cartao': faker.word(),
            'dth_sit_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_agrp_sit_cartao': faker.random_int(),
            'des_agrp_sit_cartao': faker.word(),
            'cod_estagio_cartao': faker.random_int(),
            'des_estagio_cartao': faker.word(),
            'dth_estagio_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'flg_embs_loja': faker.random_element(elements=('S', 'N')),
            'flg_cartao_cancelado': faker.random_element(elements=('S', 'N')),
            'flg_cartao_provisorio': faker.random_element(elements=('S', 'N')),
            'flg_conta_cancelada': faker.random_element(elements=('S', 'N')),
            'flg_conta_debito_cancelada': faker.random_element(elements=('S', 'N')),
            'pt_nomeplastico': faker.word(),
            'ca_arquivolote': faker.word(),
            'ca_id_imagem': faker.random_int(),
            'bc_responsavel': faker.word(),
            'ca_codigocancelamento': faker.word(),
            'ca_flaggeracartasenha': faker.random_int(),
            'pt_id_imagem': faker.random_int(),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'id_cartao_hist_dock': faker.random_int(),
            'id_conta_hist_dock': faker.random_int(),
            'id_cliente_hist_dock': faker.random_int(),
            'flg_cartao_migrado': faker.random_element(elements=('S', 'N')),
            'dth_cartao_migrado': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'des_origem': faker.word(),
            'num_anomes_emis_cartao': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['cartao'].append(cartao)

        conta = {
            'id_conta': faker.random_int(),
            'id_produto_cartao': faker.random_int(),
            'tip_produto': faker.word(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'cod_loja_ads_conta': faker.random_int(),
            'nom_canal_ads_conta': faker.word(),
            'nom_politica': faker.word(),
            'nom_mod_score': faker.word(),
            'val_score_aprov_conta': faker.random_int(),
            'cod_operacao_proposta_so': faker.bothify(text='??'),
            'id_proposta': faker.random_int(),
            'nom_colab_proposta': faker.name(),
            'id_chapa_colab_proposta': faker.bothify(text='??'),
            'des_origem_entrada_proposta': faker.word(),
            'id_cliente_so': faker.random_int(),
            'id_ori_comercial': faker.random_int(),
            'dth_ads_conta': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_prim_ads_conta': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_prim_ads_cred': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_loja_ativacao_credito': faker.random_int(),
            'nm_user_ativacao_credito': faker.name(),
            'cod_sit_conta': faker.random_int(),
            'des_sit_conta': faker.word(),
            'dth_sit_conta': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_agrp_sit_conta': faker.random_int(),
            'des_agrp_sit_conta': faker.word(),
            'cod_sit_financeiro_conta': faker.random_int(),
            'des_sit_financeiro_conta': faker.word(),
            'cod_overall_status_conta': faker.random_int(),
            'des_overall_status_conta': faker.word(),
            'cod_overall_reason_conta': faker.random_int(),
            'des_overall_reason_conta': faker.word(),
            'num_dia_vencto_fatura': faker.random_int(),
            'dth_prox_vencto_real': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_prox_vencto_padrao': faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_ult_alt_vencto': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'flg_conta_bloqueada': faker.random_element(elements=('S', 'N')),
            'flg_conta_cancelada': faker.random_element(elements=('S', 'N')),
            'id_produto_cartao_ant': faker.random_int(),
            'dth_ult_grade_produto_cartao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'id_conta_debito': faker.random_int(),
            'id_produto_conta_debito': faker.random_int(),
            'cod_sit_conta_debito': faker.random_int(),
            'des_sit_conta_debito': faker.word(),
            'dth_sit_conta_debito': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_agrp_sit_conta_debito': faker.random_int(),
            'des_agrp_sit_conta_debito': faker.word(),
            'cod_sit_financeiro_conta_debito': faker.random_int(),
            'des_sit_financeiro_conta_debito': faker.word(),
            'cod_overall_status_conta_debito': faker.random_int(),
            'des_overall_status_conta_debito': faker.word(),
            'cod_overall_reason_conta_debito': faker.random_int(),
            'des_overall_reason_conta_debito': faker.word(),
            'cod_banco': faker.random_int(),
            'cod_agencia': faker.random_int(),
            'dv_agencia': faker.random_int(),
            'cod_conta_corrente': faker.bothify(text='########'),
            'dv_conta_corrente': faker.random_digit(),
            'flg_conta_debito_bloqueada': faker.random_element(elements=('S', 'N')),
            'flg_conta_debito_cancelada': faker.random_element(elements=('S', 'N')),
            'dth_adesao_prod_flex': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_cancel_adesao_prod_flex': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_loja_ads_prod_flex': faker.random_int(),
            'nm_usr_adesao_prod_flex': faker.name(),
            'nm_usr_cancelamento_prod_flex': faker.name(),
            'id_adesao_carteira_digital_so': faker.random_int(),
            'dt_adesao_carteira_digital': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dt_cancelamento_carteira_digital': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'nm_usr_adesao_carteira_digital': faker.name(),
            'nm_usr_cancelamento_carteira_digital': faker.name(),
            'flg_overlimit_disp': faker.random_element(elements=('S', 'N')),
            'flg_indicacao_amigo_revendedor': faker.random_element(elements=('S', 'N')),
            'flg_conta_revendedor': faker.random_element(elements=('S', 'N')),
            'num_cpf_indicador': faker.random_number(digits=11, fix_len=True),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'id_conta_hist_dock': faker.random_int(),
            'id_cliente_hist_dock': faker.random_int(),
            'flg_conta_migrada': faker.random_element(elements=('S', 'N')),
            'dth_migracao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'des_origem': faker.word(),
            'num_anomes_ads_conta': faker.date_this_decade().strftime('%Y-%m-%d')

        }
        dados['conta'].append(conta)

        seguro_adesao = {
            'id_adesao_seguro_so': faker.random_int(),
            'des_tip_origem': faker.word(),
            'dth_adesao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'id_produto_financeiro': faker.random_int(),
            'nom_produto_financeiro': faker.word(),
            'des_tip_origem_pfin': faker.word(),
            'cod_tip_adesao': faker.random_int(),
            'des_tip_adesao': faker.word(),
            'cod_canal_venda': faker.random_int(),
            'des_canal_venda': faker.word(),
            'cod_tip_canal_venda': faker.random_int(),
            'des_tip_canal_venda': faker.word(),
            'cod_estabelecimento_adesao': faker.random_int(),
            'cod_estabelecimento_cancel': faker.random_int(),
            'cod_tip_situacao_seguro': faker.random_int(),
            'des_tip_situacao_seguro': faker.word(),
            'dth_situacao_seguro': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_tip_cancelamento': faker.random_int(),
            'des_tip_cancelamento': faker.word(),
            'cod_motivo_cancelamento': faker.random_int(),
            'des_motivo_cancelamento': faker.word(),
            'dth_cancelamento': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'id_conta': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'cod_tip_titularidade': faker.random_int(),
            'des_tip_titularidade': faker.word(),
            'cod_seguradora': faker.random_int(),
            'nom_seguradora': faker.company(),
            'des_tip_origem_sgrd': faker.word(),
            'dth_inicio_vigencia_seguro': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_termino_vigencia_seguro': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'num_meses_vigencia_seguro': faker.random_int(),
            'val_premio_total': faker.pyfloat(),
            'id_cliente_so': faker.random_int(),
            'id_cliente': faker.bothify(text='??'),
            'num_chapa_adesao': faker.random_int(),
            'num_chapa_cancel': faker.random_int(),
            'id_produto_cartao': faker.random_int(),
            'cod_artigo': faker.random_int(),
            'cod_cor': faker.random_int(),
            'cod_tamanho': faker.random_int(),
            'cod_sortimento': faker.random_int(),
            'nom_artigo': faker.word(),
            'cod_sku_produto': faker.bothify(text='??'),
            'val_venda_artigo': faker.pyfloat(),
            'num_apolice_seguro': faker.bothify(text='??'),
            'dth_ult_atu_so': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'flg_conta_credito': faker.random_element(elements=('S', 'N')),
            'num_anomes_adesao': faker.date_this_decade().strftime('%Y-%m-%d')
        }
        dados['seguro_adesao'].append(seguro_adesao)

    jsonl_data(data=dados)

    return dados

num_records = input_num_linhas()
pfs_unificacao_pefisa(num_records)




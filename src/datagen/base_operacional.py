from faker import Faker

from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')

def function_base_operacional(num_records):

    data = {'conta_cartao_cliente': [], 'emprestimo_pessoal_processado':[],'fatura_fechada':[] ,'faturamento_conta_digital':[], 'limite_disponibilidade_pos_mensal':[], 'pagamento_consolidado': []}

    for _ in range(num_records):
        criar_Conta_cartao_cliente = {
            'id_conta': faker.random_int(),
            'id_produto_cartao_atual': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'id_cliente_so': faker.random_int(),
            'cod_loja_ads_conta': faker.random_int(),
            'dth_ads_conta': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_prim_ads_conta': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'nom_canal_ads_conta': faker.word(),
            'cod_sit_conta': faker.random_int(),
            'des_sit_conta': faker.word(),
            'dth_sit_conta': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'num_dia_vencto_fatura': faker.random_int(min=1, max=31),
            'flg_conta_bloqueada': faker.random_element(elements=('S', 'N')),
            'flg_conta_cancelada': faker.random_element(elements=('S', 'N')),
            'dth_ult_grade_produto_cartao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'id_produto_ult_grade': faker.random_int(),
            'dth_ult_atu_so_conta': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'num_anomes_ads_conta': faker.random_int(),
            'id_chapa_colab_proposta': faker.uuid4(),
            'des_origem_entrada_proposta': faker.word(),
            'dth_produto_atual': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_prim_cancelamento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'des_motivo_prim_cancelamento': faker.word(),
            'dth_ult_cancelamento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'des_motivo_ult_cancelamento': faker.word(),
            'flg_pl_flex': faker.random_element(elements=('S', 'N')),
            'flg_indicacao_amigo_revendedor': faker.random_element(elements=('S', 'N')),
            'flg_conta_revendedor': faker.random_element(elements=('S', 'N')),
            'num_cpf_indicador': faker.random_number(digits=11, fix_len=True),
            'id_cartao': faker.random_int(),
            'num_cartao': faker.credit_card_number(),
            'num_bin': faker.random_int(),
            'num_seq_via_cartao': faker.random_int(),
            'cod_sit_cartao': faker.random_int(),
            'des_sit_cartao': faker.word(),
            'dth_sit_cartao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'flg_cartao_cancelado': faker.random_element(elements=('S', 'N')),
            'dth_cancelamento_cartao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_valid_cartao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'num_anomes_emis_cartao': faker.random_int(),
            'flg_titular': faker.random_element(elements=('S', 'N')),
            'num_anomes_valid_cartao': faker.random_int(),
            'tip_origem_principal': faker.word(),
            'cod_loja_pref': faker.random_int(),
            'nom_cliente': faker.name(),
            'dth_cadastro_cliente': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_nascimento': faker.date_of_birth(minimum_age=18, maximum_age=100).strftime('%Y-%m-%d %H:%M:%S'),
            'cod_sexo': faker.random_element(elements=('M', 'F')),
            'cod_estado_civil': faker.random_int(),
            'cod_cep_res': faker.postcode(),
            'nom_mae_cliente': faker.name(),
            'flg_funcionario': faker.random_element(elements=('S', 'N')),
            'cod_nacionalidade': faker.random_int(),
            'des_nacionalidade': faker.country(),
            'des_naturalidade_cidade': faker.city(),
            'cod_naturalidade_estado': faker.state_abbr(),
            'flg_pessoa_politicamente_exposta': faker.random_element(elements=('S', 'N')),
            'flg_deficiente_visual': faker.random_element(elements=('S', 'N')),
            'val_outra_renda_cliente': faker.random_number(digits=8, fix_len=True),
            'nom_pai_cliente': faker.name(),
            'num_rg': faker.bothify(text='########-#'),
            'dat_emissao_rg': faker.date_between(start_date='-30y', end_date='today').strftime('%Y-%m-%d'),
            'cod_orgao_expedicao_rg': faker.word(),
            'cod_estado_emissao_rg': faker.state_abbr(),
            'num_cnh': faker.bothify(text='########-#'),
            'dat_validade_cnh': faker.date_between(start_date='today', end_date='+10y').strftime('%Y-%m-%d'),
            'num_seguranca_cnh': faker.bothify(text='###'),
            'cod_validacao_cnh': faker.bothify(text='###'),
            'dat_emissao_cnh': faker.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),
            'val_patrimonio_total': faker.random_number(digits=8, fix_len=True),
            'cod_profissao': faker.random_int(),
            'nom_profissao': faker.job(),
            'id_produto_cartao_inicial': faker.random_int(),
            'dth_prim_grade': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'id_produto_prim_grade': faker.random_int(),
            'id_estab_prim_grade': faker.uuid4(),
            'id_chapa_colab_prim_grade': faker.uuid4(),
            'id_estab_ult_grade': faker.uuid4(),
            'id_chapa_colab_ult_grade': faker.uuid4(),
            'dth_ativacao_conta': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'flg_trans_ofs': faker.random_element(elements=('S', 'N')),
            'dth_inclusao_reg': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'des_origem': faker.word()
        }
        data['conta_cartao_cliente'].append(criar_Conta_cartao_cliente)

        criar_Emprestimo_pessoal_processado = {
            'id_evento_ep': faker.uuid4(),
            'id_cartao_credito_so': faker.random_int(),
            'num_cartao_credito': faker.credit_card_number(),
            'id_conta_cartao_credito': faker.random_int(),
            'nom_colab_proposta': faker.name(),
            'id_chapa_colab_proposta': faker.uuid4(),
            'cod_loja_ads_conta': faker.random_int(),
            'id_cliente_so': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'cod_tipo_operacao': faker.bothify(text='??'),
            'des_tipo_operacao': faker.word(),
            'id_estab_so': faker.random_int(),
            'cod_estab': faker.random_int(),
            'cod_status': faker.random_int(),
            'des_status': faker.word(),
            'dth_trans': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'val_trans': faker.random_number(digits=8, fix_len=True),
            'qtd_parcela': faker.random_int(min=1, max=12),
            'val_parcela': faker.random_number(digits=8, fix_len=True),
            'per_taxa_juro': faker.random_number(digits=5, fix_len=True),
            'val_trans_origem': faker.random_number(digits=8, fix_len=True),
            'val_trans_destino': faker.random_number(digits=8, fix_len=True),
            'cod_origem': faker.bothify(text='??'),
            'des_origem': faker.word(),
            'cod_ori_resolucao': faker.bothify(text='??'),
            'des_ori_resolucao': faker.word(),
            'dth_vencto_prim_par_ep': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_estimada_vencto_ult_par_ep': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'id_autorizacao': faker.random_int(),
            'cod_autorizacao': faker.bothify(text='??'),
            'val_tac': faker.random_number(digits=8, fix_len=True),
            'val_iof': faker.random_number(digits=8, fix_len=True),
            'val_juro': faker.random_number(digits=8, fix_len=True),
            'val_financiado': faker.random_number(digits=8, fix_len=True),
            'val_taxa': faker.random_number(digits=5, fix_len=True),
            'des_tipo_transacao': faker.word(),
            'des_origem_informacao': faker.word(),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_ult_atu_so': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'dat_cancelamento_ep': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'nom_canal_aprovacao_ep': faker.word(),
            'cod_loja_ads_ep': faker.random_int(),
            'nom_modelo_score': faker.word(),
            'des_sistema_origem': faker.word(),
            'num_anomes_ep': faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['emprestimo_pessoal_processado'].append(criar_Emprestimo_pessoal_processado)

        criar_Faturamento_conta_digital = {
            'id_conta_ccred_transacao': faker.random_int(),
            'id_cliente': faker.uuid4(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'num_cartao_credito': faker.credit_card_number(),
            'flg_titularidade': faker.random_element(elements=('S', 'N')),
            'flg_pl_flex': faker.random_element(elements=('S', 'N')),
            'flg_cartao_mutiplo': faker.random_element(elements=('S', 'N')),
            'id_produto_ccred_transacao': faker.random_int(),
            'dth_transacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_origem': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_status_transacao': faker.random_int(),
            'des_status_transacao': faker.word(),
            'des_tipo_trans_cred_deb': faker.word(),
            'cod_estab_transacao': faker.random_int(),
            'des_estab_transacao': faker.company(),
            'cod_mcc_estab_exter': faker.random_int(),
            'des_mcc_estab_exter': faker.word(),
            'id_transacao': faker.random_int(),
            'des_tipo_trans_on_off_us': faker.word(),
            'val_transacao': faker.random_number(digits=8, fix_len=True),
            'cod_tipo_transacao': faker.random_int(),
            'des_tipo_transacao': faker.word(),
            'cod_agrupamento_transacao': faker.random_int(),
            'val_saldo_atual_conta': faker.random_number(digits=8, fix_len=True),
            'flg_trans_carteira_digital': faker.random_element(elements=('S', 'N')),
            'flg_qr_code': faker.random_element(elements=('S', 'N')),
            'flg_cliente_funcionario': faker.random_element(elements=('S', 'N')),
            'flg_trans_isencao_tarifa': faker.random_element(elements=('S', 'N')),
            'flg_trans_cashback': faker.random_element(elements=('S', 'N')),
            'dth_inclusao_reg': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'num_anomes_transacao': faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['faturamento_conta_digital'].append(criar_Faturamento_conta_digital)
        
        criar_Fatura_fechada = {
            'id_conta': faker.random_int(),
            'id_cliente': faker.uuid4(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'cod_sit_conta': faker.random_int(),
            'des_sit_conta': faker.word(),
            'id_produto_cartao': faker.random_int(),
            'id_fatura': faker.random_int(),
            'id_fatura_anterior': faker.random_int(),
            'dth_vencto_padrao': faker.date_this_month().strftime('%Y-%m-%d'),
            'dat_vencto_real_ant': faker.date_this_month().strftime('%Y-%m-%d %H:%M:%S'),
            'val_pagamento_anterior': faker.random_number(digits=8, fix_len=True),
            'val_saldo_atual_ftura': faker.random_number(digits=8, fix_len=True),
            'val_saldo_anterior_fatura': faker.random_number(digits=8, fix_len=True),
            'val_minimo_atual': faker.random_number(digits=8, fix_len=True),
            'val_minimo_anterior': faker.random_number(digits=8, fix_len=True),
            'val_pagamento_realizado': faker.random_number(digits=8, fix_len=True),
            'flg_adesao_parcelamento': faker.random_element(elements=('S', 'N')),
            'des_tipo_parcelamento': faker.word(),
            'cod_tipo_pagamento': faker.bothify(text='??'),
            'des_canal_pagamento': faker.word(),
            'flg_cliente_cobranca': faker.random_element(elements=('S', 'N')),
            'flg_emite_extrato': faker.random_element(elements=('S', 'N')),
            'flg_pl_flex': faker.random_element(elements=('S', 'N')),
            'dth_corte_fatura': faker.date_this_month().strftime('%Y-%m-%d %H:%M:%S'),
            'val_cotacao_dolar_corte': faker.random_number(digits=5, fix_len=True),
            'dat_referencia': faker.random_int(),
            'dth_inclusao_reg': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'des_origem': faker.word(),
            'num_anomes_vencto_fatura': faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['fatura_fechada'].append(criar_Fatura_fechada)

        criar_Limite_disponibilidade_pos_mensal = {
            'id_conta': faker.random_int(),
            'id_produto_cartao': faker.random_int(),
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'num_cpf_cliente_titular': faker.random_number(digits=11, fix_len=True),
            'cod_tip_portador': faker.random_int(),
            'des_sit_conta': faker.word(),
            'flg_conta_cancelada': faker.random_element(elements=('S', 'N')),
            'dat_cadastro': faker.date_this_decade().strftime('%Y-%m-%d'),
            'dia_vencto_cartao': faker.random_int(min=1, max=31),
            'val_disp_global_credito': faker.random_number(digits=8, fix_len=True),
            'val_disp_parcela_nac': faker.random_number(digits=8, fix_len=True),
            'val_disp_saque_nac_global': faker.random_number(digits=8, fix_len=True),
            'val_limite_global_credito': faker.random_number(digits=8, fix_len=True),
            'val_limite_maximo': faker.random_number(digits=8, fix_len=True),
            'val_limite_parcelas_nac': faker.random_number(digits=8, fix_len=True),
            'val_limite_saque_nac_global': faker.random_number(digits=8, fix_len=True),
            'val_lim_util_max': faker.random_number(digits=8, fix_len=True),
            'val_lim_util_global': faker.random_number(digits=8, fix_len=True),
            'val_lim_util_parc': faker.random_number(digits=8, fix_len=True),
            'val_lim_util_saque': faker.random_number(digits=8, fix_len=True),
            'perc_iu_max': faker.random_number(digits=5, fix_len=True),
            'perc_iu_global': faker.random_number(digits=5, fix_len=True),
            'perc_iu_parc': faker.random_number(digits=5, fix_len=True),
            'perc_iu_saque': faker.random_number(digits=5, fix_len=True),
            'dth_ult_atu_so': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'num_seq_ult_alteracao': faker.random_int(),
            'dth_inclusao_reg': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'num_anomes_posicao_limite': faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['limite_disponibilidade_pos_mensal'].append(criar_Limite_disponibilidade_pos_mensal)

        criar_Pagamento_consolidado = {
            'num_cpf_cliente': faker.random_number(digits=11, fix_len=True),
            'id_conta': faker.random_int(),
            'id_produto_cartao': faker.random_int(),
            'dth_pagamento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'val_pagamento': faker.random_number(digits=8, fix_len=True),
            'des_tipo_pagamento': faker.word(),
            'des_canal_pagamento': faker.word(),
            'des_meio_pagamento': faker.word(),
            'cod_loja_pagamento': faker.random_int(),
            'qtde_dias_atraso_padrao': faker.random_int(),
            'qtde_dias_atraso_real': faker.random_int(),
            'id_fatura': faker.random_int(),
            'dth_vencto_padrao_fatura': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_vencto_real_fatura': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'val_min_fatura': faker.random_number(digits=8, fix_len=True),
            'val_tot_fatura': faker.random_number(digits=8, fix_len=True),
            'flg_adesao_parcelamento': faker.random_element(elements=('S', 'N')),
            'des_tipo_parcelamento': faker.word(),
            'flg_estorno': faker.random_element(elements=('S', 'N')),
            'dth_estorno': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'id_pagamento': faker.random_int(),
            'des_origem_informacao': faker.word(),
            'flg_emite_extrato': faker.random_element(elements=('S', 'N')),
            'dth_inclusao_reg': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_referencia': faker.random_int(),
            'des_origem': faker.word(),
            'num_anomes_pagto': faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['pagamento_consolidado'].append(criar_Pagamento_consolidado)

    jsonl_data(data=data)

    return data

num_records = input_num_linhas()
function_base_operacional(num_records)
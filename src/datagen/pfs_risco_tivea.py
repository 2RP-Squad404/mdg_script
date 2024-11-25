import random
import re

from faker import Faker

from jsonl_convert import input_num_linhas,jsonl_data

faker = Faker('pt_BR')


def function_pfs_risco_tivea(num_records):

    data = {'cartao': [], 'cobranca_campo_customizavel': [], 'cobr_cliente_atraso': [], 'cobranca_acordo': [],
            'cobranca_assessoria': [], 'cobranca_cliente': [], 'Cobranca_campo_customizavel': [], 'cobranca_email_cliente': [],
            'cobranca_endereco_cliente': [], 'cobranca_liquidacao_parc_acordo': [], 'cobranca_origem_acordo': [],
            'cobranca_pagamento_acordo': [], 'cobranca_parcela_acordo': [], 'cobranca_telefone_cliente': [], 'conta': []}

    for _ in range(num_records):

        criar_cartao_faker = {
            "id_cartao": faker.random_number(digits=10, fix_len=True),
            "id_produto_cartao": faker.random_int(min=5, max=7),
            "num_cartao": faker.credit_card_number(),
            "num_seq_via_cartao": faker.random_int(min=2, max=7),
            "id_conta": faker.random_int(min=1397165, max=24861863),
            "num_cpf_cliente": re.sub(r'\D', '', faker.cpf()),
            "cod_tip_portador": faker.random_int(min=1, max=4),
            "num_bin": faker.random_number(digits=6),
            "cod_loja_emis_cartao": faker.random_int(min=48, max=916),
            "id_cliente_so": faker.random_int(min=1000000, max=10000000),
            "dth_emis_cartao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dth_embs_cartao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dth_valid_cartao": faker.date_time_between(start_date="+3y", end_date='+6y').strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dth_desbloqueio": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "cod_sit_cartao": faker.random_int(min=1, max=50),
            "des_sit_cartao": faker.random_element(elements=('NORMAL', 'BLOQUEADO', 'CANCELADO', 'CANCELADO CLIENTE', 'CANCELADO EMBOSSING LOJA', 'CANCELADO TARJA', 'CADASTRO ERRO EMISSOR', 'CANCELADO PERDA', 'ALERTA PREVENTIVO MESA', 'BLOQUEADO PREVENÇÃO', 'CANCELADO EMBOSSING', 'CANCELADO DESATIVADO', 'FALSIFICAÇÃO NAC', 'CANCELADO DEIXADO LOJA', 'FALSIFICAÇÃO EXT', 'BLOQUEIO PREVENTIVO FALCON', 'CANCELADO CVV/CVV2 NAO GERADO', 'CANCELADO ROUBO', 'SUSPEITA DE FRAUDE - PREVENTIVO', 'CANCELADO DEFINITIVO TARJA', 'CANCELADO REEMISSÃO PERSONALIZADO', 'CANCELADO EXTRAVIADO', 'EXTRAVIO MALOTE CORREIOS')),
            "dth_sit_cartao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "cod_estagio_cartao": faker.random_int(min=0, max=22),
            "des_estagio_cartao": faker.random_element(elements=('DESBLOQUEADO SEM CODIGO', 'CRIADO', 'ENCAMINHADO')),
            "dth_estagio_cartao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "flg_embs_loja": faker.random_element(elements=('S', 'N')),
            "flg_cartao_cancelado": faker.random_element(elements=('S', 'N')),
            "flg_cartao_provisorio": faker.random_element(elements=('S', 'N')),
            "flg_conta_cancelada": faker.random_element(elements=('S', 'N')),
            "dth_ult_atu_so": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "num_seq_ult_alteracao": faker.random_int(min=1, max=4),
            "dth_inclusao_reg": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "num_anomes_emis_cartao": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cartao'].append(criar_cartao_faker)

        criar_cobranca_campo_customizavel_faker = {
            "id_cliente_cobranca": str(faker.random_number(digits=10, fix_len=True)),
            "nom_campo": faker.random_element(elements=('REACORDO', 'NOVO_LIMITE', 'ESTRATEGIA4')),
            "val_campo": faker.random_element(elements=('SERVICE_PREMIUM', 'TUDO JUSTO', 'SERASA', 'VALIDU', 'Portal Pefisa - PPN', 'DIGICOB TECNOLOGIA LTDA')),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_campo_customizavel'].append(criar_cobranca_campo_customizavel_faker)

        criar_cobr_cliente_atraso_faker = {
            "num_cpf_cnpj_cliente": faker.random_int(min=10000000000, max=99999999999),
            "id_conta": faker.random_number(digits=10, fix_len=True),
            "id_cliente_so": faker.random_number(digits=10, fix_len=True),
            "num_cartao": faker.credit_card_number(),
            "id_produto_cartao": faker.random_number(digits=10, fix_len=True),
            "nom_cliente": faker.name(),
            "tip_pessoa": "FISICA",
            "tip_situacao": faker.random_element(elements=("DEVEDOR", "COBRANCA", "ATIVO", "BLOQUEADO")),
            "nom_uf": faker.random_element(elements=("SP", "PR", "XX")),
            "cod_rating": faker.random_element(elements=("HH", "A", "C", "B", "G", "H", "D", "E", "F")),
            "des_marcador": None,
            "val_saldo_atual": faker.random_number(digits=5, fix_len=False),
            "val_saldo_atraso": faker.random_number(digits=5, fix_len=False),
            "val_saldo_contabil": faker.random_number(digits=4, fix_len=False),
            "val_saldo_provisao": None,
            "val_saldo_total": faker.random_number(digits=4, fix_len=False),
            "val_saldo_total_atraso": faker.random_number(digits=4, fix_len=False),
            "qtd_dias_atraso": faker.random_int(min=-30, max=3650),
            "qtd_parcela_aberta": faker.random_int(min=1, max=10),
            "dth_modificacao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "nom_assessoria": faker.company(),
            "num_ddd_cel": faker.random_int(min=11, max=99),
            "num_tel_cel": re.sub(r'\D', '', faker.phone_number()[-9:]),
            "num_ddd_res": faker.random_int(min=11, max=99),
            "num_tel_res": re.sub(r'\D', '', faker.phone_number()[-8:]),
            "num_ddd_com": faker.random_int(min=11, max=99),
            "num_tel_com": re.sub(r'\D', '', faker.phone_number()[-8:]),
            "nom_email": faker.email(),
            "cod_loja": faker.random_element(elements=("60", "72", "96", "98", "100", "6", "10", "12", "18", "26", "28", "32", "42", "46", "48", "52", "54", "56", "62", "64", "70", "74", "76", "78", "82", "84", "86", "88", "90", "94", "053", "102")),
            "cod_colmar": None,
            "cod_colchao": faker.random_element(elements=("49", "15")),
            "cod_contr_orig": None,
            "cod_dist_assessoria": None,
            "cod_dist_assess_mar": None,
            "cod_dist_escob": None,
            "cod_estrategia1": faker.random_element(elements=("202", "696", "847", "743", "46", "120", "10", "20", "811", "19", "783", "290", "713", "168", "67,27", "90", "856", "771", "P", "571", "259", "269", "782", "84", "218", "857", "744", "800", "650", "667", "277", "2", "683", "109", "730", "276", "206", "618", "217", "827", "792", "248", "33", "739", "682", "537", "757", "786", "211", "604")),
            "cod_estrategia2": faker.random_element(elements=("13", "98", "10", "40", "20", "21", "808", "705", "43", "807", "435", "202", "430", "1220", "806", "122", "F", "701", "900", "121", "902", "801", "600", "706", "700", "800", "0", "802", "41", "6002", "901", "11", "910", "23", "911", "69", "903", "702", "20231", "1", "400", "402", "809", "6001", "703", "20232", "94", "81", "97", "49")),
            "cod_estrategia3": faker.random_element(elements=("1", "2780.54", "0", "3638.47", "4251.09", "601.84", "3502.27", "4645.34", "1743.77", "167.4", "1129.22", "1001.99", "2915.01", "427.47", "7439.47", "3481.55", "2549.49", "865.84", "5091.79", "1238.35", "2836.28", "4175.9", "2786.91", "487.37", "3013.51", "32.39", "1796.20", "551.17", "3038.16", "783.48", "414.98", "4865.44", "927.77", "325.51", "1483.08", "2324.45", "2184.37", "355.89", "2057.74", "11166.39", "1332.86", "530.25", "7114.39", "1369.88", "3414.39", "2428.68", "4700.22", "2005.53", "1870.09", "1627.49")),
            "cod_estrategia4": faker.random_element(elements=("1", "0", "2", "5", "C")),
            "cod_estrategia5": None,
            "cod_fpd": faker.random_element(elements=("NAO", "sim", "SIM", "2", "1")),
            "cod_var_aux": faker.random_element(elements=("0", "1")),
            "cod_faixa_atraso_b": faker.random_element(elements=("1711 a 1800", "0901 a 0990", "Em dia", "Acima 1800", "0001 a 0006", "0007 a 0030", "0031 a 0060", "0061 a 0090", "0091 a 0120", "0121 a 0150", "0151 a 0180", "0181 a 0270", "0271 a 0360", "0361 a 0450", "0451 a 0540", "0541 a 0630", "0631 a 0720", "0721 a 0810", "0811 a 0900", "0991 a 1080", "1081 a 1170", "1171 a 1260", "1261 a 1350", "1351 a 1440", "1441 a 1530")),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobr_cliente_atraso'].append(criar_cobr_cliente_atraso_faker)

        criar_cobranca_acordo_faker = {
            "id_acordo_cobranca": faker.random_number(digits=10, fix_len=True),
            "id_cliente_externo": faker.random_int(min=10000000000, max=99999999999),
            "num_cpf_cnpj_cliente": faker.random_number(digits=11),
            "id_cobrador": faker.uuid4(),
            "nom_cobrador": faker.company(),
            "tip_modalidade_acordo": "Politica Padrao",
            "num_acordo": faker.random_int(min=1000000, max=9999999),
            "num_parcelas": faker.random_int(min=1, max=12),
            "dat_operacao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dat_emissao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dth_processamento": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dth_inclusao_origem": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dth_alteracao_origem": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "dat_vencimento": faker.date_this_year().strftime('%Y-%m-%d'),
            "ind_situacao": random.choice(["LIQUIDADO", "RENEGOCIADO", "PARCIAL", "PENDENTE", "NAO_CUMPRIDO", "CANCELADO"]),
            "val_taxa_operacao": faker.random_element([0.0, 2.0]),
            "val_principal": faker.random_int(min=0, max=10000),
            "val_juros": faker.random_int(min=0, max=10000),
            "val_atributo": 0.0,
            "val_total": faker.random_int(min=0, max=10000),
            "val_desconto": faker.random_int(min=0, max=2000),
            "val_saldo_principal": faker.random_int(min=0, max=10000),
            "val_saldo_total": faker.random_int(min=0, max=10000),
            "val_saldo_atual": faker.random_int(min=0, max=10000),
            "qtd_dias_atraso": faker.random_int(min=-100, max=100),
            "dat_atraso_orig_acordo": faker.date_this_year().strftime('%Y-%m-%d'),
            "id_acordo_usuario": faker.random_number(digits=10, fix_len=True),
            "nom_acordo_usuario": faker.name(),
            "id_acordo_assessoria": faker.random_number(digits=10, fix_len=True),
            "nom_acordo_assessoria": faker.company(),
            "id_acordo_negociacao": faker.random_number(digits=10, fix_len=True),
            "nom_acordo_negociacao": faker.job(),
            "tip_acordo_meio_pagto": random.choice(["BOLETO_PIX", "BOLETO", "DINHEIRO"]),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_acordo'].append(criar_cobranca_acordo_faker)

        criar_cobranca_assessoria_faker = {
            "id_assessoria": str(faker.random_number(digits=10, fix_len=True)),
            "nom_assessoria": faker.company(),
            "id_cliente_cobranca": str(faker.random_number(digits=10, fix_len=True)),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_assessoria'].append(criar_cobranca_assessoria_faker)

        criar_cobranca_cliente_faker = {
            "id_cliente_cobranca": faker.random_number(digits=10, fix_len=True),
            "id_cliente_externo": faker.random_number(digits=11, fix_len=True),
            "tip_pessoa": faker.random_element(elements=('FISICA')),
            "tip_situacao": faker.random_element(elements=('COBRANCA', 'DEVEDOR', 'ATIVO', 'BLOQUEADO')),
            "nom_cliente": faker.name(),
            "num_cpf_cnpj_cliente": faker.random_number(digits=11, fix_len=True),
            "nom_uf": faker.random_element(elements=('GO', 'MG', 'SC')),
            "cod_rating": faker.random_element(elements=('A', 'HH', 'B', 'F', 'G', 'D', 'H', 'C', 'E')),
            "des_marcador": None,
            "num_dias_maior_atraso": None,
            "dat_maior_atraso": None,
            "val_saldo_atraso": faker.random_number(digits=5, fix_len=False),
            "val_saldo_atual": faker.random_number(digits=5, fix_len=False),
            "val_saldo_contabil": faker.random_number(digits=5, fix_len=False),
            "val_saldo_provisao": None,
            "qtd_dias_atraso": faker.random_int(min=-1, max=2000),
            "val_saldo_total": faker.random_number(digits=5, fix_len=False),
            "val_saldo_total_atraso": faker.random_number(digits=5, fix_len=False),
            "dth_modificacao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
            "num_ddd_cel": faker.random_element(elements=(11, 15)),
            "num_tel_cel": faker.random_number(digits=9, fix_len=True),
            "num_ddd_res": faker.random_element(elements=(62, 34, 47)),
            "num_tel_res": faker.random_number(digits=8, fix_len=True),
            "num_ddd_com": faker.random_element(elements=(34, 11, 13)),
            "num_tel_com": faker.random_number(digits=8, fix_len=True),
            "nom_email": faker.email(),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_cliente'].append(criar_cobranca_cliente_faker)

        criar_Cobranca_campo_customizavel_faker = {
            "id_cliente_cobranca": faker.random_number(digits=10, fix_len=True),
            "nom_campo": faker.word(),
            "val_campo": faker.word(),
            "dat_referencia": faker.date()
        }
        data['Cobranca_campo_customizavel'].append(criar_Cobranca_campo_customizavel_faker)

        criar_cobranca_email_cliente_faker = {
            "id_cliente_cobranca": faker.random_number(digits=10, fix_len=True),
            "nom_email": faker.email(),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_email_cliente'].append(criar_cobranca_email_cliente_faker)

        criar_cobranca_endereco_cliente_faker = {
            "id_cliente_cobranca": faker.random_number(digits=10, fix_len=True),
            "id_cliente_externo": faker.ean13(),
            "id_endereco_cobranca": faker.random_number(digits=10, fix_len=True),
            "tip_endereco_princ": faker.boolean(),
            "nom_logradouro": faker.street_name(),
            "num_logradouro": str(faker.building_number()),
            "nom_complemento": faker.street_address(),
            "num_cep": re.sub(r'\D', '', faker.postcode()),
            "nom_bairro": faker.street_name(),
            "nom_cidade": faker.city(),
            "nom_uf": faker.state_abbr(),
            "ind_tipo": faker.random_element(elements=('RESIDENCIAL', 'COMERCIAL', 'OUTRO')),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_endereco_cliente'].append(criar_cobranca_endereco_cliente_faker)

        criar_cobranca_liquidacao_parc_acordo_faker = {
            "id_liqd_parc_acordo": faker.random_number(digits=10, fix_len=True),
            "id_parcela_acordo": faker.random_number(digits=10, fix_len=True),
            "num_parcela_acordo": faker.random_int(min=0, max=24),
            "val_principal": faker.random_int(min=0, max=1000),
            "val_total": faker.random_int(min=0, max=1000),
            "val_juros": faker.random_int(min=0, max=10),
            "val_encargos": faker.random_int(min=0, max=150),
            "val_desconto": faker.random_int(min=0, max=10),
            "val_distorcao": faker.random_int(min=0, max=10),
            "ind_tipo_liqd": faker.random_element(elements=("TOTAL", "PARCIAL")),
            "id_pagto_acordo": faker.random_number(digits=10, fix_len=True),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_liquidacao_parc_acordo'].append(criar_cobranca_liquidacao_parc_acordo_faker)

        criar_cobranca_origem_acordo_faker = {
            "id_origem_acordo": faker.numerify('####################'),
            "id_acordo_cobranca": faker.random_number(digits=10, fix_len=True),
            "num_contrato": faker.numerify('#################'),
            "num_ordem_contrato": faker.random_int(min=1, max=10),
            "id_parcela": faker.numerify('####################'),
            "num_parcela": faker.random_int(min=1, max=100),
            "dat_vencimento": faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            "id_situacao": faker.random_element(elements=('CANCELADO', 'LIQUIDADO', 'ABERTO')),
            "qtd_dias_atr_cont": faker.random_int(min=0, max=1000),
            "val_principal": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_total": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_permanencia": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_multa": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_juros": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_tarifa": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_adicionado": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_atual": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_desconto": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_desc_principal": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_desc_juros": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_desc_multa": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_desc_permanencia": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "val_desconto_total": faker.pyfloat(min_value=0, max_value=1000000, right_digits=2),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_origem_acordo'].append(criar_cobranca_origem_acordo_faker)

        criar_cobranca_pagamento_acordo_faker = {
            "id_pagto_acordo": faker.random_number(digits=10, fix_len=True),
            "id_acordo_cobranca": faker.random_number(digits=10, fix_len=True),
            "dat_processamento": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dat_liquidacao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dat_credito": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dat_cnab": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dat_operacao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dth_horainclusao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "ind_forma_liquidacao": faker.word(),
            "val_recebido": faker.pyfloat(min_value=0, max_value=10000, right_digits=2),
            "val_desconto": faker.pyfloat(min_value=0, max_value=1000, right_digits=2),
            "val_encargos": faker.pyfloat(min_value=0, max_value=1000, right_digits=2),
            "val_distorcao": faker.random_int(min=0, max=1000),
            "ind_situacao": faker.word(),
            "ind_integracao": faker.word(),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d'),
        }
        data['cobranca_pagamento_acordo'].append(criar_cobranca_pagamento_acordo_faker)

        criar_cobranca_parcela_acordo_faker = {
            "id_parcela_acordo": faker.random_number(digits=10, fix_len=True),
            "id_acordo_cobranca": faker.random_number(digits=10, fix_len=True),
            "num_parcela_acordo": faker.random_int(min=1, max=30),
            "dat_vencimento": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "ind_situacao": faker.random_element(elements=('LIQUIDADO', 'CANCELADO', 'CONCLUIDO', 'ABERTO')),
            "num_nossonumero": faker.bothify(text='########'),
            "val_principal": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
            "val_juros": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
            "val_tarifa": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
            "val_adicionado": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
            "val_total": faker.pyfloat(left_digits=4, right_digits=2, positive=True),
            "val_tributo": faker.pyfloat(left_digits=2, right_digits=2, positive=True),
            "val_base_tributo": faker.pyfloat(left_digits=4, right_digits=2, positive=True),
            "val_permanencia": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
            "val_saldo_principal": faker.pyfloat(left_digits=4, right_digits=2, positive=True),
            "val_saldo_total": faker.pyfloat(left_digits=4, right_digits=2, positive=True),
            "val_saldo_atual": faker.pyfloat(left_digits=4, right_digits=2, positive=True),
            "ind_registrado": faker.boolean().__str__().lower(),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_parcela_acordo'].append(criar_cobranca_parcela_acordo_faker)

        criar_cobranca_telefone_cliente_faker = {
            "id_cliente_cobranca": faker.random_number(digits=10, fix_len=True),
            "num_ddd_celular": faker.random_int(min=10, max=99),
            "num_tel_celular": faker.random_number(digits=9),
            "num_ddd_residencial": faker.random_int(min=10, max=99),
            "num_tel_residencial": faker.random_number(digits=8),
            "num_ddd_comercial": faker.random_int(min=10, max=99),
            "num_tel_comercial": faker.random_number(digits=8),
            "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
        }
        data['cobranca_telefone_cliente'].append(criar_cobranca_telefone_cliente_faker)

        criar_conta_faker = {
            "id_conta": faker.random_number(digits=10, fix_len=True),
            "id_produto_cartao": faker.random_int(min=1, max=20),
            "tip_produto": faker.word().upper(),
            "num_cpf_cliente": faker.random_number(digits=11),
            "cod_loja_ads_conta": faker.random_int(min=100, max=1000),
            "nom_canal_ads_conta": faker.word() + " " + faker.word(),
            "nom_politica": faker.word() + "_" + faker.word(),
            "nom_mod_score": str(faker.random_int(min=1, max=1000)),
            "val_score_aprov_conta": faker.random_int(min=-1, max=1000),
            "cod_operacao_proposta_so": str(faker.random_int(min=100000000000000000, max=999999999999999999)),
            "id_proposta": faker.random_int(min=10000000, max=100000000),
            "nom_colab_proposta": faker.name(),
            "id_chapa_colab_proposta": str(faker.random_int(min=100000, max=1000000)),
            "des_origem_entrada_proposta": faker.word(),
            "id_cliente_so": faker.random_int(min=10000000, max=100000000),
            "id_ori_comercial": faker.random_int(min=1000, max=10000),
            "dth_ads_conta": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dth_prim_ads_conta": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dth_prim_ads_cred": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "cod_sit_conta": faker.random_int(min=0, max=100),
            "des_sit_conta": faker.word(),
            "dth_sit_conta": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "num_dia_vencto_fatura": faker.random_int(min=1, max=31),
            "dth_prox_vencto_real": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dth_prox_vencto_padrao": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dth_ult_alt_vencto": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "flg_conta_bloqueada": faker.random_element(elements=('S', 'N')),
            "flg_conta_cancelada": faker.random_element(elements=('S', 'N')),
            "id_produto_cartao_ant": faker.random_int(min=1, max=20),
            "dth_ult_grade_produto_cartao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "cod_banco": faker.random_int(min=100, max=1000),
            "cod_agencia": faker.random_int(min=1, max=1000),
            "dv_agencia": faker.random_digit(),
            "cod_conta_corrente": str(faker.random_int(min=10000000, max=99999999)),
            "dv_conta_corrente": str(faker.random_int(min=1, max=12)),
            "dth_adesao_prod_flex": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dth_cancel_adesao_prod_flex": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "id_adesao_carteira_digital_so": faker.random_int(min=1000000, max=10000000),
            "dt_adesao_carteira_digital": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "dt_cancelamento_carteira_digital": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "nm_usr_adesao_carteira_digital": faker.name(),
            "nm_usr_cancelamento_carteira_digital": faker.name(),
            "flg_overlimit_disp": faker.random_element(elements=('S', 'N')),
            "flg_indicacao_amigo_revendedor": faker.random_element(elements=('S', 'N')),
            "flg_conta_revendedor": faker.random_element(elements=('S', 'N')),
            "num_cpf_indicador": faker.random_number(digits=11),
            "dth_ult_atu_so": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "num_seq_ult_alteracao": faker.random_int(min=1, max=10000),
            "dat_referencia": faker.date_this_year().strftime('%Y%m%d'),
            "dth_inclusao_reg": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
            "num_anomes_ads_conta": faker.date_this_year().strftime('%Y-%m-%d')
        }
    data['conta'].append(criar_conta_faker)

    jsonl_data(data=data)

    return data

num_records = input_num_linhas()
function_pfs_risco_tivea(num_records)

import json
import os
from faker import Faker
import itertools
from datetime import date, datetime
import random 
import re

faker = Faker('pt_BR')
id_serial = itertools.count(start=0)

def Datagen_pfs_risco_tivea(num_records):

    data = {'cartao': [], 'cobranca_campo_customizavel': [], 'cobr_cliente_atraso': [], 'cobranca_acordo': [],
            'cobranca_assessoria': [], 'cobranca_cliente':[], 'Cobranca_campo_customizavel': [], 'cobranca_email_cliente': [],
            'cobranca_endereco_cliente': [], 'cobranca_liquidacao_parc_acordo': [], 'cobranca_origem_acordo': []}

    for _ in range(num_records):

        # Este arquivo possui as funções geradoras para a tabelas do dataset: 'pfs_risco_tivea'
        criar_cartao_faker = {
                "id_cartao": next(id_serial),
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
                "des_sit_cartao": faker.random_element(elements=['NORMAL', 'BLOQUEADO', 'CANCELADO', 'CANCELADO CLIENTE', 'CANCELADO EMBOSSING LOJA', 'CANCELADO TARJA', 'CADASTRO ERRO EMISSOR', 'CANCELADO PERDA', 'ALERTA PREVENTIVO MESA', 'BLOQUEADO PREVENÇÃO', 'CANCELADO EMBOSSING', 'CANCELADO DESATIVADO', 'FALSIFICAÇÃO NAC', 'CANCELADO DEIXADO LOJA', 'FALSIFICAÇÃO EXT', 'BLOQUEIO PREVENTIVO FALCON', 'CANCELADO CVV/CVV2 NAO GERADO', 'CANCELADO ROUBO', 'SUSPEITA DE FRAUDE - PREVENTIVO', 'CANCELADO DEFINITIVO TARJA', 'CANCELADO REEMISSÃO PERSONALIZADO', 'CANCELADO EXTRAVIADO', 'EXTRAVIO MALOTE CORREIOS']),
                "dth_sit_cartao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
                "cod_estagio_cartao": faker.random_int(min=0, max=22),
                "des_estagio_cartao": faker.random_element(elements=['DESBLOQUEADO SEM CODIGO', 'CRIADO', 'ENCAMINHADO']),
                "dth_estagio_cartao": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
                "flg_embs_loja": faker.random_element(elements=['S', 'N']),
                "flg_cartao_cancelado": faker.random_element(elements=['S', 'N']),
                "flg_cartao_provisorio": faker.random_element(elements=['S', 'N']),
                "flg_conta_cancelada": faker.random_element(elements=['S', 'N']),
                "dth_ult_atu_so": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
                "num_seq_ult_alteracao": faker.random_int(min=1, max=4),
                "dth_inclusao_reg": faker.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S+00:00'),
                "num_anomes_emis_cartao": faker.date_this_year().strftime('%Y-%m-%d')
            }
        data['cartao'].append(criar_cartao_faker)



        criar_cobranca_campo_customizavel_faker = {
                "id_cliente_cobranca": str(next(id_serial)),
                "nom_campo": faker.random_element(elements=['REACORDO', 'NOVO_LIMITE', 'ESTRATEGIA4']),
                "val_campo": faker.random_element(elements=['SERVICE_PREMIUM', 'TUDO JUSTO', 'SERASA', 'VALIDU', 'Portal Pefisa - PPN', 'DIGICOB TECNOLOGIA LTDA']),
                "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
            }
        data['cobranca_campo_customizavel'].append(criar_cobranca_campo_customizavel_faker)
        
        criar_cobr_cliente_atraso_faker = {
                "num_cpf_cnpj_cliente": faker.random_int(min=10000000000, max=99999999999),
                "id_conta": next(id_serial),
                "id_cliente_so": next(id_serial),
                "num_cartao": faker.credit_card_number(),
                "id_produto_cartao": next(id_serial),
                "nom_cliente": faker.name(),
                "tip_pessoa": "FISICA",
                "tip_situacao": faker.random_element(elements=["DEVEDOR", "COBRANCA", "ATIVO", "BLOQUEADO"]),
                "nom_uf": faker.random_element(elements=["SP", "PR", "XX"]),
                "cod_rating": faker.random_element(elements=["HH", "A", "C", "B", "G", "H", "D", "E", "F"]),
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
                "cod_loja": faker.random_element(elements=["60", "72", "96", "98", "100", "6", "10", "12", "18", "26", "28", "32", "42", "46", "48", "52", "54", "56", "62", "64", "70", "74", "76", "78", "82", "84", "86", "88", "90", "94", "053", "102"]),
                "cod_colmar": None,
                "cod_colchao": faker.random_element(elements=["49", "15"]),
                "cod_contr_orig": None,
                "cod_dist_assessoria": None,
                "cod_dist_assess_mar": None,
                "cod_dist_escob": None,
                "cod_estrategia1": faker.random_element(elements=["202", "696", "847", "743", "46", "120", "10", "20", "811", "19", "783", "290", "713", "168", "67,27", "90", "856", "771", "P", "571", "259", "269", "782", "84", "218", "857", "744", "800", "650", "667", "277", "2", "683", "109", "730", "276", "206", "618", "217", "827", "792", "248", "33", "739", "682", "537", "757", "786", "211", "604"]),
                "cod_estrategia2": faker.random_element(elements=["13", "98", "10", "40", "20", "21", "808", "705", "43", "807", "435", "202", "430", "1220", "806", "122", "F", "701", "900", "121", "902", "801", "600", "706", "700", "800", "0", "802", "41", "6002", "901", "11", "910", "23", "911", "69", "903", "702", "20231", "1", "400", "402", "809", "6001", "703", "20232", "94", "81", "97", "49"]),
                "cod_estrategia3": faker.random_element(elements=["1", "2780.54", "0", "3638.47", "4251.09", "601.84", "3502.27", "4645.34", "1743.77", "167.4", "1129.22", "1001.99", "2915.01", "427.47", "7439.47", "3481.55", "2549.49", "865.84", "5091.79", "1238.35", "2836.28", "4175.9", "2786.91", "487.37", "3013.51", "32.39", "1796.20", "551.17", "3038.16", "783.48", "414.98", "4865.44", "927.77", "325.51", "1483.08", "2324.45", "2184.37", "355.89", "2057.74", "11166.39", "1332.86", "530.25", "7114.39", "1369.88", "3414.39", "2428.68", "4700.22", "2005.53", "1870.09", "1627.49"]),
                "cod_estrategia4": faker.random_element(elements=["1", "0", "2", "5", "C"]),
                "cod_estrategia5": None,
                "cod_fpd": faker.random_element(elements=["NAO", "sim", "SIM", "2", "1"]),
                "cod_var_aux": faker.random_element(elements=["0", "1"]),
                "cod_faixa_atraso_b": faker.random_element(elements=["1711 a 1800", "0901 a 0990", "Em dia", "Acima 1800", "0001 a 0006", "0007 a 0030", "0031 a 0060", "0061 a 0090", "0091 a 0120", "0121 a 0150", "0151 a 0180", "0181 a 0270", "0271 a 0360", "0361 a 0450", "0451 a 0540", "0541 a 0630", "0631 a 0720", "0721 a 0810", "0811 a 0900", "0991 a 1080", "1081 a 1170", "1171 a 1260", "1261 a 1350", "1351 a 1440", "1441 a 1530"]),
                "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
            }
        data['cobr_cliente_atraso'].append(criar_cobr_cliente_atraso_faker)

        criar_cobranca_acordo_faker = {
                "id_acordo_cobranca": next(id_serial),
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
                "id_acordo_usuario": next(id_serial),
                "nom_acordo_usuario": faker.name(),
                "id_acordo_assessoria": next(id_serial),
                "nom_acordo_assessoria": faker.company(),
                "id_acordo_negociacao": next(id_serial),
                "nom_acordo_negociacao": faker.job(),
                "tip_acordo_meio_pagto": random.choice(["BOLETO_PIX", "BOLETO", "DINHEIRO"]),
                "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
            }
        data['cobranca_acordo'].append(criar_cobranca_acordo_faker)

        criar_cobranca_assessoria_faker = {
                "id_assessoria": str(next(id_serial)),
                "nom_assessoria": faker.company(),
                "id_cliente_cobranca": str(next(id_serial)),
                "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
            }
        data['cobranca_assessoria'].append(criar_cobranca_assessoria_faker)


        criar_cobranca_cliente_faker = {
                "id_cliente_cobranca": next(id_serial),
                "id_cliente_externo": faker.random_number(digits=11, fix_len=True),
                "tip_pessoa": faker.random_element(elements=['FISICA']),
                "tip_situacao": faker.random_element(elements=['COBRANCA', 'DEVEDOR', 'ATIVO', 'BLOQUEADO']),
                "nom_cliente": faker.name(),
                "num_cpf_cnpj_cliente": faker.random_number(digits=11, fix_len=True),
                "nom_uf": faker.random_element(elements=['GO', 'MG', 'SC']),
                "cod_rating": faker.random_element(elements=['A', 'HH', 'B', 'F', 'G', 'D', 'H', 'C', 'E']),
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
                "num_ddd_cel": faker.random_element(elements=[11]),
                "num_tel_cel": faker.random_number(digits=9, fix_len=True),
                "num_ddd_res": faker.random_element(elements=[62, 34, 47]),
                "num_tel_res": faker.random_number(digits=8, fix_len=True),
                "num_ddd_com": faker.random_element(elements=[34, 11, 13]),
                "num_tel_com": faker.random_number(digits=8, fix_len=True),
                "nom_email": faker.email(),
                "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
            }
        data['cobranca_cliente'].append(criar_cobranca_cliente_faker)


        criar_Cobranca_campo_customizavel_faker = {
                "id_cliente_cobranca": next(id_serial),
                "nom_campo": faker.word(),
                "val_campo": faker.word(),
                "dat_referencia": faker.date().strftime('%Y-%m-%d %H:%M:%S')
            }
        data['Cobranca_campo_customizavel'].append(criar_Cobranca_campo_customizavel_faker)

        criar_cobranca_email_cliente_faker = {
                "id_cliente_cobranca": next(id_serial),
                "nom_email": faker.email(),
                "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
            }
        data['cobranca_email_cliente'].append(criar_cobranca_email_cliente_faker)

        criar_cobranca_endereco_cliente_faker = {
                "id_cliente_cobranca": next(id_serial),
                "id_cliente_externo": faker.ean13(),
                "id_endereco_cobranca": next(id_serial),
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
                "id_liqd_parc_acordo": next(id_serial),
                "id_parcela_acordo": next(id_serial),
                "num_parcela_acordo": faker.random_int(min=0, max=10),
                "val_principal": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
                "val_total": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
                "val_juros": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
                "val_encargos": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
                "val_desconto": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
                "val_distorcao": faker.pyfloat(left_digits=3, right_digits=2, positive=True),
                "ind_tipo_liqd": faker.random_element(elements=("TOTAL", "PARCIAL")),
                "id_pagto_acordo": next(id_serial),
                "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d %H:%M:%S')
            }
        data['cobranca_liquidacao_parc_acordo'].append(criar_cobranca_liquidacao_parc_acordo_faker)

        criar_cobranca_origem_acordo_faker = {
                "id_origem_acordo": faker.numerify('####################'),
                "id_acordo_cobranca": next(id_serial),
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

    # Obtendo o nome do dataset
    dataset_name = os.path.splitext(os.path.basename(__file__))[0]

    # Obtendo o caminho absoluto do diretório raiz do projeto
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    output_path = os.path.join(project_root, "src/mock_data", dataset_name)

    os.makedirs(output_path, exist_ok=True)

    # Salvando os dados
    for array_name, array_data in data.items():
        filename = f"{array_name}.jsonl"
        filepath = os.path.join(output_path, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            for item in array_data:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')

    return data


num_records = 100
generated_data = Datagen_pfs_risco_tivea(num_records)
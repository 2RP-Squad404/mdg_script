import random

from faker import Faker
from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')


def function_pfs_pfin_raw_dw(num_registros_dim_locais, num_registros_dw_funcionarios):
    dados = {'dim_locais': [], 'dw_funcionario': []}

    for _ in range(num_registros_dim_locais):
        registro_dim_locais = {
            'sk_local': faker.random_int(),
            'cod_estabelecimento': faker.random_int(),
            'nom_estabelecimento': faker.company(),
            'cod_micro_regiao': faker.random_int(),
            'des_micro_regiao': faker.word(),
            'cod_regional': faker.random_int(),
            'des_regional': faker.word(),
            'cod_seg_geo_economico': faker.bothify(text='??'),
            'des_seg_geo_economico': faker.word(),
            'cod_corporacao': faker.random_int(),
            'des_corporacao': faker.word(),
            'des_logradouro': faker.street_address(),
            'num_logradouro': faker.building_number(),
            'cod_cep': faker.postcode().replace('-', ''),
            'des_bairro': faker.street_name(),
            'cod_municipio': faker.random_int(),
            'nom_municipio': faker.city(),
            'cod_estado': faker.state_abbr(),
            'nom_estado': faker.state(),
            'cod_pais': faker.random_int(),
            'nom_pais': faker.country(),
            'cod_atividade_economica': faker.random_int(),
            'des_atividade_economica': faker.job(),
            'cod_grupo_margem': faker.random_int(),
            'des_grupo_margem': faker.word(),
            'nom_fantasia': faker.company(),
            'dat_abertura': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_ult_reforma': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_fechamento': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.2 else None,
            'des_natureza': faker.word(),
            'des_propriedade': faker.word(),
            'des_clima': faker.word(),
            'des_apoio': faker.word(),
            'des_situacao': faker.word(),
            'des_operacao': faker.word(),
            'des_tamanho': faker.word(),
            'num_habitantes_proximidade': faker.random_int(),
            'num_habitantes_municipio': faker.random_int(),
            'hor_abertura_semana': faker.time().strftime('%H:%M:%S'),
            'hor_fechamento_semana': faker.time().strftime('%H:%M:%S'),
            'num_horas_semana': faker.random_number(digits=2, fix_len=False),
            'hor_abertura_sabado': faker.time().strftime('%H:%M:%S'),
            'hor_fechamento_sabado': faker.time().strftime('%H:%M:%S'),
            'num_horas_sabado': faker.random_number(digits=2, fix_len=False),
            'hor_abertura_domingo': faker.time().strftime('%H:%M:%S'),
            'hor_fechamento_domingo': faker.time().strftime('%H:%M:%S'),
            'num_horas_domingo': faker.random_number(digits=2, fix_len=False),
            'val_renda_per_capita': faker.random_int(),
            'qtd_metragem_quadrada_av': faker.random_int(),
            'nom_gerente_comercial': faker.name(),
            'nom_gerente_regional': faker.name(),
            'ind_entrega_armazem': faker.random_element(elements=('S', 'N')),
            'ind_abertura_domingo': faker.random_element(elements=('S', 'N')),
            'ind_responsavel_regional': faker.random_element(elements=('S', 'N')),
            'ind_responsavel_micro_regiao': faker.random_element(elements=('S', 'N')),
            'ind_sk_atual': faker.random_element(elements=('S', 'N')),
            'sk_micro_regiao': faker.random_int(),
            'sk_regional': faker.random_int(),
            'sk_corporacao': faker.random_int(),
            'sk_seg_geo_economico': faker.random_int(),
            'sk_pais': faker.random_int(),
            'sk_estado': faker.random_int(),
            'sk_municipio': faker.random_int(),
            'sk_clima': faker.random_int(),
            'cod_clima_so': faker.bothify(text='??'),
            'dat_inc_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_exc_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.05 else None,
            'sk_estrutura_estoque_local': faker.random_int(),
            'dat_inauguracao': faker.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S'),
            'sk_tipo_porte_local': faker.random_int(),
            'num_cgc': faker.random_int(),
            'num_digito_local': faker.random_int(),
            'num_inscricao_estadual': faker.bothify(text='########-#'),
            'num_inscricao_municipal': faker.bothify(text='########-#'),
            'num_latitude': faker.random_int(),
            'num_longitude': faker.random_int(),
            'sk_ger_geral_venda': faker.random_int()
        }
        dados['dim_locais'].append(registro_dim_locais)

    for _ in range(num_registros_dw_funcionarios):
        registro_dw_funcionarios = {
            'sk_funcionario': faker.random_int(),
            'num_chapa_so': faker.random_int(),
            'nom_funcionario': faker.name(),
            'sk_local': random.choice([x['sk_local'] for x in dados['Dim_locais']]),  # Seleciona um sk_local existente
            'sk_cargo': faker.random_int(),
            'dat_dia_admissao': faker.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d %H:%M:%S'),
            'dat_dia_demissao': faker.date_between(start_date='today', end_date='+1y').strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.2 else None,
            'dat_dia_ini_afastamento': faker.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.1 else None,
            'dat_dia_fim_afastamento': faker.date_between(start_date='today', end_date='+1y').strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.1 else None,
            'des_email': faker.email(),
            'dat_inc_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_ult_alt_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_exc_dw': faker.date_time().strftime('%Y-%m-%d %H:%M:%S') if random.random() < 0.05 else None,
            'sk_situacao_funcionario': faker.random_int(),
            'num_cpf': faker.cpf(),
            'num_rg': faker.bothify(text='########-#')
        }
        dados['dw_funcionario'].append(registro_dw_funcionarios)

    jsonl_data(data=dados)

    return dados


num_records = input_num_linhas()
function_pfs_pfin_raw_dw(num_records)

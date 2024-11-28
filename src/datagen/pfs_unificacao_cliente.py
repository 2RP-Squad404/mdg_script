from faker import Faker
from datetime import datetime, date
import random

from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')

def function_unificacao_cliente(num_records):
    data = {'cliente': [], 'cliente_complemento': [], 'cliente_item_perfil': [], 'de_para_num_pfj_id_cdt_cpf': [], 'v_estabelecimento': []}

    for _ in range(num_records):
        criar_cliente = {
            'id_cliente': str(faker.random_number(digits=10, fix_len=True)),
            'dth_ult_atu_so': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'tip_pessoa': faker.random_element(elements=('Física', 'Jurídica')),
            'num_cpf_cnpj_cliente': faker.random_number(digits=11),
            'nom_cliente': faker.name(),
            'dth_cadastro': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_loja_cad': faker.random_number(digits=3),
            'des_email': faker.email(),
            'dat_nascimento': faker.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d %H:%M:%S'),
            'cod_sexo': faker.random_element(elements=('M', 'F')),
            'cod_loja_pref': faker.random_number(digits=3),
            'num_ddd_cel': faker.random_number(digits=2),
            'num_tel_cel': faker.random_number(digits=8),
            'num_ddd_res': faker.random_number(digits=2),
            'num_tel_res': faker.random_number(digits=8),
            'des_lograd_end_res': faker.street_address(),
            'num_endereco_res': str(faker.building_number()),
            'des_compl_end_res': faker.building_number(),
            'nom_bairro_res': faker.street_name(),
            'nom_cidade_res': faker.city(),
            'cod_estado_res': faker.state_abbr(),
            'cod_cep_res': faker.postcode(),
            'des_pais_res': 'Brasil',
            'num_ddd_com': faker.random_number(digits=2),
            'num_tel_com': faker.random_number(digits=8),
            'des_lograd_end_com': faker.street_address(),
            'num_endereco_com': str(faker.building_number()),
            'des_compl_end_res': faker.building_number(),
            'nom_bairro_com': faker.street_name(),
            'nom_cidade_com': faker.city(),
            'cod_estado_com': faker.state_abbr(),
            'cod_cep_com': faker.postcode(),
            'des_pais_com': 'Brasil',
            'num_ddd_cob': faker.random_number(digits=2),
            'num_tel_cob': faker.random_number(digits=8),
            'des_lograd_end_cob': faker.street_address(),
            'num_endereco_cob': str(faker.building_number()),
            'des_compl_end_cob': faker.building_number(),
            'nom_bairro_cob': faker.street_name(),
            'nom_cidade_cob': faker.city(),
            'cod_estado_cob': faker.state_abbr(),
            'cod_cep_cob': faker.postcode(),
            'des_pais_cob': 'Brasil',
            'num_ddd_ent': faker.random_number(digits=2),
            'num_tel_ent': faker.random_number(digits=8),
            'des_lograd_end_ent': faker.street_address(),
            'num_endereco_ent': str(faker.building_number()),
            'des_compl_end_ent': faker.building_number(),
            'nom_bairro_ent': faker.street_name(),
            'nom_cidade_ent': faker.city(),
            'cod_estado_ent': faker.state_abbr(),
            'cod_cep_ent': faker.postcode(),
            'des_pais_ent': 'Brasil',
            'cod_estado_civil': faker.random_element(elements=('Solteiro', 'Casado', 'Divorciado', 'Viúvo')),
            'val_renda_cliente': int(random.uniform(1000, 10000)),
            'des_endereco_mac': faker.mac_address(),
            'nom_mae_cliente': faker.name(),
            'dth_inclusao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_ult_atu_cli': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'tip_sit_telefone_res': faker.random_element(elements=('Ativo', 'Inativo')),
            'tip_sit_telefone_ent': faker.random_element(elements=('Ativo', 'Inativo')),
            'tip_sit_telefone_com': faker.random_element(elements=('Ativo', 'Inativo')),
            'tip_sit_telefone_cob': faker.random_element(elements=('Ativo', 'Inativo')),
            'tip_sit_email': faker.random_element(elements=('Ativo', 'Inativo')),
            'tip_sit_telefone_cel': faker.random_element(elements=('Ativo', 'Inativo')),
            'id_cliente_so': faker.random_number(digits=10),
            'tip_origem_principal': faker.word(),
            'dat_efetivacao_crediario': faker.date_time().strftime('%Y-%m-%d %H:%M:%S')

        }
        data['cliente'].append(criar_cliente)

        criar_cliente_complemento = {
            'id_cliente': criar_cliente['id_cliente'],
            'tip_pessoa': criar_cliente['tip_pessoa'],
            'num_cpf_cnpj_cliente': criar_cliente['num_cpf_cnpj_cliente'],
            'cod_nacionalidade': faker.random_number(digits=3),
            'des_nacionalidade': faker.country(),
            'des_naturalidade_cidade': faker.city(),
            'cod_naturalidade_estado': faker.state_abbr(),
            'flg_pessoa_politicamente_exposta': faker.random_element(elements=('Sim', 'Não')),
            'flg_deficiente_visual': faker.random_element(elements=('Sim', 'Não')),
            'val_outra_renda_cliente': random.uniform(0, 5000),
            'nom_pai_cliente': faker.name(),
            'num_rg': faker.bothify(text='########-#'),
            'dat_emissao_rg': faker.date_between(start_date='-30y', end_date='today').strftime('%Y-%m-%d'),
            'cod_orgao_expedicao_rg': faker.word(),
            'cod_estado_emissao_rg': faker.state_abbr(),
            'num_cnh': faker.bothify(text='########-#'),
            'dat_validade_cnh': faker.date_between(start_date='today', end_date='+5y').strftime('%Y-%m-%d'),
            'num_seguranca_cnh': faker.bothify(text='######'),
            'cod_validacao_cnh': faker.random_number(digits=3),
            'dat_emissao_cnh': faker.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d'),
            'val_patrimonio_total': random.uniform(0, 1000000),
            'cod_profissao': faker.random_number(digits=4),
            'nom_profissao': faker.job(),
            'tip_origem_principal': faker.word(),
            'dth_ult_atu_so': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao_reg': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_nacionalidade_iso': faker.country_code(),
            'des_nacionalidade_iso': faker.country(),
            'cod_profissao_isco08': faker.random_number(digits=5),
            'nom_profissao_isco08': faker.job()
        }
        data['cliente_complemento'].append(criar_cliente_complemento)

        criar_cliente_item_perfil = {
            'id_cliente': criar_cliente['id_cliente'],
            'dth_primeiro_evento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_ultimo_evento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_ult_atu_cli': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dth_inclusao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'tip_origem': faker.word(),
            'id_cliente_so': faker.random_number(digits=10),
            'flg_evento': faker.random_element(elements=('Ativo', 'Inativo')),
            'des_evento': faker.word(),
            'qtd_evento': str(faker.random_number(digits=2)),
            'val_evento': str(faker.random_number(digits=5)),
            'cod_item_perfil': faker.random_number(digits=4)

        }
        data['cliente_item_perfil'].append(criar_cliente_item_perfil)

        criar_de_para_num_pfj_id_cdt_cpf = {
            'num_pfj': faker.random_number(digits=10),
            'num_cpf': faker.random_number(digits=11),
            'id_pessoa_cdt': faker.random_number(digits=10),
            'tip_origem_cdt': faker.word()

        }
        data['de_para_num_pfj_id_cdt_cpf'].append(criar_de_para_num_pfj_id_cdt_cpf)

        criar_v_estabelecimento = {
            'cod_estabelecimento': faker.random_number(digits=5),
            'num_cgc': faker.bothify(text='??.???/????-??'),
            'num_digto_estabelecimento': faker.random_digit(),
            'flg_ind_atividade': faker.random_element(elements=('Ativo', 'Inativo')),
            'flg_localizacao': faker.random_element(elements=('Urbano', 'Rural')),
            'flg_tipo_estabelecimento': faker.word(),
            'nom_estabelecimento': faker.company(),
            'flg_responsavel_mr': faker.random_element(elements=('Sim', 'Não')),
            'dat_ult_atu': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'est_sgl_estado': faker.state_abbr(),
            'dat_fechamento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dat_ult_reforma': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'nom_fantasia': faker.company(),
            'nom_gerente_adm': faker.name(),
            'nom_gerente_comercial': faker.name(),
            'dat_abertura': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'num_inscricao_estadual': faker.bothify(text='??????????'),
            'num_inscricao_municipal': faker.bothify(text='??????????'),
            'dat_inauguracao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'nom_fantasia_mkt': faker.company(),
            'cod_corporacao': faker.random_number(digits=4),
            'nom_razao_social': faker.company(),
            'cod_regional': faker.random_number(digits=3),
            'des_regional': faker.word(),
            'nom_gerente': faker.name(),
            'cod_micro_regiao': faker.random_number(digits=3),
            'des_micro_regiao': faker.word(),
            'cod_estabelecimento_cdt': faker.random_number(digits=5),
            'cod_estabelecimento_onefpay': faker.random_number(digits=5)
        }
        data['v_estabelecimento'].append(criar_v_estabelecimento)

    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_unificacao_cliente(num_records)

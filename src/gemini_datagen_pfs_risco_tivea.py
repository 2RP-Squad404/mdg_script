from faker import Faker
import itertools
from datetime import date, datetime
import random 
import re

faker = Faker('pt_BR')
id_serial = itertools.count(start=0)

# Este arquivo possui as funções geradoras para a tabelas do dataset: 'pfs_risco_tivea'

def criar_cartao_faker():
    return {
        "id_cartao": next(id_serial),
        "id_produto_cartao": faker.random_int(min=5, max=7),
        "num_cartao": faker.credit_card_number(),
        "num_seq_via_cartao": faker.random_int(min=2, max=7),
        "id_conta": faker.random_int(min=1397165, max=24861863),
        "num_cpf_cliente": re.sub(r'\D','',faker.cpf()),
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



def criar_cobranca_campo_customizavel_faker():
    return {
        "id_cliente_cobranca": str(next(id_serial)),
        "nom_campo": faker.random_element(elements=['REACORDO','NOVO_LIMITE','ESTRATEGIA4']),
        "val_campo": faker.random_element(elements=['SERVICE_PREMIUM', 'TUDO JUSTO', 'SERASA', 'VALIDU', 'Portal Pefisa - PPN', 'DIGICOB TECNOLOGIA LTDA']),
        "dat_referencia": faker.date_this_year().strftime('%Y-%m-%d')
    }

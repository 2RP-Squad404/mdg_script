
from faker import Faker
from datetime import datetime, date

faker = Faker('pt_BR')

def criar_transacao_corrente_faker():
    return {
        "hash_key": faker.uuid4(),
        "source": faker.random_number(digits=12),
        "tc_id_transacao": faker.random_int(),
        "tc_id_tipotransacao": faker.random_int(),
        "tc_id_emissor": faker.random_int(),
        "tc_id_produto": faker.random_int(),
        "tc_id_conta": faker.random_int(),
        "tc_portador": faker.random_int(),
        "tc_sequencialcartao": faker.random_int(),
        "tc_datavencimentoreal": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_datavencimentopadrao": faker.date_this_year().strftime('%d/%m/%Y'),
        "tc_datageracao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_valor": faker.pyfloat(left_digits=2, right_digits=2, positive=True),
        "tc_historico": faker.sentence(),
        "tc_statuscontabil": faker.random_int(),
        "tc_statusgerencial": faker.random_int(),
        "tc_id_eventoexterno": faker.random_int(),
        "tc_dataorigem": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_statusconta": faker.random_int(),
        "tc_faturado": faker.random_int(),
        "tc_id_estabelecimento": faker.random_int(),
        "tc_datafaturamento": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_complemento": faker.sentence(),
        "tc_id_transacaoestorno": faker.random_int(),
        "tc_flagestornado": faker.random_int(),
        "tc_parcela": faker.random_int(),
        "tc_plano": faker.random_int(),
        "tc_id_estabelecimento_visa": faker.random_int(),
        "tc_id_planocredito": faker.random_int(),
        "tc_id_processoprocedure": faker.random_int(),
        "tc_datavencpadrao": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "tc_id_taxajurosapropriacao": faker.random_int(),
        "dh_relatorio": faker.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        "operation": faker.word(),
        "operation_sequence": faker.random_int(),
        "production_date": faker.date_this_year().strftime('%Y-%m-%d')
    }

from datetime import timezone
from faker import Faker

from jsonl_convert import jsonl_data,input_num_linhas

faker = Faker('pt_BR')

def criar_pfs_raw_funcao(num_records):
    data = {'v_contrato': []}
    for _ in range(num_records):
        criar_dados_cliente = {
            'nome': faker.name(),
            'documento_cliente': faker.bothify(text='###########'),
            'matricula': faker.bothify(text='########'),
            'email': faker.email(),
            'sexo': faker.random_element(elements=('Masculino', 'Feminino')),
            'ddd_celular': faker.random_number(digits=2),
            'telefone_celular': faker.bothify(text='#########'),
            'data_nascimento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'banco_pagamento': faker.word(),
            'agencia_pagamento': faker.word(),
            'conta_corrente_pagamento': faker.word(),
            'digito_conta_corrente': faker.random_number(digits=1)
        }

        criar_parcelas_abertas = {
            'data_vencimento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'movimentacoes': {"key": faker.word()},
            'numero_parcela': faker.random_number(digits=2),
            'qtde_atraso': faker.random_int(),
            'dias_cobranca_multa': faker.random_int(),
            'desconto_antecipacao_concedido': faker.word(),
            'cancelado': faker.boolean(),
            'saldo_devedor': faker.pyfloat(),
            'valor_despesa': faker.pyfloat(),
            'valor_iof_atraso': faker.pyfloat(),
            'valor_juros_parcela': faker.pyfloat(),
            'valor_mora': faker.pyfloat(),
            'valor_multa': faker.pyfloat(),
            'valor_parcela': faker.pyfloat(),
            'valor_presente': faker.pyfloat(),
            'valor_principal_parcela': faker.pyfloat(),
            'valor_tarifa': faker.pyfloat(),
        }

        criar_parcelas_liquidadas = {
            'data_liquidacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'data_vencimento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dias_cobranca_multa': faker.random_int(),
            'desconto_antecipacao_concedido': faker.pyfloat(),
            'cancelado': faker.boolean(),
            'movimentacoes': {"key": faker.word()},
            'numero_parcela': faker.random_number(digits=2),
            'valor_juros_parcela': faker.pyfloat(),
            'valor_parcela': faker.pyfloat(),
            'valor_principal_parcela': faker.pyfloat(),
        }

        criar_v_contrato = {
            'production_date': faker.date_between(start_date='-30y', end_date='today').strftime('%Y-%m-%d'),
            'codigo_do_produto': faker.word(),
            'numero_operacao': faker.word(),
            'numero_pedido': faker.word(),
            'numero_proposta': faker.word(),
            'tipo_operacao': faker.word(),
            'banco_portabilidade': faker.word(),
            'numero_carteira': faker.word(),
            'produto': faker.word(),
            'descricao_convenio': faker.paragraph(),
            'modalidade_produto': faker.word(),
            'login_chapa': faker.word(),
            'data_base': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'data_emissao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'data_vencimento_operacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'status_contrato': faker.word(),
            'estornado_em': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'status_pagamento_funcao': faker.word(),
            'valor_troco': faker.word(),
            'tipo_de_pagamento': faker.word(),
            'empresa': faker.word(),
            'matriz': faker.word(),
            'regional': faker.word(),
            'promotora': faker.word(),
            'empregador': faker.word(),
            'orgao': faker.word(),
            'a1O2': faker.word(),
            'seguro': faker.word(),
            'agente_certificado_chapa': faker.word(),
            'agente_certificado_cpf': faker.bothify(text='###########'),
            'representante_legal_cpf': faker.bothify(text='###########'),
            'representante_legal_nome': faker.name(),
            'correspondente': faker.word(),
            'digitador': faker.word(),
            'qtde_parcelas_em_aberto': faker.random_int(),
            'qtde_parcelas_pagas': faker.random_int(),
            'qtde_parcelas_em_atraso': faker.random_int(),
            'taxa_juros_cl_ano': faker.word(),
            'taxa_juros_cl_mes': faker.word(),
            'taxa_apropriacao_ano': faker.word(),
            'taxa_apropriacao_mes': faker.word(),
            'taxa_cet_mes': faker.word(),
            'taxa_iof': faker.word(),
            'taxa_iof_complementar': faker.word(),
            'valor_principal': faker.word(),
            'valor_juros_contratado': faker.word(),
            'valor_TAC': faker.word(),
            'valor_bruto': faker.word(),
            'valor_IOF': faker.word(),
            'valor_mora': faker.pyfloat(),
            'valor_perc_mora': faker.word(),
            'valor_multa': faker.pyfloat(),
            'valor_perc_multa': faker.word(),
            'valor_do_iof_vencido': faker.word(),
            'valor_saldo': faker.word(),
            'dados_cliente': criar_dados_cliente,
            'parcelas_abertas': criar_parcelas_abertas,
            'parcelas_liquidadas': criar_parcelas_liquidadas
        }
        data['v_contrato'].append(criar_v_contrato)

    jsonl_data(data=data)
    return data

num_records=input_num_linhas()
criar_pfs_raw_funcao(num_records)


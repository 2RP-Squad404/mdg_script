from faker import Faker

from jsonl_convert import input_num_linhas, jsonl_data

fake = Faker('pt_BR')

def fake_date():
    return fake.date_time().strftime('%Y-%m-%d')

def fake_datetime():
    return fake.date_time().strftime('%Y-%m-%d %H:%M:%S')

def fake_dict():
    return {'key1': fake.word(), 'key2': fake.random_int()}

def fake_str():
    return fake.word()

def function_pfs_raw_onidata(num_records):
    data = {'v_credito_pessoal_contratos': []}
    for _ in range(num_records):
        criar_assinatura_info = {
            'browser': fake.user_agent(),
            'data': fake_date(),
            'ip': fake.ipv4()
        }

        criar_canal = {
            'id': fake.random_number(digits=5, fix_len=True),
            'nome': fake.word()
        }

        criar_cliente_info_no_contrato = {
            'cargo': fake.job(),
            'conjuge': fake.name(),
            'cpf': fake.cpf(),
            'data_nascimento': fake_date(),
            'documento': fake_dict(),
            'email': fake.email(),
            'endereco': fake_dict(),
            'escolaridade': fake.random_element(elements=('Ensino Fundamental', 'Ensino Médio', 'Superior')),
            'estado_civil': fake.random_element(elements=('Solteiro', 'Casado', 'Divorciado', 'Viúvo')),
            'nacionalidade': fake.country(),
            'nascimento_uf': fake.state_abbr(),
            'nome': fake.name(),
            'nome_mae': fake.name(),
            'nome_pai': fake.name(),
            'pagamento': fake_dict(),
            'resourcetype': fake_str(),
            'salario': fake.numerify(text='R$#######,##'),
            'salario_bruto': fake.random_number(digits=7, fix_len=True),
            'salario_liquido': fake.numerify(text='R$#######,##'),
            'sexo': fake.random_element(elements=('Masculino', 'Feminino')),
            'sobrenome': fake.last_name(),
            'telefone_celular': fake.phone_number(),
            'telefone_fixo': fake.phone_number()
        }

        criar_documentacao_comprovacao = {
            'identidade_frente': fake_dict(),
            'identidade_verso': fake_dict(),
            'renda': fake_dict(),
            'residencia': fake_dict()
        }

        criar_financeira = {
            'cnpj': fake.cnpj(),
            'id': fake.random_number(digits=5, fix_len=True),
            'nome_fantasia': fake.company(),
            'razao_social': fake.company()
        }

        criar_metadados = {
            'PEFISA': fake_dict(),
            'PEFISA_FGTS': fake_dict()
        }

        criar_parcelas_info = {
            'em_atraso': fake_dict(),
            'pagas': fake_dict(),
            'pendentes': fake_dict()
        }

        criar_v_credito_pessoal_contratos = {
            'production_date': fake_date(),
            'dth_inclusao': fake_datetime(),
            'assinatura_info': criar_assinatura_info,
            'canal': criar_canal,
            'canal_atendimento': fake.random_element(elements=('Telefone', 'Online', 'Presencial')),
            'cargo': fake.job(),
            'ccb_original_html': fake_str(),
            'ccb_original_pdf': fake_str(),
            'cliente': fake_str(),
            'cliente_info_no_contrato': criar_cliente_info_no_contrato,
            'cpf': fake.cpf(),
            'cpf_operador': fake.cpf(),
            'data_efetivacao': fake_date(),
            'data_nascimento': fake_date(),
            'data_pagamento': fake_date(),
            'data_primeiro_vencimento': fake_date(),
            'data_solicitacao': fake_date(),
            'data_ultimo_vencimento': fake_date(),
            'dias_cobranca_multa': fake.random_int(min=1, max=30),
            'documentacao_comprovacao': criar_documentacao_comprovacao,
            'email': fake.email(),
            'escolaridade': fake.random_element(elements=('Ensino Fundamental', 'Ensino Médio', 'Superior')),
            'estado_civil': fake.random_element(elements=('Solteiro', 'Casado', 'Divorciado', 'Viúvo')),
            'financeira': criar_financeira,
            'financeira_valor_a_pagar': fake.random_number(digits=8, fix_len=True),
            'gerado_em': fake_datetime(),
            'id': fake.uuid4(),
            'localizador': fake.bothify(text='???-####'),
            'METADADOS': criar_metadados,
            'modalidade': fake_str(),
            'nacionalidade': fake.country(),
            'nascimento_uf': fake.state_abbr(),
            'nome': fake.name(),
            'nome_mae': fake.name(),
            'nome_operador': fake.name(),
            'nome_pai': fake.name(),
            'origem': fake_str(),
            'parcelas_info': criar_parcelas_info,
            'prazo': fake.random_int(min=1, max=120),
            'proposta': fake.bothify(text='####-#####'),
            'salario_bruto': fake.random_number(digits=7, fix_len=True),
            'salario_liquido': fake.numerify(text='R$#######,##'),
            'saldo_devedor': fake.random_number(digits=8, fix_len=True),
            'sexo': fake.random_element(elements=('Masculino', 'Feminino')),
            'sobrenome': fake.last_name(),
            'status': fake_str(),
            'status_alterado_em': fake_datetime(),
            'taxa_cet_mes': fake.random_number(digits=4, fix_len=True),
            'taxa_contrato': fake.random_number(digits=4, fix_len=True),
            'taxa_iof': fake.random_number(digits=4, fix_len=True),
            'taxa_iof_complementar': fake.random_number(digits=4, fix_len=True),
            'taxa_irr': fake.random_number(digits=4, fix_len=True),
            'taxa_multa': fake.random_number(digits=4, fix_len=True),
            'taxa_permanencia': fake.random_number(digits=4, fix_len=True),
            'telefone_celular': fake.phone_number(),
            'telefone_fixo': fake.phone_number(),
            'valor_financiado': fake.random_number(digits=8, fix_len=True),
            'valor_iof': fake.random_number(digits=7, fix_len=True),
            'valor_juros': fake.random_number(digits=8, fix_len=True),
            'valor_liberado': fake.random_number(digits=8, fix_len=True),
            'valor_parcela': fake.random_number(digits=7, fix_len=True),
            'valor_recebivel': fake.random_number(digits=8, fix_len=True),
            'valor_seguro': fake.random_number(digits=7, fix_len=True),
            'valor_tarifas': fake.random_number(digits=7, fix_len=True)
        }
        data['v_credito_pessoal_contratos'].append(criar_v_credito_pessoal_contratos)

    jsonl_data(data=data)
    return data

num_records = input_num_linhas()
function_pfs_raw_onidata(num_records)
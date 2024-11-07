import uuid

from faker import Faker

fake = Faker('pt_BR')


def criar_acordo():
    id_serial = iter(range(1, 10000))
    return {
        'source': [fake.url() for _ in range(4)],
        'id': [str(next(id_serial)) for _ in range(3)],
        'cliente': [fake.random_number(digits=10) for _ in range(4)],
        'cobrador': [fake.random_number(digits=16) for _ in range(1)],
        'tipo': ['ACORDO', 'RENEGOCIACAO'],
        'numeroAcordo': [fake.random_number(digits=7) for _ in range(3)],
        'numeroParcelas': [fake.random_number(digits=1) for _ in range(3)],
        'dataOperacao': [
            fake.date_this_year().strftime('%Y-%m-%d') for _ in range(3)
        ],
        'dataEmissao': [
            fake.date_this_year().strftime('%Y-%m-%d') for _ in range(3)
        ],
        'dataProcessamento': [
            fake.date_this_year().strftime('%Y-%m-%d') for _ in range(3)
        ],
        'dataHoraInclusao': [
            fake.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S')
            for _ in range(3)
        ],
        'dataHoraModificacao': [
            fake.date_time_this_year().strftime('%Y-%m-%dT%H:%M:%S')
            for _ in range(3)
        ],
        'dataVencimento': [
            fake.date_between(start_date='+1y', end_date='+2y').strftime(
                '%Y-%m-%d'
            )
            for _ in range(3)
        ],
        'situacao': [
            'NAO_CUMPRIDO',
            'CANCELADO',
            'LIQUIDADO',
            'PENDENTE',
            'RENEGOCIADO',
        ],
        'taxaOperacao': [
            str(fake.pyfloat(left_digits=1, right_digits=2, positive=True))
            for _ in range(4)
        ],
        'valorPagoTributo': ['0.00'],
        'valorPrincipal': [
            str(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
            for _ in range(4)
        ],
        'valorJuros': [
            str(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
            for _ in range(5)
        ],
        'valorTarifa': ['0.00'],
        'valorTributo': [
            str(fake.pyfloat(left_digits=2, right_digits=2, positive=True))
            for _ in range(4)
        ],
        'valorAdicionado': ['0.00'],
        'valorTotal': [
            str(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
            for _ in range(4)
        ],
        'saldoPrincipal': [
            str(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
            for _ in range(3)
        ],
        'saldoTotal': [
            str(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
            for _ in range(3)
        ],
        'saldoAtual': [
            str(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
            for _ in range(3)
        ],
        'diasAtraso': [fake.random_int(-6, 5) for _ in range(8)],
        'motivoCancelamento': [fake.json() for _ in range(2)],
        'negociacao': [
            {
                'id': str(uuid.uuid4()),
                'nome': fake.sentence(),
                'descricao': fake.sentence(),
                'situacao': 'INATIVO',
                'tipo': 'ACORDO',
                'gestao': 'EXTERNO',
                'cor': '#2412eb',
                'icone': 'money',
                'tipoDesconto': 'PARCELAMENTO',
                'modalidade': {
                    'id': str(uuid.uuid4()),
                    'nome': fake.sentence(),
                    'tipo': 'ACORDO',
                    'situacao': 'ATIVO',
                    'gestao': 'EXTERNO',
                    'cor': '#2412eb',
                    'valorDistorcao': '0.00',
                    'percentualDistorcao': '0.00',
                    'atrasoMaximo': '31',
                    'atrasoEntrada': '4',
                    'acaoOrigemLiquidaca': 'LIQUIDAR',
                },
            }
            for _ in range(3)
        ],
        'criterioTributo': ['FINANCIA'],
        'produto': [
            {
                'id': str(uuid.uuid4()),
                'idExterno': fake.word(),
                'nome': fake.word(),
                'descricao': fake.sentence(),
            }
            for _ in range(4)
        ],
        'tributo': [
            {
                'id': str(uuid.uuid4()),
                'nome': fake.word(),
                'percentual': str(
                    fake.pyfloat(left_digits=1, right_digits=7, positive=True)
                ),
                'percentualFixo': str(
                    fake.pyfloat(left_digits=1, right_digits=2, positive=True)
                ),
                'percentualMaximo': str(
                    fake.pyfloat(left_digits=1, right_digits=2, positive=True)
                ),
                'arredondamento': 'BAIXO',
                'dataCalculo': 'VENCIMENTO',
            }
            for _ in range(1)
        ],
        'meioPagamento': [
            {
                'id': str(uuid.uuid4()),
                'tipo': 'BOLETO',
                'nome': fake.word(),
                'cobrador': {
                    'id': str(uuid.uuid4()),
                    'nome': fake.word(),
                    'banco': fake.random_number(digits=3),
                },
            }
            for _ in range(4)
        ],
        'usuario': [
            {'id': str(uuid.uuid4()), 'nome': fake.word()} for _ in range(3)
        ],
        'assessoria': [
            {'id': str(uuid.uuid4()), 'nome': fake.word()} for _ in range(3)
        ],
        'parcelas': [
            [
                {
                    'id': str(uuid.uuid4()),
                    'acordo': str(uuid.uuid4()),
                    'numeroParcela': '0',
                    'dataVencimento': fake.date_between(
                        start_date='+1y', end_date='+2y'
                    ).strftime('%Y-%m-%d'),
                    'situacao': 'ABERTO',
                    'nossoNumero': fake.random_number(digits=10),
                    'valorPrincipal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'valorJuros': '0.00',
                    'valorTarifa': '0.00',
                    'valorAdicionado': '0.00',
                    'valorTotal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'valorTributo': str(
                        fake.pyfloat(
                            left_digits=1, right_digits=2, positive=True
                        )
                    ),
                    'valorBaseTributo': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'valorPermanencia': '0.00',
                    'valorMora': '0.00',
                    'valorMulta': '0.00',
                    'saldoPrincipal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'saldoTotal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'saldoAtual': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'registrado': True,
                },
                {
                    'id': str(uuid.uuid4()),
                    'acordo': str(uuid.uuid4()),
                    'numeroParcela': '1',
                    'dataVencimento': fake.date_between(
                        start_date='+1y', end_date='+2y'
                    ).strftime('%Y-%m-%d'),
                    'situacao': 'ABERTO',
                    'nossoNumero': fake.random_number(digits=10),
                    'valorPrincipal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'valorJuros': '0.00',
                    'valorTarifa': '0.00',
                    'valorAdicionado': '0.00',
                    'valorTotal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'valorTributo': str(
                        fake.pyfloat(
                            left_digits=1, right_digits=2, positive=True
                        )
                    ),
                    'valorBaseTributo': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'valorPermanencia': '0.00',
                    'valorMora': '0.00',
                    'valorMulta': '0.00',
                    'saldoPrincipal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'saldoTotal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'saldoAtual': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'registrado': True,
                },
            ]
            for _ in range(1)
        ],
        'pagamentos': [
            [
                {
                    'id': str(uuid.uuid4()),
                    'dataProcessamento': fake.date_this_year().strftime(
                        '%Y-%m-%d'
                    ),
                    'dataLiquidacao': fake.date_this_year().strftime(
                        '%Y-%m-%d'
                    ),
                    'dataCredito': None,
                    'dataCnab': None,
                    'dataOperacao': fake.date_this_year().strftime('%Y-%m-%d'),
                    'dataHoraInclusao': fake.date_time_this_year().strftime(
                        '%Y-%m-%dT%H:%M:%S'
                    ),
                    'formaLiquidacao': 'DINHEIRO',
                    'valorRecebido': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'valorDesconto': '0.00',
                    'valorEncargos': '0.00',
                    'valorDistorcao': '0.00',
                    'valorSobra': '0.00',
                    'situacao': 'ATIVO',
                    'integracao': 'CONCLUIDO',
                    'agrupador': None,
                    'abatimentos': [
                        {
                            'id': str(uuid.uuid4()),
                            'origem': str(uuid.uuid4()),
                            'valorPrincipal': str(
                                fake.pyfloat(
                                    left_digits=2,
                                    right_digits=2,
                                    positive=True,
                                )
                            ),
                            'valorTotal': str(
                                fake.pyfloat(
                                    left_digits=2,
                                    right_digits=2,
                                    positive=True,
                                )
                            ),
                            'valorPermanencia': str(
                                fake.pyfloat(
                                    left_digits=1,
                                    right_digits=2,
                                    positive=True,
                                )
                            ),
                            'valorMora': '0.00',
                            'valorMulta': '0.00',
                            'valorOutros': '0.00',
                            'valorDesconto': '0.00',
                            'valorJuros': '0.00',
                            'valorTarifa': '0.00',
                            'valorTributo': '0.00',
                            'valorAdicionado': '0.00',
                            'valorAtual': str(
                                fake.pyfloat(
                                    left_digits=2,
                                    right_digits=2,
                                    positive=True,
                                )
                            ),
                            'percentual': '100.000000000000',
                            'tipo': 'TOTAL',
                            'integracao': 'CONCLUIDO',
                            'mensagemIntegracao': None,
                            'dataHoraIntegracao': fake.date_time_this_year().strftime(
                                '%Y-%m-%dT%H:%M:%S'
                            ),
                        }
                    ],
                    'liquidacoes': [
                        {
                            'id': str(uuid.uuid4()),
                            'parcela': str(uuid.uuid4()),
                            'valorPrincipal': str(
                                fake.pyfloat(
                                    left_digits=2,
                                    right_digits=2,
                                    positive=True,
                                )
                            ),
                            'valorTotal': str(
                                fake.pyfloat(
                                    left_digits=2,
                                    right_digits=2,
                                    positive=True,
                                )
                            ),
                            'valorJuros': '0.00',
                            'valorEncargos': '0.00',
                            'valorDesconto': '0.00',
                            'valorDistorcao': '0.00',
                            'diasAtraso': '0',
                            'numeroParcela': '0',
                            'tipo': 'TOTAL',
                        }
                    ],
                }
            ]
            for _ in range(1)
        ],
        'origens': [
            [
                {
                    'id': str(uuid.uuid4()),
                    'valorContabil': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'descontoContabil': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'saldoContabil': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'contrato': fake.random_number(digits=8),
                    'contratoId': str(uuid.uuid4()),
                    'numeroContrato': fake.random_number(digits=11),
                    'parcela': '1',
                    'parcelaId': str(uuid.uuid4()),
                    'numeroParcela': '1',
                    'diasAtraso': fake.random_int(0, 100),
                    'ordem': '1',
                    'dataVencimento': fake.date_this_year().strftime(
                        '%Y-%m-%d'
                    ),
                    'nossoNumero': None,
                    'notaFiscal': None,
                    'situacao': 'CANCELADO',
                    'valorPrincipal': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'valorTotal': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'valorPermanencia': '0.00',
                    'valorMora': '0.00',
                    'valorMulta': '0.00',
                    'valorOutros': '0.00',
                    'valorDesconto': '0.00',
                    'valorJuros': '0.00',
                    'valorTarifa': '0.00',
                    'valorAdicionado': '0.00',
                    'valorAtual': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'saldoPrincipal': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'saldoTotal': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'saldoPermanencia': '0.00',
                    'saldoMora': '0.00',
                    'saldoMulta': '0.00',
                    'saldoOutros': '0.00',
                    'saldoDesconto': '0.00',
                    'saldoJuros': '0.00',
                    'saldoTarifa': '0.00',
                    'saldoAdicionado': '0.00',
                    'saldoAtual': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'descontoPrincipal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                    'descontoJuros': '0.00',
                    'descontoMora': '0.00',
                    'descontoMulta': '0.00',
                    'descontoOutros': '0.00',
                    'descontoPermanencia': str(
                        fake.pyfloat(
                            left_digits=3, right_digits=2, positive=True
                        )
                    ),
                    'descontoTotal': str(
                        fake.pyfloat(
                            left_digits=2, right_digits=2, positive=True
                        )
                    ),
                }
            ]
            for _ in range(2)
        ],
        'pendencias': [[[] for _ in range(40)]],
        'production_date': [fake.date_this_year().strftime('%Y-%m-%d')],
    }

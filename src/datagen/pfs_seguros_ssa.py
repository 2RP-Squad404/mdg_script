from faker import Faker
from jsonl_convert import input_num_linhas, jsonl_data

faker = Faker('pt_BR')


def fake_int():
    return faker.random_int()


def fake_float():
    return faker.pyfloat(left_digits=2, right_digits=2, positive=True)


def fake_str():
    return faker.word()



def pfs_seguros_ssa(num_records):
    data = {
        'parcela_seguro': [],
        'cliente': [],
        'endereco': [],
        'pessoa': [],
        'estabelecimento': [],
        'adesao_seguro': [],
        'participante': [],
        'agrupamento_produto_seguro': [],
        'plano_seguro': [],
        'adesao_seguro_item': [],
        'seguradora': [],
        'objeto_seguro': [],
        'produto_venda': [],
        'canal_venda': [],
        'produto_seguro': [],
        'adesao_participacao': [],
    }
    for _ in range(num_records):
        parcela_seguro = {
            'id_ParcelaSeguro': fake_int(),
            'id_AdesaoSeguro': fake_int(),
            'no_Parcela': fake_int(),
            'dt_Vencimento': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'vl_Parcela': fake_float(),
            'tp_Situacao': fake_int(),
            'dt_Situacao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dt_Emissao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'tp_SituacaoCobranca': fake_int(),
            'tp_SituacaoTransferencia': fake_int(),
            'no_TituloCapitalizacao': fake_str(),
            'fl_PagamentoPDV': faker.boolean(),
            'dt_EnvioCobranca': faker.date_time().strftime('%Y-%m-%d'),
            'dt_PostagemParcela': faker.date_time().strftime('%Y-%m-%d'),
            'dt_Liquidacao': faker.date_time().strftime('%Y-%m-%d'),
            'tp_FormaPagamento': fake_int(),
            'dt_SituacaoCobranca': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dt_SituacaoTransferencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'no_TentativasLancamentosContaDigital': fake_int(),
            'id_ArquivoExportacaoDados': fake_int(),
            'id_ParcelaPIN': fake_int(),
            'tp_StatusIntegracaoParcelaGS': fake_int(),
            'id_RetornoProcessadora': fake_int(),
            'tp_AjusteLancado': fake_int(),
            'dt_LiquidacaoHoraReal': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['parcela_seguro'].append(parcela_seguro)

    for _ in range(num_records):
        cliente = {
            'id_cliente': fake_int(),
            'id_emissor': fake_int(),
            'tp_cliente': fake_int(),
            'no_conta': fake_str(),
            'tp_cartao': fake_int(),
            'no_diavencimento': fake_int(),
            'tp_titularidade': fake_int(),
            'id_pessoa': fake_int(),
            'tp_statusintegracaocliente': fake_int(),
            'fl_contacredito': faker.boolean(),
            'fl_grade': faker.boolean(),
            'data_cdcbi': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['cliente'].append(cliente)

    for _ in range(num_records):
        endereco = {
            'id_Endereco': fake_int(),
            'nm_Logradouro': fake_str(),
            'no_Logradouro': fake_str(),
            'dc_Complemento': fake_str(),
            'nm_Bairro': fake_str(),
            'nm_Municipio': fake_str(),
            'cd_UF': faker.bothify(text='??'),
            'no_CEP': faker.bothify(text='#####-###'),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['endereco'].append(endereco)

    for _ in range(num_records):
        pessoa = {
            'id_Pessoa': fake_int(),
            'nm_Pessoa': faker.name(),
            'no_CPF': faker.bothify(text='###.###.###-##'),
            'dt_Nascimento': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'tp_Sexo': fake_int(),
            'nm_Mae': faker.name(),
            'no_RG': fake_str(),
            'dt_EmissaoRG': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'cd_UF_RG': faker.bothify(text='??'),
            'no_PIS': fake_str(),
            'no_CNS': fake_str(),
            'no_DeclaracaoNascidoVivo': fake_str(),
            'tp_EstadoCivil': fake_int(),
            'tp_GrauParentesco': fake_int(),
            'id_Endereco': fake_int(),
            'id_Contato': fake_int(),
            'tp_Pessoa': fake_str(),
            'fl_ApenasResponsavelFinanceiro': faker.boolean(),
            'id_IntegracaoParceiro': fake_int(),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['pessoa'].append(pessoa)

    for _ in range(num_records):
        estabelecimento = {
            'id_Estabelecimento': fake_int(),
            'id_Emissor': fake_int(),
            'no_CNPJ': faker.bothify(text='##.###.###/####-##'),
            'cd_Estabelecimento': fake_str(),
            'nm_Estabelecimento': faker.company(),
            'id_Endereco': fake_int(),
            'id_Contato': fake_int(),
            'fl_Ativo': faker.boolean(),
            'no_SerieNFE': fake_str(),
            'cd_Servico': fake_str(),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['estabelecimento'].append(estabelecimento)

    for _ in range(num_records):
        adesao_seguro = {
            'id_adesaoseguro': fake_int(),
            'id_emissor': fake_int(),
            'id_cliente': fake_int(),
            'id_produtoseguro': fake_int(),
            'id_planoseguro': fake_int(),
            'id_estabelecimento': fake_int(),
            'dt_emissao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dt_iniciovigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dt_terminovigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'no_certificado': fake_float(),
            'id_objetoseguro': fake_int(),
            'id_produtovenda': fake_int(),
            'vl_objetoseguro': fake_float(),
            'dt_vendaproduto': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'vl_franquia': fake_float(),
            'id_localrisco': fake_int(),
            'tp_situacaoseguro': fake_int(),
            'dt_situacaoseguro': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'vl_premioliquido': fake_float(),
            'vl_iof': fake_float(),
            'vl_premiototal': fake_float(),
            'tp_situacaotransferencia': fake_int(),
            'vl_restituido': fake_float(),
            'tp_cancelamento': fake_int(),
            'no_ultimaparcelaemitida': fake_int(),
            'id_motivocancelamento': fake_int(),
            'cd_canalvenda': fake_str(),
            'vl_prolabore': fake_float(),
            'dc_observacaocancelamento': fake_str(),
            'no_parcelas': fake_int(),
            'no_notafiscal': fake_int(),
            'no_serieprodutovenda': fake_str(),
            'no_bilhete': fake_str(),
            'dt_adesao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'vl_iofrestituido': fake_float(),
            'id_documentosafedoc': fake_int(),
            'id_estabelecimentocancelamento': fake_int(),
            'dt_emissaoproxparcela': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dt_emissaoultparcela': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'no_pin': fake_int(),
            'vl_comissaosegurada': fake_float(),
            'id_canalvenda': fake_int(),
            'tp_canalvenda': fake_int(),
            'dt_cancelamentofimvigencia': faker.date_time().strftime('%Y-%m-%d'),
            'id_safedocassinatura': fake_int(),
            'cd_planoenquadramento': fake_str(),
            'id_arquivoexportacaodados': fake_int(),
            'tp_statusintegracaogs': fake_int(),
            'dc_observacaostatus': fake_str(),
            'fl_seguroquitado': faker.boolean(),
            'vl_restituidoviacartao': fake_float(),
            'no_contrato': fake_str(),
            'no_mesescarencia': fake_int(),
            'dt_emissaohora': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'id_documentosafedoc_new': fake_int(),
            'id_safedocassinatura_new': fake_int(),
            'id_safedocassinatura_old': fake_int(),
            'id_documentosafedoc_old': fake_int(),
            'dt_emissaohorareal': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'data_cdcbi': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['adesao_seguro'].append(adesao_seguro)

    for _ in range(num_records):
        participante = {
            'id_Participante': fake_int(),
            'tp_Participante': fake_int(),
            'cd_Participante': fake_str(),
            'id_Estabelecimento': fake_int(),
            'nm_Participante': faker.name(),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['participante'].append(participante)

    for _ in range(num_records):
        agrupamento_produto_seguro = {
            'id_AgrupamentoProdutoSeguro': fake_int(),
            'nm_Agrupamento': fake_str(),
            'dc_TermoAceite': fake_str(),
            'no_OrdemApresentacao': fake_int(),
            'id_Emissor': fake_int(),
            'fl_Ativo': faker.boolean(),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['agrupamento_produto_seguro'].append(agrupamento_produto_seguro)

    for _ in range(num_records):
        plano_seguro = {
            'id_PlanoSeguro': fake_int(),
            'id_ProdutoSeguro': fake_int(),
            'cd_PlanoEmissor': fake_str(),
            'nm_PlanoSeguro': fake_str(),
            'dc_PlanoSeguro': fake_str(),
            'nm_ProdutoPlano': fake_str(),
            'dt_InicioVigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dt_TerminoVigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'no_MesesVigencia': fake_int(),
            'fl_InformarMesesVigencia': faker.boolean(),
            'dc_PrefixoCertificado': fake_str(),
            'dc_MascaraCertificado': fake_str(),
            'qt_TitulosCapitalizacao': fake_int(),
            'fl_InformarQtdNumerosSorte': faker.boolean(),
            'fl_InformarNumerosSorte': faker.boolean(),
            'dc_MascaraNumeroSorte': fake_str(),
            'qt_LoteNumerosSorte': fake_int(),
            'fl_EmissaoTituloCapitalizacaoMensal': faker.boolean(),
            'tp_CobrancaRepasse': fake_int(),
            'tp_VigenciaFutura': fake_int(),
            'no_DiasVigenciaFutura': fake_int(),
            'id_ConjuntoTituloCapitalizacao': fake_int(),
            'id_OperacaoCobranca': fake_int(),
            'id_OperacaoEstorno': fake_int(),
            'dc_Completa': fake_str(),
            'dc_RiscosExcluidos': fake_str(),
            'dc_TermoAdesao': fake_str(),
            'fl_ExtratoIncondicional': faker.boolean(),
            'fl_DebitoIncondicional': faker.boolean(),
            'tp_Garantia': fake_str(),
            'fl_RenovacaoAutomatica': faker.boolean(),
            'fl_ReenviarEmail': faker.boolean(),
            'dt_InicioVigenciaRenovacaoAutomatica': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'vl_Plano': fake_float(),
            'id_TipoAjusteDebito': fake_int(),
            'id_TipoAjusteEstorno': fake_int(),
            'fl_AceitaLancamentoNaAdesao': faker.boolean(),
            'id_ConjuntoPIN': fake_int(),
            'dc_MascaraPIN': fake_str(),
            'fl_RecebeInfoPinAdesao': faker.boolean(),
            'dc_MascaraSeriePIN': fake_str(),
            'dc_MascaraLotePIN': fake_str(),
            'fl_AceitaItem': faker.boolean(),
            'fl_ObtemValorNoPlano': faker.boolean(),
            'id_AjusteRestituicaoCredito': fake_int(),
            'id_AjusteRestituicaoDebito': fake_int(),
            'no_mesesCarencia': fake_int(),
            'destaque': fake_str(),
            'tp_Complemento': fake_int(),
            'fl_mesesCarencia': faker.boolean(),
            'Total_Dependentes': fake_int(),
            'dc_OperacaoCobranca': fake_str(),
            'dc_OperacaoEstorno': fake_str(),
            'dc_AjusteCobranca': fake_str(),
            'dc_AjusteEstorno': fake_str(),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['plano_seguro'].append(plano_seguro)

    for _ in range(num_records):
        adesao_seguro_item = {
            'id_AdesaoSeguroItem': fake_int(),
            'id_AdesaoSeguro': fake_int(),
            'id_Pessoa': fake_int(),
            'cd_Item': fake_int(),
            'dt_InicioVigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dt_TerminoVigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'fl_Titular': faker.boolean(),
            'tp_statusIntegracao': fake_int(),
            'dt_Exclusao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'dt_Adesao': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
            'id_IntegracaoParceiro': fake_str(),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['adesao_seguro_item'].append(adesao_seguro_item)

    for _ in range(num_records):
        seguradora = {
            'id_Seguradora': fake_int(),
            'nm_Seguradora': faker.company(),
            'id_Endereco': fake_int(),
            'fl_Ativo': faker.boolean(),
            'no_CNPJ': faker.bothify(text='##.###.###/####-##'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['seguradora'].append(seguradora)

    for _ in range(num_records):
        objeto_seguro = {
            'id_ObjetoSeguro': fake_int(),
            'id_PlanoSeguro': fake_int(),
            'tp_ObjetoSeguro': fake_int(),
            'id_CategoriaProduto': fake_int(),
            'dt_InicioVigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'dt_TerminoVigencia': faker.date_time().strftime(
                '%Y-%m-%d %H:%M:%S'
            ),
            'vl_FaixaPrecoInicial': fake_float(),
            'vl_FaixaPrecoFinal': fake_float(),
            'vl_PremioLiquido': fake_float(),
            'vl_IOF': fake_float(),
            'vl_PremioTotal': fake_float(),
            'pc_Franquia': fake_float(),
            'vl_ProLabore': fake_float(),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['objeto_seguro'].append(objeto_seguro)

    for _ in range(num_records):
        produto_venda = {
            'id_ProdutoVenda': fake_int(),
            'id_Emissor': fake_int(),
            'cd_ProdutoVenda': fake_str(),
            'nm_ProdutoVenda': fake_str(),
            'fl_Ativo': faker.boolean(),
            'no_MesesGarantiaFabricante': fake_int(),
            'id_NivelProduto': fake_int(),
            'nm_Marca': fake_str(),
            'nm_Modelo': fake_str(),
            'vl_PremioRisco': fake_float(),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['produto_venda'].append(produto_venda)

    for _ in range(num_records):
        canal_venda = {
            'id_CanalVenda': fake_int(),
            'cd_CanalVenda': fake_str(),
            'nm_CanalVenda': fake_str(),
            'fl_CanalPadrao': faker.boolean(),
            'id_Emissor': fake_int(),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['canal_venda'].append(canal_venda)

    for _ in range(num_records):
        produto_seguro = {
            'id_ProdutoSeguro': fake_int(),
            'id_Emissor': fake_int(),
            'cd_ProdutoSeguro': fake_str(),
            'nm_ProdutoSeguro': fake_str(),
            'dc_ProdutoSeguro': fake_str(),
            'id_Seguradora': fake_int(),
            'fl_SeguroMensal': faker.boolean(),
            'fl_PagamentoAntecipado': faker.boolean(),
            'qt_ParcelasBonificacao': fake_int(),
            'tp_BonificacaoMensal': fake_int(),
            'tp_DevolucaoCancelamento': fake_int(),
            'no_DiasDevolucaoCancelamento': fake_int(),
            'fl_ValidacaoAdesao': faker.boolean(),
            'fl_Excluido': faker.boolean(),
            'fl_PossuiItem': fake_int(),
            'no_Itens': fake_int(),
            'id_AgrupamentoProdutoSeguro': fake_int(),
            'fl_AceitaParcelamento': faker.boolean(),
            'no_MaximoParcelas': fake_int(),
            'no_NOP': fake_str(),
            'dc_TextoNotaFiscal': fake_str(),
            'cd_IntegracaoAP': fake_str(),
            'tp_IntegracaoAP': fake_str(),
            'cd_GrupoPagamento': fake_str(),
            'dc_GrupoPagamento': fake_str(),
            'cd_ContaContabil': fake_str(),
            'qt_ParcelasCancelamento': fake_int(),
            'fl_NaoEstornarParcelasNaoPagas': faker.boolean(),
            'fl_PostagemParcelaCorte': faker.boolean(),
            'fl_EnvioSeguradoraMensal': faker.boolean(),
            'dc_SMS': fake_str(),
            'fl_EnvioSMS': faker.boolean(),
            'fl_permitePrimeiraParcelaPaga': faker.boolean(),
            'fl_PermiteResponsavelFinanceiro': faker.boolean(),
            'fl_PermiteMultiplasAdesoes': faker.boolean(),
            'fl_ValidaProdutoVenda': faker.boolean(),
            'fl_ValidaNumeroSerieProdutoVenda': faker.boolean(),
            'fl_RestituicaoCancelamento': faker.boolean(),
            'fl_CalculaParcelaPorItem': faker.boolean(),
            'no_MinimoItens': fake_int(),
            'fl_IntegracaoServicoGS': faker.boolean(),
            'id_ProdutoAssociado': fake_int(),
            'fl_PermiteAssociacao': faker.boolean(),
            'fl_IntegracaoServicoGSRecorrencia': faker.boolean(),
            'fl_BonificacaoAntesDoCorte': faker.boolean(),
            'no_DiasBonificacao': fake_int(),
            'fl_PermiteEstCancSolicitacao': faker.boolean(),
            'id_Parceiro': fake_int(),
            'fl_ProdutoNovo': faker.boolean(),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['produto_seguro'].append(produto_seguro)

    for _ in range(num_records):
        adesao_participacao = {
            'id_AdesaoSeguro': fake_int(),
            'id_Participante': fake_int(),
            'tp_Operacao': fake_int(),
            'data_cdcBI': faker.date_time().strftime('%Y-%m-%d %H:%M:%S'),
             'production_date': faker.date_time().strftime('%Y-%m-%d'),
        }
        data['adesao_participacao'].append(adesao_participacao)

    jsonl_data(data=data)

    return data


num_records = input_num_linhas()
dados = pfs_seguros_ssa(num_records)


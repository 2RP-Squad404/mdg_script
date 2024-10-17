from google.cloud import bigquery

# Dataset: pfs_seguros_ssa, Table: adesao_seguro_item
adesao_seguro_item_schema = [
    bigquery.SchemaField('id_AdesaoSeguroItem', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_AdesaoSeguro', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_Pessoa', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cd_Item', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dt_InicioVigencia', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dt_TerminoVigencia', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('fl_Titular', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('tp_statusIntegracao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('dt_Exclusao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('dt_Adesao', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('id_IntegracaoParceiro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED'),
]


# Dataset: pfs_seguros_ssa, Table: endereco
endereco_schema = [
    bigquery.SchemaField('id_Endereco', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nm_Logradouro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('no_Logradouro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dc_Complemento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nm_Bairro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nm_Municipio', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cd_UF', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('no_CEP', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED'),
]


# Dataset: pfs_seguros_ssa, Table: pessoa
pessoa_schema = [
    bigquery.SchemaField('id_Pessoa', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nm_Pessoa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('no_CPF', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dt_Nascimento', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('tp_Sexo', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nm_Mae', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('no_RG', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dt_EmissaoRG', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('cd_UF_RG', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('no_PIS', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('no_CNS', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('no_DeclaracaoNascidoVivo', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tp_EstadoCivil', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tp_GrauParentesco', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_Endereco', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_Contato', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tp_Pessoa', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('fl_ApenasResponsavelFinanceiro', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('id_IntegracaoParceiro', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('data_cdcBI', 'TIMESTAMP', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED'),
]


# Dataset: pfs_seguros_ssa, Table: produto_seguro
produto_seguro_schema = [
    bigquery.SchemaField('id_ProdutoSeguro', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_Emissor', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('cd_ProdutoSeguro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('nm_ProdutoSeguro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dc_ProdutoSeguro', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_Seguradora', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_SeguroMensal', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_PagamentoAntecipado', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('qt_ParcelasBonificacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tp_BonificacaoMensal', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('tp_DevolucaoCancelamento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('no_DiasDevolucaoCancelamento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_ValidacaoAdesao', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_Excluido', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_PossuiItem', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('no_Itens', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('id_AgrupamentoProdutoSeguro', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_AceitaParcelamento', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('no_MaximoParcelas', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('no_NOP', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dc_TextoNotaFiscal', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cd_IntegracaoAP', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('tp_IntegracaoAP', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cd_GrupoPagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('dc_GrupoPagamento', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('cd_ContaContabil', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('qt_ParcelasCancelamento', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_NaoEstornarParcelasNaoPagas', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_PostagemParcelaCorte', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_EnvioSeguradoraMensal', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('dc_SMS', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('fl_EnvioSMS', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_permitePrimeiraParcelaPaga', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_PermiteResponsavelFinanceiro', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_PermiteMultiplasAdesoes', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_ValidaProdutoVenda', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_ValidaNumeroSerieProdutoVenda', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_RestituicaoCancelamento', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_CalculaParcelaPorItem', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('no_MinimoItens', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_IntegracaoServicoGS', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('id_ProdutoAssociado', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_PermiteAssociacao', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_IntegracaoServicoGSRecorrencia', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('fl_BonificacaoAntesDoCorte', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('no_DiasBonificacao', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_PermiteEstCancSolicitacao', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('id_Parceiro', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_ProdutoNovo', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED'),
]


# Dataset: pfs_seguros_ssa, Table: seguradora
seguradora_schema = [
    bigquery.SchemaField('id_Seguradora', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('nm_Seguradora', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('id_Endereco', 'INTEGER', 'NULLABLE'),
    bigquery.SchemaField('fl_Ativo', 'BOOLEAN', 'NULLABLE'),
    bigquery.SchemaField('no_CNPJ', 'STRING', 'NULLABLE'),
    bigquery.SchemaField('production_date', 'DATE', 'REQUIRED'),
]

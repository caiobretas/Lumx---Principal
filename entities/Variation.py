from datetime import datetime
class Variation:
    def __init__(self,
    idTransacao=None,
    idExterno=None,
    tipovariacao=None,
    tipo=None,
    realizado=None,
    datavencimentoantiga=None,
    datavencimento=None,
    datapagamentoantiga=None,
    datapagamento=None,
    valorprevistoantigo=None,
    valorrealizadoantigo=None,
    valorprevisto=None,
    valorrealizado=None,
    diferencaprojecao=None,
    idclassificacao=None,
    descricao=None,
    projeto=None,
    nomecentrocusto=None):
        
        self.idTransacao = idTransacao
        self.idExterno = idExterno
        self.tipovariacao = tipovariacao
        self.tipo = tipo
        self.realizado = realizado
        self.datavencimentoantiga = datavencimentoantiga
        self.datavencimento = datavencimento
        self.datapagamentoantiga = datapagamentoantiga
        self.datapagamento = datapagamento
        self.valorprevistoantigo = valorprevistoantigo
        self.valorrealizadoantigo = valorrealizadoantigo
        self.valorprevisto = valorprevisto
        self.valorrealizado = valorrealizado
        self.diferencaprojecao = diferencaprojecao
        self.idclassificacao = idclassificacao
        self.descricao = descricao
        self.projeto = projeto
        self.nomecentrocusto = nomecentrocusto

    def __repr__(self):
        return f"ID: {self.idTransacao} - tipovariacao: {self.tipovariacao}"

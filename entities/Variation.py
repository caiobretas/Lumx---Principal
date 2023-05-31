from datetime import datetime
class Variation:
    def __init__(self,
    id=None,
    tipo=None,
    tipovariacao=None,
    realizado=None,
    datavariacao=None,
    datavencimento=None,
    dataliquidacao=None,
    valorprevisto=None,
    valorantigo=None,
    valornovo=None,
    diferencaprojecao=None,
    idclassificacao=None,
    descricao=None,
    projeto=None,
    nomecentrocusto=None):
        
        self.id = id
        self.tipo = tipo
        self.tipovariacao = tipovariacao
        self.realizado = realizado
        if datavariacao: self.datavariacao = datetime.now()
        self.datavencimento = datavencimento
        self.dataliquidacao = dataliquidacao
        self.valorprevisto = valorprevisto
        self.valorantigo = valorantigo
        self.valornovo = valornovo
        self.diferencaprojecao = diferencaprojecao
        self.idclassificacao = idclassificacao
        self.descricao = descricao
        self.nomecentrocusto = nomecentrocusto

    def __repr__(self):
        return f"Tipo: {self.tipo} - Diferença: {self.diferencaprojecao}"

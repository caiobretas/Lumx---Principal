from uuid import UUID
from datetime import datetime
class Projection:
    def __init__(
        self,id: UUID = None,data_lançamento: datetime = None,data_liquidação: datetime = None,datavencimento: datetime = None,valorprevisto: float = None,valorrealizado: float = None,moeda: str = None,cotação: str = None, valorprevisto_BRL: float = None, valorrealizado_BRL: float = None,realizado: bool = None,recorrente: bool = None,de: str = None,para: str = None,percentualrateio: float = None,nomecentrocusto: str = None,nomepessoa: str = None,observacao: str = None,descricao: str = None,numeronotafiscal: int = None,nomeprojeto: str = None,contaativo: str = None,subcategoria4: str = None,subcategoria3: str = None,subcategoria2: str = None,subcategoria: str = None,categoria: str = None,categoriaprojecao: str = None,categoriacusto_receita: str = None,hash: str = None,check_conciliadoorigem: bool = None,check_conciliadodestino: bool = None):
        
        self.id = id
        self.data_lançamento = data_lançamento
        self.data_liquidação = data_liquidação
        self.datavencimento = datavencimento
        self.valorprevisto = valorprevisto
        self.valorrealizado = valorrealizado
        self.moeda = moeda
        self.cotação = cotação
        self.valorprevisto_BRL = valorprevisto_BRL
        self.valorrealizado_BRL = valorrealizado_BRL
        self.realizado = realizado
        self.recorrente = recorrente
        self.de = de
        self.para = para
        self.percentualrateio = percentualrateio
        self.nomecentrocusto = nomecentrocusto
        self.nomepessoa = nomepessoa
        self.observacao = observacao
        self.descricao = descricao
        self.numeronotafiscal = numeronotafiscal
        self.nomeprojeto = nomeprojeto
        self.contaativo = contaativo
        self.subcategoria4 = subcategoria4
        self.subcategoria3 = subcategoria3
        self.subcategoria2 = subcategoria2
        self.subcategoria = subcategoria
        self.categoria = categoria
        self.categoriaprojecao = categoriaprojecao
        self.categoriacusto_receita = categoriacusto_receita
        self.hash = hash
        self.check_conciliadoorigem = check_conciliadoorigem
        self.check_conciliadodestino = check_conciliadodestino
    
    def __repr__(self) -> str:
        return f'Data: {self.data_lançamento} - Categoria: {self.subcategoria4} - Valor: {self.valorprevisto} - Conta: {self.contaativo}\n'
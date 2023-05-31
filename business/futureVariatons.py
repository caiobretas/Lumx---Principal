"""
    Recebe lista de transações novas e lista de transações atuais

    Encontra as diferenças nas contas futuras vindas da Kamino e as que estão no banco*
    Instancia a entidade "Variation"
    
    * identifica se é alteração, entrada ou saída
    se for entrada verifica se é alteração. Se não, insere com o tipo 'Entrada'*2
    se for saída insere os valores com o tipo 'Saída'
    *2 = se for alteração, varifica as alterações, instancia as entidade final "Variation"
    
    A entidade final vai conter atributos necessários para a inserção na tabela de variações no banco
    
"""

o

from repositories.repositoryTransactions import RepositoryTransaction
from controllers.controllerHTTP.controllerKamino import ControllerKamino
from entities.Variation import Variation
from entities.entityCategory import Category
from entities.entityTransaction import Transaction

class TransactionsVariations:
    
    def __init__(self, newTransactions: list, oldTransactions) -> None:
        self.newTransactions: list = newTransactions
        
        self.oldTransactions: list[Transaction] = oldTransactions
        self.newTransactions: list[Transaction] = newTransactions
        
    def identifyType(self):
        
        self.inserts: list[Variation] = []
        self.deletes: list[Variation] = []
        self.changes: list[Variation] = []
        
        for obj in self.oldTransactions:
            
            transaction = Variation()
            
            
            # se o id da lista atual não estiver na lista de ids nova, foi deletada. Se estiver é atualização
            if obj.idKamino not in [transaction.idKamino for transaction in self.newTransactions]:   
                if obj.valorprevisto < 0: transaction.tipo = 'Pagamento'
                else: transaction.tipo = 'Recebimento'
                transaction.tipovariacao = 'Saída'
                self.deletes.append(obj)
                
            else: self.changes.append(obj)
        
        for obj in self.newTransactions:
            # se o id da lista nova não estiver na lista de ids atuais, 
            if obj.idKamino not in [transaction.idKamino for transaction in self.oldTransactions]: self.inserts.append(obj) 
    
    def insert
    
    def calculateVariation(self):
        self.identifyType(self)
        # itera sobre a lista de alterações para fazer as classificações
        for transaction in self.changes:
            transaction.

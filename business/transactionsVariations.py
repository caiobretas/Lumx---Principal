"""
    Recebe lista de transações novas e lista de transações atuais

    Encontra as diferenças nas contas futuras vindas da Kamino e as que estão no banco*
    Instancia a entidade "Variation"
    
    * identifica se é alteração, entrada ou saída
    se for entrada verifica se é alteração. Se não, insere com o tipo 'Entrada'*2
    se for saída insere os valores com o tipo 'Saída'
    *2 = se for alteração, verifica as alterações, instancia as entidade final "Variation"
    
    A entidade final vai conter atributos necessários para a inserção na tabela de variações no banco
    
"""


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
        
        self.inserts: list[Variation] = []
        self.deletes: list[Variation] = []
        self.changes: list[Variation] = []
        
        self.variations: list[Variation] = []
        
    def identifyType(self):
        if not self.oldTransactions or not self.newTransactions: return None
        
        oldIds = [oldTransaction.idKamino for oldTransaction in self.oldTransactions]
        newIds = [newTransaction.idKamino for newTransaction in self.newTransactions]
        
        for oldTransaction in self.oldTransactions:
            transaction = Variation(
                oldTransaction.id,
                oldTransaction.idKamino,
                datavencimentoantiga=oldTransaction.datavencimento,
                datapagamentoantiga=oldTransaction.datapagamento,
                valorprevistoantigo=oldTransaction.valorprevisto,
                valorrealizadoantigo=oldTransaction.valorrealizado,
                descricao=oldTransaction.descricao
            )
            
            if oldTransaction.valorprevisto < 0: transaction.tipo = 'Pagamento'
            else: transaction.tipo = 'Recebimento'
            
            # se o id atual não estiver na lista de ids nova, foi deletada. Se estiver é atualização
            if oldTransaction.idKamino not in newIds:
                transaction.tipovariacao = 'Saída'
                self.deletes.append(transaction)
                
            # se o id atual estiver na lista de ids nova, ele deve ir para a lista de alterações para as checagens
            else:
                # estação de checagem de alterações
                checks = []
                
                for newTransaction in self.newTransactions:
                
                    check1 = True
                    check2 = True
                    check3 = True
                    check4 = True
                    
                    if not oldTransaction.idKamino == newTransaction.idKamino: continue
                    
                    # checa se o idnovo está na lista de id (se não estiver, deve ser inserido. Não é alteração)
                    if newTransaction.idKamino not in oldIds:
                        transaction.tipovariacao = 'Entrada'
                    
                    # checa alteração de valor realizado
                    if newTransaction.valorrealizado: check1 = (False if newTransaction.valorrealizado == transaction.valorrealizadoantigo else True)
                    else: check1 = False
                    checks.append(check1)
                    
                    # checa alteração de valorprevisto
                    if newTransaction.valorprevisto == transaction.valorprevistoantigo: check2 = False
                    else: check2 =  True
                    checks.append(check2)
                    
                    # checa alteração de data de vencimento
                    if newTransaction.datavencimento == transaction.datavencimentoantiga.date(): check3 = False
                    else: check3 = True
                    checks.append(check3)
                    
                    # checa alteração de data de liquidação 
                    if newTransaction.datapagamento: check4: bool = (False if newTransaction.datapagamento != transaction.datapagamentoantiga else True)
                    else: check4 = False
                    checks.append(check4)
                    
                    if any(checks): 
                        check1: transaction.valorrealizado = newTransaction.valorrealizado
                        check2: transaction.valorprevisto = newTransaction.valorprevisto
                        check3: transaction.datavencimento = newTransaction.datavencimento
                        check4: transaction.datapagamento = newTransaction.datapagamento
                        
                        self.changes.append(transaction) 
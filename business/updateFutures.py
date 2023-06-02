import logging
from time import time
from datetime import datetime
from entities.entityTransaction import Transaction
from business.loadTransactions import LoadTransactions
from business.transactionsVariations import TransactionsVariations
from repositories.repositoryTransactions import RepositoryTransaction

from controllers.controllerHTTP.controllerKamino import ControllerKamino
from repositories.repositoryTransactions import RepositoryTransaction
                
class UpdateFutures:
    
    def __init__(self, connection, engine): 
        
        self.repositoryTransaction = RepositoryTransaction(connection, engine)
        self.controllerKamino = ControllerKamino()    

        self.param_periodoAte = datetime(year=2024, month=12, day=31).strftime('%m-%d-%Y') # determined max date that will be inserted
        
        print('\nUpdating futures...')
        
    def update(self):
        print('\nUpdating futures...')
        start_time = time()
        try:
            
            oldTransactions = self.repositoryTransaction.getTransactions(realizado=0) # get the futures in the repository
            newTransactions = [obj for obj in self.controllerKamino.getTransactions(periodoAte=self.param_periodoAte, apenasRealizados=False) if obj.realizado == 0 ] # get the futures in Kamino
            
            pixel = TransactionsVariations(newTransactions,oldTransactions)
            
            pixel.identifyType()
            pixel.inserts
            pixel.deletes
            pixel.changes
                        
            status = 'Complete'
            
        except Exception as err:
            status = 'Failed'
            logging.exception(err)
            
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
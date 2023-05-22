import logging
from time import time
from datetime import datetime
from entities.entityTransaction import Transaction
from business.loadTransactions import LoadTransactions
from repositories.repositoryTransactions import RepositoryTransaction

from controllers.controllerHTTP.controllerKamino import ControllerKamino
from repositories.repositoryTransactions import RepositoryTransaction
                
class UpdateFutures:
    
    def __init__(self, connection, engine):
        start_time = time()
        
        repositoryTransaction = RepositoryTransaction(connection, engine)
        controllerKamino = ControllerKamino()
        
        minFutureDateinRepo = repositoryTransaction.getDate(realizado=0)
        
        param_periodoDe = minFutureDateinRepo.strftime("%m-%d-%Y") if minFutureDateinRepo != None else None # the max date in the repository when realizado = 0
        param_periodoAte = datetime(year=2024, month=12, day=31).strftime('%m-%d-%Y') # determined max date that will be inserted
        
        print('\nUpdating futures...')
        try:
            
            list_transactionsRepository = repositoryTransaction.getTransactions(realizado=0) # get the futures in the repository
            list_transactionsKamino = [obj for obj in controllerKamino.getTransactions(param_periodoDe, param_periodoAte, apenasRealizados=False) if obj.realizado == 0 ] # get the futures in Kamino
            
            idKamino_list = [obj.idKamino for obj in list_transactionsKamino if obj.realizado == 0]
            idRepository_list = [obj.idKamino for obj in list_transactionsRepository  if obj.realizado == 0]
            
            delete_idList = []
            delete_list = []
            for transaction in list_transactionsRepository:
                if transaction.idKamino not in idKamino_list:
                    delete_list.append(transaction)
                    delete_idList.append(transaction.idKamino)
            
            update_list = []
            insert_list = []
            for transaction in list_transactionsKamino:
                if transaction.idKamino not in idRepository_list:
                    insert_list.append(transaction)        
                
                if transaction.idKamino in idRepository_list:
                    update_list.append(transaction)
                    
            repositoryTransaction.delete(delete_idList) if len(delete_idList) > 0 else None
            repositoryTransaction.upsert(update_list) if len(update_list) > 0 else None
            repositoryTransaction.upsert(insert_list) if len(insert_list) > 0 else None
            # repositoryTransaction.insert(insert_list, 'bulk') if len(insert_list) > 0 else None
            
            
            print(f'{len(update_list)} updates\n{len(insert_list)} inserts\n{len(delete_idList)} deletes\n')
            status = 'Complete'
            
        except Exception as err:
            status = 'Failed'
            logging.exception(err)
            
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
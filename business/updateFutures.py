from time import time
from datetime import datetime
from entities.entityTransaction import Transaction
from business.loadTransactions import LoadTransactions
from repositories.repositoryTransactions import RepositoryTransaction

class UpdateFutures:
    
    def __init__(self, connection, engine):
        start_time = time()
        self.repositoryTransaction = RepositoryTransaction(connection, engine)
        limitDate = datetime(year=2024, month=12, day=31).strftime('%m-%d-%Y')
        print('\nUpdating futures...')
        try:
            listTransactions: list[Transaction]=LoadTransactions(periodoDe=periodoDe,periodoAte=limitDate,apenasRealizados=False).loadTransactions()
            date = self.repositoryTransaction.getDate(realizado=0).strftime("%y-%m-%d")
            periodoDe = datetime.strftime(datetime.strptime(date, "%y-%m-%d"), "%m-%d-%y")
            self.repositoryTransaction.deleteFutures()
            self.repositoryTransaction.insert(lst=listTransactions)
            status = 'Complete'
       
        except:
            # put on limit dates
            now: datetime = datetime.now()
            periodoDe = now.strftime("%m-%d-%y")
            list_transactions = LoadTransactions(periodoDe=periodoDe, periodoAte=limitDate, apenasRealizados=False).loadTransactions()
            self.repositoryTransaction.insert(lst=list_transactions)
            status = 'Complete'
        
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
                
from time import time
from datetime import datetime, timedelta
from business.loadTransactions import LoadTransactions
from repositories.repositoryTransactions import RepositoryTransaction

class UpdateFutures:
    
    def __init__(self, connection, engine, schema, tableName):
        start_time = time()
        self.repositoryTransaction = RepositoryTransaction(connection, engine, schema, tableName)
        
        print('\nUpdating futures...')
        try:
            date = self.repositoryTransaction.getDate(realizado=0).strftime("%y-%m-%d")
            periodoDe = datetime.strftime(datetime.strptime(date, "%y-%m-%d"), "%m-%d-%y")
            periodoAte = datetime.strftime((datetime.strptime(date, "%y-%m-%d") + timedelta(days=365)), "%m-%d-%y")
            self.repositoryTransaction.deleteFutures()
            self.repositoryTransaction.insert(
                    lst=LoadTransactions(
                    periodoDe=periodoDe,
                    periodoAte=datetime.strptime(date, "%y-%m-%d") + timedelta(days=365),
                    apenasRealizados=False).loadTransactions()
                    )
            status = 'Complete'
       
        except:
            # put on limit dates
            now: datetime = datetime.now()
            periodoDe = now.strftime("%m-%d-%y")
            periodoAte = (now + timedelta(days=370)).strftime("%m-%d-%y")
            list_transactions = LoadTransactions(periodoDe=periodoDe, periodoAte=periodoAte, apenasRealizados=False).loadTransactions()
            self.repositoryTransaction.insert(lst=list_transactions)
            status = 'Complete'
        
        finally:
            try_time = time()
            print('Status: {} - Time: {:.2f}s'.format(status,' ' * 1, try_time - start_time))
                
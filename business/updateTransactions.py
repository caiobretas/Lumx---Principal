from time import time
from datetime import datetime
from business.loadTransactions import LoadTransactions
from repositories.repositoryTransactions import RepositoryTransaction

class UpdateTransactions:
    
    def __init__(self, connection, engine):
        start_time = time()
        self.repositoryTransaction = RepositoryTransaction(connection, engine)
        
        print('\nUpdating transactions...')

        try:
            date: str = self.repositoryTransaction.getDate(realizado=1)
            self.periodoDe = datetime.strftime(date, "%m-%d-%y")
            self.repositoryTransaction.deleteByDate(date=date)
                
        except:
            status = 'Reset'
            return None
    
        finally:
            try:
                lst = LoadTransactions(periodoDe=self.periodoDe,apenasRealizados=True).loadTransactions()
                self.repositoryTransaction.insert(lst=lst)
                status = 'Complete'
            except:
                # put on a limit date 
                self.periodoAte = datetime.now().strftime("%m-%d-%y")

                self.repositoryTransaction.insert(
                    lst=LoadTransactions(
                    periodoAte=self.periodoAte,
                    apenasRealizados=True).loadTransactions())
                
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
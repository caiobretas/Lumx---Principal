from time import time
from datetime import datetime
from business.loadTransactions import LoadTransactions
from repositories.repositoryTransactionsKamino import RepositoryKamino
from repositories.repositoryTransactions import RepositoryTransactions

class UpdateKaminoTransactions:
    
    def __init__(self, connection, engine):
        
        self.connection = connection
        self.engine = engine
        self.repositoryKamino = RepositoryKamino(connection, engine)
        self.repositoryTransaction = RepositoryTransactions(connection, engine)
        
        print('\nUpdating Kamino transactions...')
        
    def update(self):
        try:
            date: str = self.repositoryKamino.getDate(realizado=1)
            self.periodoDe = datetime.strftime(date, "%m-%d-%y")
            self.repositoryKamino.deleteByDate(date)
                
        except:
            status = 'Reset'
            return None
    
        finally:
            start_time = time()
            try:
                self.repositoryKamino.insert(LoadTransactions(self.periodoDe,apenasRealizados=True).loadKaminoTransactions())
                
                status = 'Complete'
            except:
                # put on a limit date 
                self.periodoAte = datetime.now().strftime("%m-%d-%y")

                self.repositoryKamino.insert(
                    lst=LoadTransactions(
                    periodoAte=self.periodoAte,
                    apenasRealizados=True).loadKaminoTransactions())
                
                
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
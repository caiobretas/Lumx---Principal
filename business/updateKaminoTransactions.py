import logging
from time import time
from datetime import datetime, timedelta
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
            periodoDe = datetime.strftime(date - timedelta(days=10), "%m-%d-%y")
                
        except Exception as e:
            logging.error(e)
            status = 'Reset'
            return None
    
        finally:
            start_time = time()
            try:
                self.repositoryKamino.insert(LoadTransactions(periodoDe=periodoDe,apenasRealizados=True).loadKaminoTransactions())
                status = 'Complete'
                
            except Exception as e:
                logging.error(e)
                # put on a limit date 
                self.periodoAte = datetime.now().strftime("%m-%d-%y")

                self.repositoryKamino.insert(
                    lst=LoadTransactions(
                    periodoAte=self.periodoAte,
                    apenasRealizados=True).loadKaminoTransactions())
                
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
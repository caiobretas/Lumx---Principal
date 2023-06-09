import logging
from time import time
from repositories.repositoryTransactionsKamino import RepositoryKamino
from repositories.repositoryTransactions import RepositoryTransactions
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction

class UpdateTransactions:
    
    def __init__(self, connection, engine):
        
        self.repositoryKamino = RepositoryKamino(connection, engine)
        self.repositoryCrypto = RepositoryCryptoTransaction(connection, engine)
        self.repositoryTransaction = RepositoryTransactions(connection, engine)
        
        self.connection = connection
        self.engine = engine
        
        print('\nUpdating transactions...')
        
    def update(self):
        start_time = time()
        try:
            self.repositoryKamino.getTransactions(realizado=1)
            self.repositoryCrypto.getCryptoTransactions()
            
            transactionsCrypto = self.repositoryCrypto.transactions
            transactionsKamino = self.repositoryKamino.transactions
            
            
            self.repositoryTransaction.insert(transactionsKamino, 'bulk')
            self.repositoryTransaction.insert(transactionsCrypto, 'bulk')
            
            status = 'Complete'
        
        except Exception as e:
            status = 'Failed'
            logging.error(e)

        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
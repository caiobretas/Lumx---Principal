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
            self.repositoryKamino.getTransactions()
            self.repositoryCrypto.getCryptoTransactions()
            
            transactionsKamino = self.repositoryKamino.transactions
            transactionsCrypto = self.repositoryCrypto.transactions
            
            self.repositoryTransaction.insert(transactionsCrypto, 'bulk')
            self.repositoryTransaction.insert(transactionsKamino, 'bulk')
            status = 'Complete'
        
        except Exception as e:
            status = 'Failed'
            logging.error(e)
            return None

        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
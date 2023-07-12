from time import time
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateCategories import UpdateCategories
from business.updateKaminoTransactions import UpdateKaminoTransactions
from business.updateCryptoTransactions import UpdateCryptoTransactions
from business.updateTransactionsRepository import UpdateTransactions
from business.finance.updateProjects import UpdateProjects
from business.updateFutures import UpdateFutures
from business.updateBook import UpdateBook

class FinanceRepository:
    def __init__(self,connection,engine) -> None:
        self.connection = connection
        self.engine = engine
        
    def update(self): 
        timer = time()
        
        UpdateBook(self.connection,self.engine).update()
        UpdateCategories(self.connection, self.engine).update()
        UpdateProjects(self.connection, self.engine).update()
        UpdateCryptoPrices(self.connection,self.engine).update()
        UpdateCryptoTransactions(self.connection, self.engine).update()
        UpdateKaminoTransactions(self.connection,self.engine).update()
        UpdateFutures(self.connection,self.engine).update()
        # UpdateTransactions(self.connection, self.engine).update()
        print('\nRepositories updated in {:.2f} seconds\n'.format(time() - timer))

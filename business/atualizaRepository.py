from time import time
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateCategories import UpdateCategories
from business.updateTransactions import UpdateTransactions
from business.updateCryptoTransactions import UpdateCryptoTransactions
from business.updateFutures import UpdateFutures
from business.updateBook import UpdateBook

class UpdateFinanceRepository:
    def __init__(self,connection,engine) -> None:
        
        self.connection = connection
        self.engine = engine
        
    def update(self):
        timer = time()
        UpdateBook(self.connection,self.engine) # update book repository from 'interface.xlsx'
        UpdateCategories(self.connection, self.engine)
        UpdateCryptoTransactions(self.connection, self.engine)
        UpdateCryptoPrices(self.connection,self.engine)
        UpdateTransactions(self.connection,self.engine)
        UpdateFutures(self.connection,self.engine)

        print('\nDatabase updated in {:.2f} seconds\n'.format(time() - timer))

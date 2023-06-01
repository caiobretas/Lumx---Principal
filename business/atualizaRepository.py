from time import time
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateCategories import UpdateCategories
from business.updateTransactions import UpdateTransactions
from business.updateCryptoTransactions import UpdateCryptoTransactions
from business.updateFutures import UpdateFutures
from business.updateBook import UpdateBook

class UpdateFinanceRepository:
    def __init__(self,connection,engine) -> None:
        timer = time()
        
        UpdateBook(connection,engine).update() # update book repository from 'interface.xlsx'
        UpdateCategories(connection, engine).update()
        UpdateCryptoTransactions(connection, engine).update()
        UpdateCryptoPrices(connection,engine).update()
        UpdateTransactions(connection,engine)
        UpdateFutures(connection,engine).update()

        print('\nDatabase updated in {:.2f} seconds\n'.format(time() - timer))

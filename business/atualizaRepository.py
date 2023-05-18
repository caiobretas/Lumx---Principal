from time import time
from business.updateCryptoPrices import UpdateCryptoPrices
from business.updateCategories import UpdateCategories
from business.updateTransactions import UpdateTransactions
from business.updateCryptoTransactions import UpdateCryptoTransactions
from business.updateFutures import UpdateFutures
from business.updateBook import UpdateBook

class AtualizaFinanceRepository:
    def __init__(self, connFinance, engine, schema, pathIF, connProtocol) -> None:
        timer = time()
        
        UpdateBook(connection=connFinance, engine=engine, schema=schema, tableName='book', path_interface=pathIF,sheetName_interface='book')
        UpdateCategories(connection=connFinance, engine=engine,pathIF=pathIF,schema='finance', sheetName='categories', tableName='categories')
        UpdateCryptoTransactions(path_interface=pathIF, connection=connFinance, engine=engine, schema='finance', tableName='movements_crypto')
        UpdateCryptoPrices(connectionFinance=connFinance, engineAdmin=engine, schema=schema, tableName='prices_crypto')
        UpdateTransactions(connection=connFinance,engine=engine,schema='finance',tableName='movements')
        UpdateFutures(connection=connFinance,engine=engine,schema='finance',tableName='movements')

        print('\nDatabase updated in {:.2f} seconds\n'.format(time() - timer))

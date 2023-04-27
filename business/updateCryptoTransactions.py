from datetime import datetime
from time import time
from entities.entityCoin import Coin
from entities.entityBook import Book
from entities.entityTransaction import TransactionCrypto
from business.loadTransactions import LoadTransactions
from business.treatCryptoTransactions import TreatCryptoTransactions
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from repositories.repositoryBook import RepositoryBook
from repositories.repositoryPrices import RepositoryPrices

class UpdateCryptoTransactions:
    
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
            
            start_time = time()
            list_coins: list[Coin] = RepositoryPrices(connection=connection, engine=engine, schema=schema, tableName='prices_crypto').getTokens()
            list_wallets: list[Book] = RepositoryBook(connection=connection, engine=engine, schema=schema, tableName='book').getBook()
            
            print('\nUpdating Crypto Transactions...')
            try:
                self.repositoryCryptoTransactions = RepositoryCryptoTransaction(connection=connection, engine=engine, schema=schema, tableName=tableName)
                apiKey = 'DUUV82YWBS4YIWEURM8V7N5AXWB5ZMJH3A'

                list_transactions: list[TransactionCrypto] = []
                for wallet in list_wallets:
                    if wallet.is_lumx:
                        obj = LoadTransactions().loadCryptoTransactions(is_safe=wallet.is_safe,address=wallet.address, apiKey=apiKey, chain=wallet.blockchain, name=wallet.name)
                        list_transactions.extend(obj)
                
                if self.repositoryCryptoTransactions.getDate() != None:
                    # get the higher date registered
                    date = self.repositoryCryptoTransactions.getDate()
                    # delete the registers on that date to avoid duplicates
                    self.repositoryCryptoTransactions.deleteByDate(date=date)

                    list_new_transactions: list[TransactionCrypto] = []
                    for transaction in list_transactions:
                        if transaction.datetime.date() >= date:
                                list_new_transactions.append(transaction)
                                TreatCryptoTransactions(transaction)
                    self.repositoryCryptoTransactions.insert(lst=list_new_transactions)
                    status = 'Complete'
                else:
                    for transaction in list_transactions:
                        TreatCryptoTransactions(transaction)
                    self.repositoryCryptoTransactions.insert(lst=list_transactions)
                    status = 'Reset'
            
            except:
                status = 'Failed'
                raise Exception
            
            finally:
                try_time = time()
                print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
                self.repositoryCryptoTransactions.delete_unknown_tokens(list_known_tokens=list_coins)
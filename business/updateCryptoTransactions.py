import logging
from time import time
from entities.entityCoin import Coin
from entities.entityBook import Book
from entities.entityTransaction import TransactionCrypto
from business.loadTransactions import LoadTransactions
from business.conciliateCryptoTransactions import ConciliateCryptoTransactions
from business.treatCryptoTransactions import TreatCryptoTransactions
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from repositories.repositoryBook import RepositoryBook
from repositories.repositoryPrices import RepositoryPrices

class UpdateCryptoTransactions:
    
    def __init__(self, path_interface, connection: str, engine: str, schema: str, tableName: str):
            start_time = time()
            
            self.repositoryBook = RepositoryBook(connection=connection, engine=engine, schema=schema, tableName='book')
            list_coins: list[Coin] = RepositoryPrices(connection=connection, engine=engine, schema=schema, tableName='prices_crypto').getTokens()
            self.list_addresses: list[Book] = self.repositoryBook.getBook()
            self.list_wallets: list = self.repositoryBook.list_wallets
            self.list_conversion: list = self.repositoryBook.list_conversion
            self.list_primarysale: list = self.repositoryBook.list_primarysale
            self.list_secondarysale: list = self.repositoryBook.list_secondarysale
            
            print('\nUpdating Crypto Transactions...')
            try:
                self.repositoryCryptoTransactions = RepositoryCryptoTransaction(connection=connection, engine=engine, schema=schema, tableName=tableName)
                apiKey = 'DUUV82YWBS4YIWEURM8V7N5AXWB5ZMJH3A'
                
                list_transactions: list[TransactionCrypto] = []
                for wallet in self.list_addresses:
                    if wallet.is_lumx:
                        transaction_crypto = LoadTransactions().loadCryptoTransactions(is_safe=wallet.is_safe,address=wallet.address, chain=wallet.blockchain, name=wallet.name)
                        list_transactions.extend(transaction_crypto)
                
                if self.repositoryCryptoTransactions.getDate() != None:
                    # get the higher date registered
                    date = self.repositoryCryptoTransactions.getDate()
                    # delete the registers on that date to avoid duplicates
                    self.repositoryCryptoTransactions.deleteByDate(date=date)

                    list_new_transactions: list[TransactionCrypto] = []
                    for transaction_crypto in list_transactions:
                        if transaction_crypto.datetime.date() >= date:
                            TreatCryptoTransactions(obj=transaction_crypto,list_wallets=self.list_wallets, list_conversion=self.list_conversion,list_primarysale=self.list_primarysale,list_secondarysale=self.list_secondarysale)
                            list_new_transactions.append(transaction_crypto)
                        
                    self.repositoryCryptoTransactions.insert(lst=list_new_transactions)
                    status = 'Complete'
                else:
                    status = 'Reset'
                    for obj in list_transactions:
                        TreatCryptoTransactions(obj=obj,list_wallets=self.list_wallets, list_conversion=self.list_conversion,list_primarysale=self.list_primarysale,list_secondarysale=self.list_secondarysale)
                    self.repositoryCryptoTransactions.insert(lst=list_transactions)
            
            except Exception as e:
                logging.error(f"An error occurred while getting the book: {e}")
                status = 'Failed'
                raise e
            
            finally:
                try_time = time()
                print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
                self.repositoryCryptoTransactions.delete_unknown_tokens(list_known_tokens=list_coins)
                ConciliateCryptoTransactions(path_interface, connection, engine, schema, tableName)
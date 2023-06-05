import logging
from time import time, sleep
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
    
    def __init__(self, connection: str, engine: str):
            
            self.connection = connection
            self.engine = engine
            self.repositoryBook = RepositoryBook(connection,engine)
            self.list_coins: list[Coin] = RepositoryPrices(connection,engine).getTokens()
            self.list_addresses: list[Book] = self.repositoryBook.getBook()
            self.list_wallets: list = self.repositoryBook.list_wallets
            self.list_conversion: list = self.repositoryBook.list_conversion
            self.list_primarysale: list = self.repositoryBook.list_primarysale
            self.list_secondarysale: list = self.repositoryBook.list_secondarysale
    
    def update(self):      
            print('\nUpdating Crypto Transactions...')
            start_time = time()
            try:
                self.repositoryCryptoTransactions = RepositoryCryptoTransaction(self.connection,self.engine)
                list_transactions: list[TransactionCrypto] = []
                for wallet in self.list_addresses:
                    if wallet.is_lumx:
                        transaction_crypto = LoadTransactions().loadCryptoTransactions(wallet.is_safe,wallet.address, wallet.name, wallet.blockchain)
                        list_transactions.extend(transaction_crypto)
                        print(f'{" "*5}{wallet.name} transactions imported.')
                    else:
                        None
                        
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
                logging.error(e)
                status = 'Failed'
                raise e
            
            finally:
                try_time = time()
                print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
                self.repositoryCryptoTransactions.delete_unknown_tokens(list_known_tokens=self.list_coins)
                ConciliateCryptoTransactions(self.connection, self.engine)
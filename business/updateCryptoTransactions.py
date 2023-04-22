from datetime import datetime
from time import time
from entities.entityCoin import Coin
from entities.entityTransaction import Transaction, TransactionCrypto
from business.loadTransactions import LoadTransactions
from repositories.repositoryCryptoTransactions import RepositoryCryptoTransaction
from repositories.repositoryPrices import RepositoryPrices

class UpdateCryptoTransactions:
    
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
            
            start_time = time()
            list_coins: list[Coin] = RepositoryPrices(connection=connection, engine=engine, schema=schema, tableName='prices_crypto').getTokens()
            dict_wallets: dict = {
            'Bank': ['Gnosis',
                     'Gnosis',
                     'Ledger',
                     'Helper',
                     '55Unity',
                     'Seamore',
                     'Mercado Bitcoin',
                     'Caio Bretas',
                     'Michel Goldberg',
                     ],
                     
            'Address': ['0x4e3c4cb1c2ecc0005c5980a5c09ac5146529ccb2',
                        '0xABDce09D5989D7E2e9Fc53132718A7F5129f2625',
                        '0x26ac68037C202B8AC2D1CFcc487651daD41B68E0',
                        '0xA65aae78EdEF916d4102BA7b5672068C0D35fbff',
                        '0x29D212888BB715322a6f7c80A78Cb75E31B2d9Aa',
                        '0xE32BB205766A79ADd2f92153E36613EF62f656Ae',
                        '0x128Dbbc9A8E0F1c9c5b28FacA391891Fcdc707F7',
                        '0x83Cc4e2C40164D6A56fe5bA7396706bE523AdEF6',
                        '0x531686eD12bA65f94BcaF4ed1A2478Ffac1A78E7'
                        ],

            'Blockchain': ['ETH',
                           'MATIC',
                           'ETH',
                           'ETH',
                           'ETH',
                           'ETH',
                           'ETH',
                           'ETH',
                           'ETH'
                           ],
            'Metamask': [0,0,1,1,1,1,0,1,1]
            }
            
            print('\nUpdating Crypto Transactions...')
            try:
                self.repositoryCryptoTransactions = RepositoryCryptoTransaction(connection=connection, engine=engine, schema=schema, tableName=tableName)
                apiKey = 'DUUV82YWBS4YIWEURM8V7N5AXWB5ZMJH3A'

                list_transactions: list[TransactionCrypto] = []
                for value in dict_wallets['Address']:
                    value_index: int = dict_wallets['Address'].index(value)
                    name: str = dict_wallets['Bank'][value_index]
                    chain: str = dict_wallets['Blockchain'][value_index]
                    metamask: bool = bool(dict_wallets['Metamask'][value_index])
                    obj = LoadTransactions().loadCryptoTransactions(metamask=metamask,address=value, apiKey=apiKey, chain=chain, name=name)
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
                    self.repositoryCryptoTransactions.insert(lst=list_new_transactions)
                    status = 'Complete'
                else:
                    self.repositoryCryptoTransactions.insert(lst=list_transactions)
                    status = 'Reset'
            
            except:
                status = 'Failed'
                raise Exception
            
            finally:
                try_time = time()
                print('{} Status: {} - Time: {}'.format(status,' ' * 1,round(try_time - start_time, 3)))
                self.repositoryCryptoTransactions.delete_unknown_tokens(list_known_tokens=list_coins)
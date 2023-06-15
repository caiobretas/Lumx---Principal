import logging
from time import time
from datetime import datetime
from entities.entityCoin import Coin
from repositories.repositoryPrices import RepositoryPrices
from business.loadPrices import LoadPrices

class UpdateCryptoPrices:
    def __init__(self, connection, engine):
        self.repositoryPrices = RepositoryPrices(connection, engine)
       
    def update(self):
        print('\nUpdating Crypto Prices...')
        start_time = time()
        try:
            self.repositoryPrices.getDate()
            date = self.repositoryPrices.maxDate
            
            if date == None:
                status = 'Empty'
                raise ValueError('Empty database')
            
            status = 'Updating'
            
        except ValueError as ve:
            print(f'{"" * 3}Warning: {ve}')
            status = 'Empty'
            date = datetime(year=2021, month=12, day=31).date()

        finally:
            self.repositoryPrices.deleteByDate(date=date)
            try:
                prices = LoadPrices(apiKey_CryptoCompare='23e942445972f1802686f5a61a92555d1d2c5f0f3c10976d04b2b783a8453e5d').loadPrices()
                newPrices_list: list[Coin] = []
                for price in prices:
                    if price.date >= date or status == 'Empty' and price.date >= date:
                        newPrices_list.append(price)
                status = 'Updating'
                self.repositoryPrices.insertPrice(list_coin=newPrices_list)
                status = 'Complete'
                
            except Exception:
                status = 'Failed'
                raise Exception
                # raise KeyError('Erro')
                
            finally:
                try_time = time()
                print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))                
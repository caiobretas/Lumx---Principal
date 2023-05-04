from time import time
from entities.entityCoin import Coin
from repositories.repositoryPrices import RepositoryPrices
from viewers.viewerPrices import ViewerPrices

class WritePrices:
    def __init__(self, path, sheetName, connection, engine, schema, tableName):
        self.schema = schema
        self.tableName = tableName
        self.sheetName = sheetName
        self.path = path
        self.connection = connection
        self.engine = engine
        self.tableName = tableName
        
    def writePrices(self):
        repositoryPrices = RepositoryPrices(self.connection, self.engine, self.schema, self.tableName)
        start_time = time()
        print('\nWriting prices...')
        
        try:
            list_coins: list[Coin] = repositoryPrices.getPrices()
            ViewerPrices(path=self.path, sheetName=self.sheetName).insertPrices(list_coins)
            status = 'Complete'
        except:
            status = 'Failed'
            raise Exception
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))


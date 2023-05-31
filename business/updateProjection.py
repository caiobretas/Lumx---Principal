from time import time
from viewers.viewerPrices import ViewerPrices
from business.writePrices import WritePrices
from business.writeProjection import WriteProjection

class UpdateProjection(object):
    def __init__(self, connFinance, engineAdmin) -> None:
        self.connection = connFinance
        self.engine = engineAdmin
        
    def update(self):
        timer = time()
        self.projection = WriteProjection(worksheetId='1jbUYWqBW1aFmqJNAISv7xw7Bwe6p1e_uLleOAUGYRfs', connection=self.connection, engine=self.engine)
        self.projection.writeTransactions()
        self.projection.writePrices()
        print('Projection updated in {:.2f} seconds\n'.format(time() - timer))
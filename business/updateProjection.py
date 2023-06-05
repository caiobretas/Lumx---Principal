from time import time
from business.writeProjection import WriteProjection

class UpdateProjection(object):
    def __init__(self, connection, engine) -> None:
        self.connection = connection
        self.engine = engine
    
    def update(self):
        timer = time()
        self.projection = WriteProjection('1jbUYWqBW1aFmqJNAISv7xw7Bwe6p1e_uLleOAUGYRfs', self.connection, self.engine)
        self.projection.writeTransactions()
        self.projection.writePrices()
        print('Projection updated in {:.2f} seconds\n'.format(time() - timer))
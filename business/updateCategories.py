import logging
from time import time
from repositories.repositoryCategories import RepositoryCategories

class UpdateCategories:
    def __init__(self, connection, engine):
        
        self.connection = connection
        self.engine = engine
        
        print('\nUpdating Categories...')
    def update(self):
        start_time = time()
        try:
            repositoryCategories = RepositoryCategories(self.connection, self.engine)
            repositoryCategories.insertCategories(repositoryCategories.getCategories_fromExcel())
            status = 'Complete'
            
        except Exception as e:
            status = 'Failed'
            logging.error(e)
            return None
        
        finally:
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
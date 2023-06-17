import logging
from time import time
from repositories.repositoryBook import RepositoryBook

class UpdateBook:

    def __init__(self,connection,engine):
        self.connection = connection
        self.engine = engine
        
    def update(self):
        print('\nUpdating Book...')
        start_time = time()
        try:
            self.list_books = RepositoryBook(self.connection,self.engine).getBook_fromSheets()
            # insert the list in database
            RepositoryBook(self.connection,self.engine).insert(lst=self.list_books)
            try_time = time()
            status = 'Complete'
            
        except Exception as e:
            status = 'Failed'
            try_time = time()
            logging.error(e)
        print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
import logging
from time import time
from repositories.repositoryBook import RepositoryBook

class UpdateBook:
    def __init__(self,connection,engine):
        start_time = time()
        print('\nUpdating Book...')
        try:
            self.list_books = RepositoryBook(connection,engine).getBook_fromExcel()
            # insert the list in database
            RepositoryBook(connection,engine).insert(lst=self.list_books)
            try_time = time()
            status = 'Complete'
            
        except Exception as e:
            status = 'Failed'
            logging.error(e)
        print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
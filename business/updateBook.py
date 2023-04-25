from time import time
from interfaces.interfaceBook import InterfaceBook
from repositories.repositoryBook import RepositoryBook

class UpdateBook:
    def __init__(self, connection, engine, schema, tableName, path_interface, sheetName_interface):
        start_time = time()
        try:
            self.list_books = InterfaceBook(path_interface=path_interface, sheetName_interface=sheetName_interface).getBook()
            # insert the list in database
            RepositoryBook(connection=connection, engine=engine, schema=schema, tableName=tableName).insert(lst=self.list_books)
            try_time = time()
            status = 'Complete'
        except:
            status = 'Failed'
        print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
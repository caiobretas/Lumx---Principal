from interfaces.interfaceBook import InterfaceBook
from repositories.repositoryBook import RepositoryBook

class UpdateBook:
    def __init__(self, connection, engine, schema, tableName, path_interface, sheetName_interface):
        self.list_books = InterfaceBook(path_interface=path_interface, sheetName_interface=sheetName_interface).getBook()
        # insert the list in database
        RepositoryBook(connection=connection, engine=engine, schema=schema, tableName=tableName).insert(lst=self.list_books)
        
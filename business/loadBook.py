from interfaces.interfaceBook import InterfaceBook

class LoadBook:
    def __init__(self, path, sheetName):
        try:
            self.list_books = InterfaceBook(path=path, sheetName=sheetName).getBook()
            print(self.list_books)

        except Exception as e:
            raise e
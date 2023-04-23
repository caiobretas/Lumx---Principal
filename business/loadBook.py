from interfaces.interfaceBook import InterfaceBook

class LoadBook:
    def __init__(self, path, sheetName):
        try:
            self.list_books = InterfaceBook(path=path, sheetName=sheetName).getBook()

        except:
            raise Exception
import pandas as pd
from entities.entityBook import Book
from interfaces.interfaceBase import InterfaceBase

class InterfaceBook(InterfaceBase):
    def __init__(self,path, sheetName):
        self.path = path
        super().__init__(path, sheetName)
        self.dataframe = super().abreDataFrame()
    
    def getSheets(self):
        try:
            xlsx = pd.ExcelFile(self.path)
            sheet_names = xlsx.sheet_names
            return sheet_names
        except Exception as e:
            print("Erro ao obter nomes das sheets:", e)
            return None
   
    def getBook(self) -> list[Book]:
        self.getSheets()


        list_books: list[Book] = []
        for index, row in self.dataframe.iterrows():
            book = Book(
                address = row['address'],
                name = row['name'],
                is_lumx = row['is_lumx'],
                is_conversion = row['is_conversion'],
                is_primarysale = row['is_primarysale'],
                is_secondarysale = row['is_secondarysale'])
            list_books.append(book)
        return list_books
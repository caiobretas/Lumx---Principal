import pandas as pd
from entities.entityBook import Book
from interfaces.interfaceBase import InterfaceBase

class InterfaceBook(InterfaceBase):
    def __init__(self,path_interface, sheetName_interface):
        self.path = path_interface
        super().__init__(path_interface, sheetName_interface)
        
    
    def getSheets(self):
        try:
            xlsx = pd.ExcelFile(self.path)
            sheet_names = xlsx.sheet_names
            return sheet_names
        except Exception as e:
            print("Erro ao obter nomes das sheets:", e)
            return None
   
    def getBook(self) -> list[Book]:
        self.dataframe = super().abreDataFrame()
        self.getSheets()

        list_books: list[Book] = []
        for index, row in self.dataframe.iterrows():
            book = Book(
                address = row['address'] if row['address'] != 'nan' else None,
                name = row['name'] if row['name'] != 'nan' else None,
                is_lumx = bool(row[2]) if str(row[2]) != 'nan' else None,
                is_safe = bool(row[3]) if str(row[3]) != 'nan' else None,
                blockchain = str(row[4]) if str(row[4]) != 'nan' else None,
                is_conversion = bool(row[5]) if str(row[5]) != 'nan' else None,
                is_primarysale = bool(row[6]) if str(row[6]) != 'nan' else None,
                is_secondarysale = bool(row[7]) if str(row[7]) != 'nan' else None)
            list_books.append(book)
        return list_books
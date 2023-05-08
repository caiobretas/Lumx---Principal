import logging
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
        except:
            raise Exception
   
    def getBook(self) -> list[Book]:
        try:
            self.dataframe = super().abreDataFrame()
            sheets = self.getSheets()

            list_books: list[Book] = []
            self.dataframe.fillna(value=bool(), inplace=True)
            for index, row in self.dataframe.iterrows():
                book = Book(
                    address = row[0],
                    name = row[1],
                    is_lumx = bool(row[2]),
                    is_safe = bool(row[3]),
                    blockchain = str(row[4]),
                    is_conversion = bool(row[5]),
                    is_primarysale = bool(row[6]),
                    is_secondarysale = bool(row[7]),
                    project = str(row[8]))
                
                list_books.append(book)
            return list_books
        
        except Exception as e:
            logging.error(f"An error occurred while getting the book: {e}")
            raise e
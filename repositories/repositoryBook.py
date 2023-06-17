import string
import psycopg2
import logging
from pandas import DataFrame
from controllers.controllerGoogle.controllerGoogleSheets import GoogleSheets
from entities.entityBook import Book
from repositories.repositoryBase import RepositoryBase
from gspread import Worksheet
class RepositoryBook ( RepositoryBase ):
    def __init__(self, connection: str, engine: str):
        self.tableName = 'book' # postgresql
        self.schema = 'finance' # postgresql
        self.worksheetName = 'book' # excel
        self.connection: psycopg2.connection = connection
        
        super().__init__(connection, engine, self.schema, self.tableName)

        self.controllerGoogleSheets = GoogleSheets()
        self.workSheetId = '1PbXHn_U8fcI4yknowFlYAQ7ISc_t6ZVG1uhuhxfcaXM'
        self.workSheetHeaders = [
        'address',
        'name',
        'is_lumx',
        'is_safe',
        'blockchain',
        'is_conversion',
        'is_primarysale',
        'is_secondarysale',
        'project'
        ]
        self.bookSheetId = 1088169641
        self.lastUpdateSheetId = 1239069114


    def insert(self, lst: list[Book]) -> None: # postgresql
        if not lst: return
        with self.connection.cursor() as cur:
            values = [t.to_tuple() for t in lst]
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
            
                query = f"""
INSERT INTO {self.schema}.{self.tableName}
(address, name, is_lumx, is_safe, blockchain, is_conversion, is_primarysale, is_secondarysale, project)
VALUES ({placeholders})
ON CONFLICT (address) DO UPDATE SET 
name = EXCLUDED.name, 
is_lumx = EXCLUDED.is_lumx, 
is_safe = EXCLUDED.is_safe,
blockchain = EXCLUDED.blockchain, 
is_conversion = EXCLUDED.is_conversion,
is_primarysale = EXCLUDED.is_primarysale, 
is_secondarysale = EXCLUDED.is_secondarysale,
project = EXCLUDED.project
"""     
                cur.executemany(query, values)
                self.connection.commit()
            
            except Exception as e:
                logging.error(e)
                return None
                
            
    def getBook(self) -> list[Book]: # postgresql
        with self.connection.cursor() as cur:
            query = f"SELECT DISTINCT * FROM {self.schema}.{self.tableName} order by is_lumx desc"
            try:
                cur.execute(query)
                
                self.list_wallets: list = []
                self.list_conversion: list = []
                self.list_primarysale: list = []
                self.list_secondarysale: list = []
                list_book: list[Book] = []
                for row in cur.fetchall():
                    book = Book(
                    address = row[0],
                    name = row[1],
                    is_lumx = row[2],
                    is_safe = row[3],
                    blockchain = row[4],
                    is_conversion = row[5],
                    is_primarysale = row[6],
                    is_secondarysale = row[7]
                    )
                    list_book.append(book)
                    self.list_wallets.append(str(book.address).strip().lower()) if book.is_lumx else None
                    self.list_conversion.append(str(book.address).strip().lower()) if book.is_conversion else None
                    self.list_primarysale.append(str(book.address).strip().lower()) if book.is_primarysale else None
                    self.list_secondarysale.append(str(book.address).strip().lower()) if book.is_secondarysale else None
                    
                return list_book
            
            except:
                raise Exception
    
    def getBook_fromExcel(self) -> list[Book]: # excel
        try:
            dataframe: DataFrame = super().openDataFrame()
            list_books: list[Book] = []
            dataframe.fillna(value=bool(), inplace=True)
            for index, row in dataframe.iterrows():
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

    def getBook_fromSheets(self):
        sheet: Worksheet = self.controllerGoogleSheets.openSheet(self.workSheetId, self.bookSheetId)
        
        maxColumn = len(self.workSheetHeaders)
        alphabet = string.ascii_uppercase
        index = (maxColumn - 1) % 26
        letter = alphabet[index]
        self.workSheetrange = f"A:{letter}"
        
        row_list: list = sheet.get(self.workSheetrange)
        row_numbers = len(row_list) - 1
        if row_numbers == 0:
            return
        if row_list: row_list.pop(0)
        
        self.controllerGoogleSheets.eraseSheet(self.workSheetId,self.lastUpdateSheetId, self.workSheetHeaders)
        self.controllerGoogleSheets.eraseSheet(self.workSheetId,self.bookSheetId, self.workSheetHeaders)
        
        book_list: list[Book] = []
        filteredRows = []
        
        for row in row_list:
            _index = row_list.index(row)
            if not row or row[0] == '':
                continue
            
            table_range = f'A{row_numbers}:{letter}{row_numbers}'
            
            if row != self.workSheetHeaders:

                book = Book(
                address=row[0],
                name=row[1],
                is_lumx=bool(int(row[2])),
                is_safe=bool(int(row[3])),
                blockchain=row[4],
                is_conversion=bool(int(row[5])),
                is_primarysale=bool(int(row[6])),
                is_secondarysale=bool(int(row[7])),
                project=row[8]
                )
                if book.address:
                    book_list.append(book)
                    if row not in filteredRows: filteredRows.append(row)
        
        self.controllerGoogleSheets.openSheet(self.workSheetId,self.lastUpdateSheetId)
        self.controllerGoogleSheets.writemanyRows(filteredRows)
        return book_list if row_list else None
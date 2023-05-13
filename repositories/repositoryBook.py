import psycopg2
from entities.entityBook import Book
from repositories.repositoryBase import RepositoryBase

class RepositoryBook ( RepositoryBase ):
    def __init__(self, connection: str, engine: str, schema: str = 'finance', tableName: str ='book'):
        self.tableName = tableName
        self.schema = schema
        self.connection: psycopg2.connection = connection
        super().__init__(connection, engine, schema, tableName)

    def insert(self, lst: list[Book]) -> None:
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
            
            except:
                raise Exception
            
    def getBook(self) -> list[Book]:
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
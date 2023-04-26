import psycopg2
from entities.entityBook import Book
from repositories.repositoryBase import RepositoryBase

class RepositoryBook ( RepositoryBase ):
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
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
                    (address, name, is_lumx, is_safe, blockchain, is_conversion, is_primarysale, is_secondarysale)
                    VALUES ({placeholders})
                    ON CONFLICT (address) DO UPDATE SET
                    name = excluded.name,
                    is_lumx = excluded.is_lumx,
                    is_safe = excluded.is_safe,
                    blockchain = excluded.blockchain,
                    is_conversion = excluded.is_conversion,
                    is_primarysale = excluded.is_primarysale,
                    is_secondarysale = excluded.is_secondarysale;;
                    """
                    
                cur.executemany(query, values)
                self.connection.commit()
            
            except:
                raise Exception
            
    def getBook(self) -> list[Book]:
        with self.connection.cursor() as cur:
            query = f"SELECT * FROM {self.schema}.{self.tableName} order by is_lumx desc"
            try:
                cur.execute(query=query)
                list_book: list[Book] = []
                for row in cur.fetchall():
                    book = Book(
                    address = row[0],
                    name = row[1],
                    is_lumx = row[2],
                    is_conversion = row[3],
                    is_primarysale = row[4],
                    is_secondarysale = row[5]
                    )
                    list_book.append(book)
                return list_book
            
            except:
                raise Exception
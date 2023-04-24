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
(address, name, is_lumx, is_conversion, is_primarysale, is_secondarysale)
VALUES ({placeholders})
ON CONFLICT (address) DO UPDATE SET
  name = excluded.name,
  is_lumx = excluded.is_lumx,
  is_conversion = excluded.is_conversion,
  is_primarysale = excluded.is_primarysale,
  is_secondarysale = excluded.is_secondarysale;;
"""
                    
                cur.executemany(query, values)
                self.connection.commit()
            
            except Exception as e:
                print(e)
                print(f'\nProblem inserting book registers')
                raise e

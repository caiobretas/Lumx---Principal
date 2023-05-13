
import logging
from repositories.repositoryBase import RepositoryBase
from entities.entityCategory import Category

class RepositoryCategories( RepositoryBase ):
    def __init__(self, connection, engine: str, schema: str, tableName: str):
        super().__init__(connection, engine, schema, tableName)

    def insertCategories(self, list_category: list[Category]):
        values = [t.to_tuple() for t in list_category]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id, projeto, method_id, subcategoria4, subcategoria3,
                    subcategoria2,subcategoria,categoria,categoriaprojecao,
                    categoriacustoreceita)
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO UPDATE SET 
                    id = EXCLUDED.id,
                    projeto = EXCLUDED.projeto,
                    method_id = EXCLUDED.method_id,
                    subcategoria4 = EXCLUDED.subcategoria4,
                    subcategoria3 = EXCLUDED.subcategoria3, 
                    subcategoria2 = EXCLUDED.subcategoria,
                    subcategoria = EXCLUDED.subcategoria,
                    categoria = EXCLUDED.categoria,
                    categoriaprojecao = EXCLUDED.categoriaprojecao"""

                cur.executemany(query, values)
                self.connection.commit()

            except Exception as e:
                logging.error(f"Error: {e}")
                raise Exception
    
    def getCategories(self):
        query = f"""SELECT * FROM {self.schema}.{self.tableName}
        order by categoriaprojecao asc;"""
        super().run_query(query=query)
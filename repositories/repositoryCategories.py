import logging
from pandas import DataFrame

from repositories.repositoryBase import RepositoryBase
from entities.entityCategory import Category

class RepositoryCategories( RepositoryBase ):
    def __init__(self, connection, engine: str):
        self.schema = 'finance' # postgresql
        self.tableName = 'categories' # postgresql
        self.worksheetName = 'categories' # excel
        super().__init__(connection,engine,self.schema,self.tableName)

    def insertCategories(self, list_category: list[Category]| None):
        if list_category != None:
            values = [t.to_tuple() for t in list_category]
            with self.connection.cursor() as cur:
                try:
                    placeholders = ','.join(['%s'] * len(values[0]))
                    query = f"""
                        INSERT INTO {self.schema}.{self.tableName}
                        (id, recorrencia, projeto, produto, method_id, subcategoria4, subcategoria3,
                        subcategoria2,subcategoria,categoria,categoriaprojecao,
                        categoriacustoreceita)
                        VALUES ({placeholders})
                        ON CONFLICT (id) DO UPDATE SET 
                        recorrencia = EXCLUDED.recorrencia,
                        projeto = EXCLUDED.projeto,
                        produto = EXCLUDED.produto,
                        method_id = EXCLUDED.method_id,
                        subcategoria4 = EXCLUDED.subcategoria4,
                        subcategoria3 = EXCLUDED.subcategoria3, 
                        subcategoria2 = EXCLUDED.subcategoria2,
                        subcategoria = EXCLUDED.subcategoria,
                        categoria = EXCLUDED.categoria,
                        categoriaprojecao = EXCLUDED.categoriaprojecao,
                        categoriacustoreceita = EXCLUDED.categoriacustoreceita"""

                    cur.executemany(query, values)
                    self.connection.commit()
    
                except Exception as e:
                    logging.error(f"{e}")
                    return None
        else:
            return None
        
    def getCategories_fromExcel(self) -> list[Category] | None:
        df: DataFrame = super().openDataFrame()            
        try:
            df.fillna(value="", inplace=True)
            list_aux: list[Category] = []
            for index, row in df.iterrows():
                row = Category(
                    id = row['id'],
                    recorrencia= row['recorrência'],
                    projeto = row['projeto'],
                    produto = row['produto'],
                    method_id = row['method_id'],
                    subcategoria4 = row['subcategoria4'],
                    subcategoria3 = row['subcategoria3'],
                    subcategoria2 = row['subcategoria2'],
                    subcategoria = row['subcategoria'],
                    categoria = row['categoria'],
                    categoriaprojecao = row['categoriaprojecao'],
                    categoriacustoreceita= row['categoriacustoreceita']
                    )
                list_aux.append(row)
            return list_aux
        except Exception as e:
            logging.error(f'Erro: {e}')
            return None   
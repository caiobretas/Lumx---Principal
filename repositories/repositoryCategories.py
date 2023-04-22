from repositories.repositoryBase import RepositoryBase
from entities.entityCategory import Category

class RepositoryCategories( RepositoryBase ):
    def __init__(self, connection: str, engine: str, schema: str, tableName: str):
        super().__init__(connection, engine, schema, tableName)

    def insertCategories(self, lst: list[Category]):
        super().salvaDatabase(lst=lst)
    
    def getCategories(self):
        query = f"""SELECT * FROM {self.schema}.{self.tableName}
        order by categoriaprojecao asc;"""
        super().run_query(query=query)
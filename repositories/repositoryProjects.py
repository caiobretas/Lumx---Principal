from entities.entityProject import Project

from repositories.repositoryBase import RepositoryBase

from entities.entityClient import Client

class RepositoryProjects ( RepositoryBase ):
    def __init__(self, connection, engine: str, schema: str, tableName: str):
        super().__init__(connection= connection, engine=engine, schema=schema, tableName=tableName)
    
    def insereProjeto(self, lst: list[Project]):
        super().salvaDatabase(lst)
import logging
from entities.legal.entityDocument import Document
from repositories.repositoryBase import RepositoryBase

class RepositoryDocuments(RepositoryBase):
    def __init__(self,connection, engine):
        self.driveId = '0AOWIfBoIehBbUk9PVA'
        self.tableName = 'documents'
        self.schema = 'legal'
        super().__init__(connection, engine, self.schema,self.tableName)
    
    def runQuery(self, query) -> list:
        try:
            with self.connection.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        except Exception as e:
            logging.error(e)
            
    def insertDocuments(self, list_documents: list[Document]):
        if not list_documents:
            return None
        values = [t.to_tuple() for t in list_documents]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id,googleid,name,type,drive,path,webLink,createdTime,modifiedTime,parents,trashed)
                    VALUES ({placeholders})
                    ON CONFLICT (googleid) DO
                    UPDATE SET
                    name = EXCLUDED.name,
                    type = EXCLUDED.type,
                    drive = EXCLUDED.drive,
                    path = EXCLUDED.path,
                    webLink = EXCLUDED.webLink,
                    createdTime = EXCLUDED.createdTime,
                    modifiedTime = EXCLUDED.modifiedTime,
                    parents = EXCLUDED.parents,
                    trashed = EXCLUDED.trashed
                    """
                cur.executemany(query, values)
                self.connection.commit()

            except Exception as e:
                logging.error(e)
    
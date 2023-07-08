import logging
from entities.legal.entityDocument import LegalDocument
from repositories.repositoryBase import RepositoryBase

class RepositoryLegalDocuments(RepositoryBase):
    def __init__(self,connection, engine):
        self.driveId = '0AOWIfBoIehBbUk9PVA'
        self.tableName = 'documents_categories'
        self.schema = 'legal'
        super().__init__(connection, engine, self.schema,self.tableName)
    
    def runQuery(self, query) -> list:
        try:
            with self.connection.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        except Exception as e:
            logging.error(e)
            
    def insert(self, list_documents: list[LegalDocument]):
        if not list_documents:
            return None
        values = [t.to_tuple() for t in list_documents]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id,nome,categoria1,categoria2,categoria3,categoria4,categoria5)
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO
                    UPDATE SET
                    nome = EXCLUDED.nome,
                    categoria1 = EXCLUDED.categoria1,
                    categoria2 = EXCLUDED.categoria2,
                    categoria3 = EXCLUDED.categoria3,
                    categoria4 = EXCLUDED.categoria4,
                    categoria5 = EXCLUDED.categoria5
                    """
                cur.executemany(query, values)
                self.connection.commit()

            except Exception as e:
                logging.error(e)
    
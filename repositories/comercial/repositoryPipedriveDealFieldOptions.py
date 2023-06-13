import logging
from ..repositoryBase import RepositoryBase
from entities.comercial.entityPipedriveDealFields import PipedriveDealFieldOptions

class RepositoryPipedriveDealFieldOptions(RepositoryBase):
    def __init__(self,connection, engine):
        self.schema = 'comercial'
        self.tableName = 'pipe_dealfieldoptions'
        super().__init__(connection, engine, self.schema, self.tableName)
    
    def insert(self, list_deals: list[PipedriveDealFieldOptions]) -> None:
        if not list_deals:
            return None
        values = [t.to_tuple() for t in list_deals]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id,dealfield_id, internal_id, label)
                    VALUES ({placeholders})
                    ON CONFLICT (internal_id) DO
                    UPDATE SET
                    id = EXCLUDED.id,
                    dealfield_id = EXCLUDED.dealfield_id,
                    label = EXCLUDED.label
                    
                    """
                cur.executemany(query, values)
                self.connection.commit()

            except Exception as e:
                logging.error(e)
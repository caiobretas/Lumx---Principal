import logging
from ..repositoryBase import RepositoryBase
from entities.comercial.entityPipedriveDealFields import PipedriveDealFields

class RepositoryPipedriveDealFields(RepositoryBase):
    def __init__(self,connection, engine):
        self.schema = 'comercial'
        self.tableName = 'pipe_dealfields'
        super().__init__(connection, engine, self.schema, self.tableName)
    
    def insert(self, list_deals: list[PipedriveDealFields]) -> None:
        if not list_deals:
            return None
        values = [t.to_tuple() for t in list_deals]
        with self.connection.cursor() as cur:
            try:
                placeholders = ','.join(['%s'] * len(values[0]))
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id,key,name,order_nr,field_type,json_column_flag,add_time,update_time,last_updated_by_user_id,edit_flag,details_visible_flag,add_visible_flag,important_flag,bulk_edit_allowed,filtering_allowed,sortable_flag,searchable_flag,active_flag,projects_detail_visible_flag)
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO
                    UPDATE SET
                    key = EXCLUDED.key,
                    name = EXCLUDED.name,
                    order_nr = EXCLUDED.order_nr,
                    field_type = EXCLUDED.field_type,
                    json_column_flag = EXCLUDED.json_column_flag,
                    add_time = EXCLUDED.add_time,
                    update_time = EXCLUDED.update_time,
                    last_updated_by_user_id = EXCLUDED.last_updated_by_user_id,
                    details_visible_flag = EXCLUDED.details_visible_flag,
                    add_visible_flag = EXCLUDED.add_visible_flag,
                    important_flag = EXCLUDED.important_flag,
                    bulk_edit_allowed = EXCLUDED.bulk_edit_allowed,
                    filtering_allowed = EXCLUDED.filtering_allowed,
                    sortable_flag = EXCLUDED.sortable_flag,
                    searchable_flag = EXCLUDED.searchable_flag,
                    active_flag = EXCLUDED.active_flag,
                    projects_detail_visible_flag = EXCLUDED.projects_detail_visible_flag
                    """
                cur.executemany(query, values)
                self.connection.commit()

            except Exception as e:
                logging.error(e)
                

  
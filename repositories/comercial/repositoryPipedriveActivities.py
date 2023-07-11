import logging
from repositories.repositoryBase import RepositoryBase
from entities.comercial.entityPipedriveActivity import PipedriveActivity

class RepositoryPipedriveActivites (RepositoryBase):
    
    def __init__(self, connection, engine):
        self.schema = 'comercial'
        self.tableName = 'pipe_activities'
        super().__init__(connection, engine, self.schema, self.tableName)
        
    def insert(self, list_activities: list[PipedriveActivity]):
        if not list_activities:
            return
        values = [t.to_tuple() for t in list_activities]
        with self.connection.cursor() as cur:
            placeholders = ','.join(['%s'] * len(values[0]))
            try:
                query = f"""
                    INSERT INTO {self.schema}.{self.tableName}
                    (id,done,type,duration,subject,company_id,user_id,conference_meeting_client,conference_meeting_url,conference_meeting_id,due_date,due_time,busy_flag,add_time,marked_as_done_time,public_description,location,org_id,person_id,deal_id,active_flag,update_time,update_user_id,source_timezone,lead_id,location_subpremise,location_street_number,location_route,location_sublocality,location_locality,location_admin_area_level_1,location_admin_area_level_2,location_country,location_postal_code,location_formatted_address,project_id)
                    VALUES ({placeholders})
                    ON CONFLICT (id) DO
                    UPDATE SET
                    id = EXCLUDED.id,
                    done = EXCLUDED.done,
                    type = EXCLUDED.type,
                    duration = EXCLUDED.duration,
                    subject = EXCLUDED.subject,
                    company_id = EXCLUDED.company_id,
                    user_id = EXCLUDED.user_id,
                    conference_meeting_client = EXCLUDED.conference_meeting_client,
                    conference_meeting_url = EXCLUDED.conference_meeting_url,
                    conference_meeting_id = EXCLUDED.conference_meeting_id,
                    due_date = EXCLUDED.due_date,
                    due_time = EXCLUDED.due_time,
                    busy_flag = EXCLUDED.busy_flag,
                    add_time = EXCLUDED.add_time,
                    marked_as_done_time = EXCLUDED.marked_as_done_time,
                    public_description = EXCLUDED.public_description,
                    location = EXCLUDED.location,
                    org_id = EXCLUDED.org_id,
                    person_id = EXCLUDED.person_id,
                    deal_id = EXCLUDED.deal_id,
                    active_flag = EXCLUDED.active_flag,
                    update_time = EXCLUDED.update_time,
                    update_user_id = EXCLUDED.update_user_id,
                    source_timezone = EXCLUDED.source_timezone,
                    lead_id = EXCLUDED.lead_id,
                    location_subpremise = EXCLUDED.location_subpremise,
                    location_street_number = EXCLUDED.location_street_number,
                    location_route = EXCLUDED.location_route,
                    location_sublocality = EXCLUDED.location_sublocality,
                    location_locality = EXCLUDED.location_locality,
                    location_admin_area_level_1 = EXCLUDED.location_admin_area_level_1,
                    location_admin_area_level_2 = EXCLUDED.location_admin_area_level_2,
                    location_country = EXCLUDED.location_country,
                    location_postal_code = EXCLUDED.location_postal_code,
                    location_formatted_address = EXCLUDED.location_formatted_address,
                    project_id = EXCLUDED.project_id
                    """
                cur.executemany(query, values)
                self.connection.commit()
            except Exception as e:
                print(f'Erro ao inserir dados no banco: {self.schema}.{self.tableName}')
                logging.error(e)
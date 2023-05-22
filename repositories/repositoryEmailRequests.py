from repositories.repositoryBase import RepositoryBase
from entities.entityEmailRequest import EmailRequest
import logging

class RepositoryEmailRequests(RepositoryBase):

    def __init__(self, connection, engine: str):
        self.schema = 'admin' # postgresql
        self.tableName = 'email_requests' # postgresql
        super().__init__(connection,engine,self.schema,self.tableName)

    def insertEmailRequests(self, list_requests: list[EmailRequest]| None):
        if list_requests != None:
            values = [t.to_tuple() for t in list_requests]
            with self.connection.cursor() as cur:
                try:
                    placeholders = ','.join(['%s'] * len(values[0]))
                    query = f"""
                        INSERT INTO {self.schema}.{self.tableName}
                        (id, external_id, draft_id, email_id,datetime,request_type,contact_id,from_,to_,subject,answered,atacchment,pending,concluded)
                        VALUES ({placeholders})
                        ON CONFLICT DO UPDATE SET
                        draft_id = EXCLUDED.draft_id,
                        email_id = EXCLUDED.email_id,
                        datetime = EXCLUDED.datetime,
                        request_type = EXCLUDED.request_type,
                        contact_id = EXCLUDED.contact_id,
                        from_ = EXCLUDED.from_,
                        to_ = EXCLUDED.to_,
                        subject = EXCLUDED.subject,
                        answered = EXCLUDED.answered,
                        atacchment = EXCLUDED.atacchment,
                        pending = EXCLUDED.pending,
                        concluded = EXCLUDED.concluded
                        """
                    cur.executemany(query, values)
                    self.connection.commit()
    
                except Exception as e:
                    logging.error(f"{e}")
                    return None
        else:
            return None
        
    def getEmailRequests(self):
        try:
            with self.connection.cursor() as cursor:
                query = f'select * from {self.schema}.{self.tableName}'
                cursor.execute(query)
                list_requests: list[EmailRequest] = []
                for row in cursor.fetchall():
                    email_request = EmailRequest(
                        id = row[0],
                        external_id = row[1],
                        draft_id = row[2],
                        email_id = row[3],
                        datetime = row[4],
                        request_type = row[5],
                        contact_id = row[6],
                        from_ = row[7],
                        to_ = row[8],
                        subject = row[9],
                        answered = row[10],
                        atacchment = row[11],
                        pending = row[12],
                        concluded = row[13])
                    list_requests.append(email_request)
            return list_requests        
        except Exception as e:
            logging.error(e)
            return None
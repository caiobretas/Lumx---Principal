from repositories.repositoryBase import RepositoryBase
from repositories.repositoryContacts import RepositoryContacts
from entities.entityEmailRequest import EmailRequest
import logging

class RepositoryEmailRequests(RepositoryBase):

    def __init__(self, connection, engine: str):
        self.schema = 'admin' # postgresql
        self.tableName = 'email_requests' # postgresql
        super().__init__(connection,engine,self.schema,self.tableName)
        self.repositoryContacts: RepositoryContacts = RepositoryContacts(connection, engine)

    def insertEmailRequests(self, list_requests: list[EmailRequest]| None):
        if list_requests != None:
            values = [t.to_tuple() for t in list_requests]
            with self.connection.cursor() as cur:
                try:
                    placeholders = ','.join(['%s'] * len(values[0]))
                    query = f"""
                        INSERT INTO {self.schema}.{self.tableName}
                        (id, external_id,draft_id,email_id,datetime,request_type,contact_id,from_,to_,subject,answered,attachment, attachment_id,pending,concluded)
                        VALUES ({placeholders})
                        ON CONFLICT (email_id) DO UPDATE SET
                        draft_id = EXCLUDED.draft_id,
                        email_id = EXCLUDED.email_id,
                        request_type = EXCLUDED.request_type,
                        contact_id = EXCLUDED.contact_id,
                        from_ = EXCLUDED.from_,
                        to_ = EXCLUDED.to_,
                        subject = EXCLUDED.subject,
                        answered = EXCLUDED.answered,
                        attachment = EXCLUDED.attachment,
                        attachment_id = EXCLUDED.attachment_id,
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
        
    def getEmailRequests(self, concludedOnly=False, pendingOnly=False,request_type='Invoice'):
        
        query = f"select e.*, c.nome from {self.schema}.{self.tableName} as e left join {self.repositoryContacts.schema}.{self.repositoryContacts.tableName} as c on c.id = e.contact_id where request_type='{request_type}'"
        query = query + f" and concluded = {concludedOnly}" if concludedOnly else query + " and not concluded"
        
        if pendingOnly: query = query + f" and pending = {pendingOnly}"
        
        
        self.messageId_list: list = []
        self.externalId_list: list = []
        try:
            with self.connection.cursor() as cursor:
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
                        contact_name = row[15],
                        from_ = row[7],
                        to_ = row[8],
                        subject = row[9],
                        answered = row[10],
                        attachment = row[11],
                        attachment_id = row[12],
                        pending = row[13],
                        concluded = row[14])
                    self.messageId_list.append(email_request.email_id)
                    self.externalId_list.append(email_request.external_id)
                    list_requests.append(email_request)
                    
            return list_requests        
        except Exception as e:
            logging.error(e)
            return None
from repositories.repositoryEmailRequests import RepositoryEmailRequests
from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from entities.entityEmailRequest import EmailRequest
class UpdateEmailRequests:
    def __init__(self, connection=None, engine=None):
        self.repositoryEmailRequests = RepositoryEmailRequests(connection, engine) if connection != None and engine != None else None
        self.controllerGmail = GoogleGmail()
        self.mailUpdates: list = []
    
    def updateEmailRequests(self):
        emailRequests_list = self.repositoryEmailRequests.getEmailRequests(False, False, 'Invoice')
        
        if not emailRequests_list:
            return None
        
        
        for request in emailRequests_list:
            if request.contact_name == 'Thamyres Guedes Reis Corrêa':
                print(1)
            
            mail: dict = self.controllerGmail.getMessagebyId(request.email_id)
            thread: dict = self.controllerGmail.getThreadById(mail['threadId'])
            messages_list: list[dict] = thread.get('messages', None)
            
            attachmentId = None
            attachment = None
            
            attachment_list: list = []
            for message in messages_list:
                
                payload: dict = message.get('payload', None)
                if not payload: continue
                     
                parts: list[dict] = payload.get('parts', None)
                if not parts: continue
            
                for part in parts:
                    body: dict = part.get('body', None)
                    if not body: continue
                    attachmentId = body.get('attachmentId', None)
                    if not attachmentId: continue
                    
                    attachment: tuple = self.controllerGmail.getAttachmentById(message['id'],attachmentId)
                
                attachment_list.append(attachment)
                
                if attachment_list:
                    request.attachment = True

                request_update = EmailRequest(
                    id = request.id, 
                    external_id = request.external_id,
                    draft_id = request.draft_id,
                    email_id = request.email_id, 
                    datetime = request.datetime,
                    request_type = request.request_type,
                    contact_id = request.contact_id,
                    from_ = request.from_,
                    to_ = request.to_,
                    subject = request.subject,
                    answered = True if len(messages_list) > 1 else False,
                    pending = True,
                    concluded = False
                )
                
                request_update.attachment = True if attachmentId else False
                request_update.attachment_id = attachmentId if attachmentId else None
                request_update.pending = False if (request_update.answered and request_update.attachment) else True
                request_update.concluded = True if request_update.attachment_id else False # write condition to check if the attachment is accepted
            
            self.mailUpdates.append(request_update)
                
        self.repositoryEmailRequests.insertEmailRequests(self.mailUpdates)
        print('\nEmail Requests Updated')
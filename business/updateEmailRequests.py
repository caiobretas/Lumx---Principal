from repositories.repositoryEmailRequests import RepositoryEmailRequests
from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from entities.entityEmailRequest import EmailRequest
class UpdateEmailRequests:
    def __init__(self, connection=None, engine=None):
        self.repository = RepositoryEmailRequests(connection, engine) if connection != None and engine != None else None
        self.controller = GoogleGmail()
    
        # get mail updates from gmail
        mailUpdates: list = []
        emailRequests_list = self.repository.getEmailRequests(True)
        for request in emailRequests_list:
            if len(emailRequests_list) == 0:
                break    
            mail: dict = self.controller.getMessagebyId(request.email_id)
            thread: dict = self.controller.getThreadById(mail['threadId'])
            attachments: list = []
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
                answered = True if len(thread['messages']) > 1 else False,
                attachment = True if request.attachment_id != None else request.attachment_id,            
                attachment_id = request.attachment_id,
                pending = True,
                concluded = False
            )
    
            mailUpdates.append(request_update)
        self.repository.insertEmailRequests(mailUpdates)
            
        a = 1
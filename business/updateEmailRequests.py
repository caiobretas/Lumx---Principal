from repositories.repositoryEmailRequests import RepositoryEmailRequests
from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from entities.entityEmailRequest import EmailRequest
class UpdateEmailRequests:
    def __init__(self, connection=None, engine=None):
        self.repository = RepositoryEmailRequests(connection, engine) if connection != None and engine != None else None
        self.controller = GoogleGmail()
        mailUpdates: list = []
        
        emailRequests_list = self.repository.getEmailRequests(True)
        if emailRequests_list:
            for request in emailRequests_list:
                attachment_list: list = []
                mail: dict = self.controller.getMessagebyId(request.email_id)
                thread: dict = self.controller.getThreadById(mail['threadId'])
                messages_list: list[dict] = thread['messages']
                for message in messages_list:
                    try:
                        for part in message['payload']['parts']:
                            try:
                                attachmentId = part['body']['attachmentId']
                                attachment: tuple = self.controller.getAttachmentById(message['id'],attachmentId)
                                attachment_list.append(attachment)
                            except KeyError:
                                continue
                    except KeyError:
                        attachmentId = None
                        attachment = None
                        continue
            
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
                
                request.attachment = True if attachmentId else False
                request.attachment_id = attachmentId if attachmentId else None
                request.pending = False if (request.answered and request.attachment) else True
                request.concluded = True # write condition to check if the attachment is accepted
                mailUpdates.append(request_update)
                
        self.repository.insertEmailRequests(mailUpdates)
        print('\nEmail Requests Updated')
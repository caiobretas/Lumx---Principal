import logging
from time import time
from googleapiclient.errors import HttpError
from repositories.repositoryEmailRequests import RepositoryEmailRequests
from controllers.controllerGoogle.controllerGoogleGmail import GoogleGmail
from controllers.controllerGoogle.controllerGoogleDrive import GoogleDrive
from entities.entityEmailRequest import EmailRequest
class UpdateEmailRequests:
    
    def __init__(self, connection=None, engine=None):
        self.repositoryEmailRequests = RepositoryEmailRequests(connection, engine) if connection != None and engine != None else None
        self.controllerGmail = GoogleGmail()
        self.controllerDrive = GoogleDrive()
        self.mailUpdates: list = []
    
    def update(self):
        start_time = time()
        self.mailUpdates.clear()
        print('\nUpdating Email Requests...')
        
        emailRequests_list: list[EmailRequest] = self.repositoryEmailRequests.getEmailRequests(False, False, 'Invoice')
        
        if not emailRequests_list:
            status = 'Empty'
            try_time = time()
            print('{} Status: {} - Time: {:.2f}s'.format(' ' * 3,status, try_time - start_time))
            return None
        
        for request in emailRequests_list:
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
                
                if not attachment: continue
                if attachment: attachment_list.append(attachment)
                
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
                
                request_update.pending = False if (request_update.answered and request_update.attachment) else True
                request_update.concluded = True if request_update.attachment_id else False # write condition to check if the attachment is accepted
            
                if attachmentId:
                    request_update.attachment_id = attachmentId
                    request_update.attachment = True
                    try:
                        binary = self.controllerGmail.getAttachmentById(request.email_id, attachmentId)[1]
                        self.controllerDrive.uploadFile(binary, request.subject, '1lPF_AJywPuJ2bxJ2ppDl7hX9MZ2HUKRw')
                        request_update.concluded = True
                    except HttpError as err:
                        logging.error(err)
                        request_update.concluded = False   
            
                # se attachment Id;
                # renomeia o attachment com o subject
                # joga o attachment na pasta
                # marca como concluded
                        
                self.mailUpdates.append(request_update)
                
        self.repositoryEmailRequests.insertEmailRequests(self.mailUpdates)
        print('\n{}Email Requests updated in {:.2f} seconds\n'.format(' ' * 3,time() - start_time))
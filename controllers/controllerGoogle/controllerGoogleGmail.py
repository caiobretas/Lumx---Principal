import logging
import base64
from googleapiclient.errors import HttpError
from controllers.controllerGoogle.controllerGoogle import ControllerGoogle
from googleapiclient.discovery import build, Resource
from email.message import EmailMessage

class GoogleGmail(ControllerGoogle):

    def __init__(self):
        try:
            super().__init__()

            self.service: Resource = build('gmail', 'v1', credentials=self.credential)
        
        except Exception as e:
            logging.error(e)

    def createDraft(self, from_:str=None, to:str=None, cc_list:list=None, subject:str=None, message_body:str=None, messageId:str=None):
        '''Cria um rascunho e retorna o rascunho'''
       
        message = EmailMessage()
        message.set_content(message_body)
        
        message['To'] = f'{to}'
        message['From'] = f'{from_}'
        message['Subject'] = f'{subject}'
        if cc_list: message['Cc'] = cc_list
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()    
        
        try:   
            if not messageId:
                create_message = {
                    'message': {
                        'raw': encoded_message
                    }
                }
            else:
                message: dict = self.service.users().messages().get(userId='me', id=messageId, format='full').execute()
                create_message = {
                    'message': {
                        'raw': encoded_message,
                        'threadId': message.get('threadId', None),
                        'inReplyTo': messageId,
                        'references': [messageId]
                    }
                }
            
            return self.service.users().drafts().create(userId='me', body=create_message).execute()      
        except Exception as e:
            logging.error(e)

            
    def sendDraft(self, draft_id):
        '''Sends a draft and returns the email sent'''
        body = {'id': draft_id}
        email = self.service.users().drafts().send(userId='me', body=body).execute()
        return email
    
    def sendMessage(self, subject, content, to, from_):
        message = EmailMessage()
        message.set_content(content)
        message['To'] = f'{to}'
        message['From'] = f'{from_}'
        message['Subject'] = f'{subject}'
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            'raw': encoded_message
        }
        try:
            self.service.users().messages().send(userId='me', body=create_message).execute()
            print('E-mail enviado com sucesso!')
        except HttpError as error:
            logging.error(error)
            print(f'Erro ao enviar e-mail: {error}')
    
    def getMessagebyId(self,messageId):
        try:
            emailmessage = self.service.users().messages().get(userId='me',id=f'{messageId}').execute()
            return emailmessage
        except HttpError as error:
            emailmessage = None
            logging.error(error)
            return None
        
    def getThreadById(self,threadId):
        try:
            thread = self.service.users().threads().get(userId='me',id=f'{threadId}').execute()
            return thread
        
        except HttpError as error:
            thread = None
            logging.error(error)
            return None
    
    def getAttachmentById(self, messageId, attachmentId) -> tuple:
        'return a tuple: (attachment, binary)'
        try:
            attachment: dict = self.service.users().messages().attachments().get(userId='me',messageId=messageId, id=f'{attachmentId}').execute()
            data_encoded = attachment.get('data', None)
            binary = base64.urlsafe_b64decode(data_encoded)
            return (attachment, binary)
        
        except KeyError:
            return None
        
        except HttpError as error:
            attachment = None
            logging.error(error)
            return None
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
    
    def getEmails(self):        
        try:
            response = self.service.users().messages().list(userId='me').execute()
            # Obter os IDs dos emails retornados
            messages = response.get('messages', [])

            # Iterar sobre os emails
            for message in messages:
                email_id = message['id']
                # Você pode fazer outras chamadas à API do Gmail para obter detalhes específicos do email usando o ID, como o assunto, remetente, etc.
                email = self.service.users().messages().get(userId='me', id=email_id).execute()
                subject = email['payload']['headers'][18]['value']  # Exemplo para obter o assunto do email
                print(subject)
        except Exception as e:
            logging.error(e)
            
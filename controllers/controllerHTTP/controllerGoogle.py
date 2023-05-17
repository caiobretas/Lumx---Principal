from __future__ import print_function
import base64
import logging
from googleapiclient.errors import HttpError
import gspread
from entities.Credentials import MyCredentials
class ControllerGoogle:
    def __init__(self):
        
        try:
            self.credential = MyCredentials.get_credentials()
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
            
from gspread import Spreadsheet, Worksheet            
class GoogleSheets(ControllerGoogle):
    def __init__(self):
        super().__init__()
        try:
            self.client = gspread.authorize(credentials=self.credential)
        except Exception as e:
            logging.error(e)
        
    def getRow(self, rowNumber, sheetName, worksheetId: str):
        try:
            worksheet: Spreadsheet = self.client.open_by_key(worksheetId)
            sheet: Worksheet = worksheet.worksheet(sheetName)
            return sheet.row_values(rowNumber)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
            
    def appendRow(self, values: list, sheetName, worksheetId: str):
        try:
            worksheet: gspread.Spreadsheet = self.client.open_by_key(worksheetId)
            sheet: gspread.worksheet.Worksheet = worksheet.worksheet(sheetName)
            sheet.append_row(values)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
            
    def overwriteWorksheet_byID(self, worksheetId: str, list_values: list, sheetName = None,range=None):
        try:
            worksheet = self.client.open_by_key(worksheetId)
            sheet = worksheet.worksheet(sheetName)
            headers = self.getRow(1,sheetName,worksheetId)
            sheet.clear()
            sheet.append_row(values=headers, table_range='A1')
            sheet.append_rows(values=list_values,table_range=range)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')

from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.discovery import Resource
class GoogleGmail(ControllerGoogle):

    def __init__(self):
        try:
            super().__init__()

            self.service: Resource = build('gmail', 'v1', credentials=self.credential)
            
        except Exception as e:
            logging.error(e)

    def setMessage(self):
        message = EmailMessage()
        message.set_content('Tu é gay man?')
        message['To'] = 'joao.fernandes@lumxstudios.com'
        message['From'] = 'financeiro@lumxstudios.com'
        message['Subject'] = 'Tu é man?'
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
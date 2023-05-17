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
        self.client = gspread.authorize(credentials=self.credential)
        
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

class GoogleGmail(ControllerGoogle):

    def __init__(self):
        try:
            super().__init__()
            # self.oauth2credentials = InstalledAppFlow.from_client_secrets_file(self.oauth2_credentials_path, SCOPES=SCOPES)
            
            self.service = build('gmail', 'v1', credentials=self.credential)
        except Exception as e:
            logging.error(e)

    def setMessage(self):
        message = EmailMessage()
        message.set_content('Consegui')
        message['To'] = 'arthur.marques@lumxstudios.com'
        message['From'] = 'financeiro@lumxstudios.com'
        message['Subject'] = 'E-mail teste API GMAIL'
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
            
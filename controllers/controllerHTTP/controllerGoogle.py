from __future__ import print_function
import json
import base64
import logging
from googleapiclient.errors import HttpError
import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials

from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase

class ControllerGoogle:
    def __init__(self):
        try:
            credentialsPath = 'credentials/credentialsGoogle.json'
            scopes = [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://mail.google.com',
                'https://www.googleapis.com/auth/gmail.modify',
                'https://www.googleapis.com/auth/gmail.compose',
                'https://www.googleapis.com/auth/gmail.send',
                'https://mail.google.com/',
                    ]

            with open(credentialsPath, 'r') as arquivo:
                self.jsoncredentials = json.load(arquivo)

            self.credentials: ServiceAccountCredentials = ServiceAccountCredentials.from_json_keyfile_name(filename=credentialsPath, scopes=scopes)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
    
from gspread import Spreadsheet, Worksheet            
class GoogleSheets(ControllerGoogle):
    def __init__(self):
        super().__init__()
        self.client = gspread.authorize(credentials=self.credentials)
        
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
from googleapiclient.discovery import Resource, build
class GoogleGmail(ControllerGoogle):
    
    def __init__(self):

        try:
            super().__init__()
            self.service: Resource = build('gmail', 'v1', credentials=self.credentials)
            c = dir(self.service.users().drafts())

        except Exception as e:
            logging.error(e)
            
class GoogleGmail(ControllerGoogle):

    def __init__(self):
        try:
            super().__init__()
            self.service = build('gmail', 'v1', credentials=self.credentials)
        except Exception as e:
            logging.error(e)

    def setMessage(self):
        message = EmailMessage()
        message.set_content('Teste')
        message['To'] = 'caiodbretas@icloud.com'
        message['From'] = 'caio.bretas@lumxstudios.com'
        message['Subject'] = 'Teste'
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {
            'raw': encoded_message
        }
        try:
            self.service.users().messages().send(userId='me', body=create_message).execute()
            print('E-mail enviado com sucesso!')
        except HttpError as error:
            print(f'Erro ao enviar e-mail: {error}')
            
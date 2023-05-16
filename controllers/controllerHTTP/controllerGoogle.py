from __future__ import print_function
import json
import base64
import logging
from flask import Flask
from googleapiclient.errors import HttpError
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google_auth_oauthlib.flow import InstalledAppFlow

class ControllerGoogle:
    def __init__(self):
        try:
            webService_credentials_path = 'credentials/credentialsGoogle/webServicecredentials.json'
            oauth2_credentials_path = 'credentials/credentialsGoogle/oAuth2_credentials.json'
            scopes =[
                'https://www.googleapis.com/auth/spreadsheets',
                'https://mail.google.com',
                'https://www.googleapis.com/auth/gmail.modify',
                'https://www.googleapis.com/auth/gmail.compose',
                'https://www.googleapis.com/auth/gmail.send',
                'https://mail.google.com/',
                ]

            with open(webService_credentials_path) as arquivo:
                self.jsonWebServicecredentials = json.load(arquivo)
            with open(oauth2_credentials_path) as arquivo:
                self.jsonoauth2credentials = json.load(arquivo)
            
            # with Flask(__name__).run(port=8000) as app:
            #     self.oauth2credentials = InstalledAppFlow.from_client_secrets_file(oauth2_credentials_path, scopes=scopes).run_local_server(port=5000)
            #     return app
            self.webserviceCredentials: ServiceAccountCredentials = ServiceAccountCredentials.from_json_keyfile_name(filename=webService_credentials_path, scopes=scopes)
        
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
    
from gspread import Spreadsheet, Worksheet            
class GoogleSheets(ControllerGoogle):
    def __init__(self):
        super().__init__()
        self.client = gspread.authorize(credentials=self.webserviceCredentials)
        
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
            # self.oauth2credentials = InstalledAppFlow.from_client_secrets_file(self.oauth2_credentials_path, scopes=scopes)
            
            self.service = build('gmail', 'v1', credentials=self.oauth2credentials)
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
            logging.error(error)
            print(f'Erro ao enviar e-mail: {error}')
            
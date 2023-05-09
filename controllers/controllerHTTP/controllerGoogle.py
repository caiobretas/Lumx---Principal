import logging
import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials

from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase

class ControllerGoogle:
    def __init__(self):
        try:
            credentialsPath = 'credentials/credentialsGoogle.json'
            scopes = [
                'https://www.googleapis.com/auth/spreadsheets'
                      ]
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(filename=credentialsPath, scopes=scopes)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
            
class GoogleSheets(ControllerGoogle):
    def __init__(self):
        super().__init__()
        self.client = gspread.authorize(credentials=self.credentials)
        
    def appendRow(self, values: list, sheetName, worksheetId: str):
        try:
            worksheet = self.client.open_by_key(worksheetId)
            sheet = worksheet.worksheet(sheetName)
            sheet.append_row(values)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
            
    def updateWorksheet_byID(self, worksheetId: str, list_values: list, sheetName = None,range=None):
        try:
            worksheet = self.client.open_by_key(worksheetId)
            sheet = worksheet.worksheet(sheetName)
            sheet.update(range,list_values)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')


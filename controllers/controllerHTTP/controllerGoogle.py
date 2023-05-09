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
        
    def updateWorksheet_byID(self, worksheetId: str, list_values: list[list], sheetName=None, start_row=2, start_col=1):
        try:
            worksheet = self.client.open_by_key(worksheetId).worksheet(sheetName)
            headers = worksheet.row_values(1)
            if not headers:
                worksheet.insert_row(list(list_values[0].keys()), 1)
            else:
                list_values = list_values
                range_str = f"{sheetName}!{chr(start_col + 64)}{start_row}:{chr(start_col + len(headers) - 1 + 64)}{len(list_values) + start_row - 1}"
                worksheet.update(range_str, list_values)
        
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')

import logging
import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials

from controllers.controllerHTTP.controllerHTTPBase import ControllerHTTPBase

class ControllerGoogle:
    def __init__(self):
        try:
            creds = Credentials.from_service_account_file('credentials/credentialsGoogle.json')
            credentials = ServiceAccountCredentials.from_json_keyfile_name(creds, ['https://www.googleapis.com/auth/spreadsheets'])
            print(credentials)
        except Exception as e:
            logging.error(f'{" "* 3} Erro: {e}')
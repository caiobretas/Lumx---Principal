import os
import logging
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow, Flow
from google.oauth2.credentials import Credentials

class MyCredentials:
    creds = None  # Variável estática para armazenar as credenciais
    credentialToken_path = 'credentials/credentialsGoogle/token.json'
    oauth2_credentials_path = 'credentials/credentialsGoogle/oAuth2_credentials.json'
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/gmail.modify',
        'https://www.googleapis.com/auth/gmail.compose',
        'https://www.googleapis.com/auth/gmail.send',
        'https://mail.google.com/'
    ]
    @staticmethod
    def get_credentials() -> Credentials:
        creds = MyCredentials.creds
        try:
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
            if os.path.exists(MyCredentials.credentialToken_path):
                creds = Credentials.from_authorized_user_file(MyCredentials.credentialToken_path, MyCredentials.SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(MyCredentials.oauth2_credentials_path, MyCredentials.SCOPES)
                    creds = flow.run_local_server(port=8080)
                with open(MyCredentials.credentialToken_path,'w') as token:
                    token.write(creds.to_json())    
            return creds
                    
        except Exception as e:
            logging.error(e)
            return None
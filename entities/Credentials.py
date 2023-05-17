# import os
# import logging
# from google.auth.transport.requests import Request
# from google_auth_oauthlib.flow import InstalledAppFlow, Flow
# from google.oauth2.credentials import Credentials

# class MyCredentials:
#     creds = None  # Variável estática para armazenar as credenciais
#     credentialToken_path = 'credentials/credentialsGoogle/token.json'
#     oauth2_credentials_path = 'credentials/credentialsGoogle/oAuth2_credentials.json'
#     SCOPES = [
#         'https://www.googleapis.com/auth/spreadsheets',
#         'https://www.googleapis.com/auth/gmail.modify',
#         'https://www.googleapis.com/auth/gmail.compose',
#         'https://www.googleapis.com/auth/gmail.send',
#         'https://mail.google.com/',
#     ]
#     @staticmethod
#     def get_credentials() -> Credentials:
#         try:
#         # The file token.json stores the user's access and refresh tokens, and is
#         # created automatically when the authorization flow completes for the first
#         # time.
#             if os.path.exists(MyCredentials.credentialToken_path):
#                 MyCredentials.creds = Credentials.from_authorized_user_file(MyCredentials.credentialToken_path, MyCredentials.SCOPES)
#             # If there are no (valid) credentials available, let the user log in.
#             if not MyCredentials.creds or not MyCredentials.creds.valid:
#                 if MyCredentials.creds and MyCredentials.creds.expired and MyCredentials.creds.refresh_token:
#                     MyCredentials.creds.refresh(Request())
#                 else:
#                     flow = InstalledAppFlow.from_client_secrets_file(
#                         MyCredentials.oauth2_credentials_path, MyCredentials.SCOPES)
#                     MyCredentials.creds = flow.run_local_server(port=8080)
#                 # Save the credentials for the next run
#                 with open(MyCredentials.credentialToken_path, 'w') as token:
#                     token.write(MyCredentials.creds.to_json())
#                 return MyCredentials.creds
        
#         except Exception as e:
#             logging.error(e)
#             return None

import os
import logging
import flask
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
        'https://mail.google.com/',
    ]
    @staticmethod
    def get_credentials() -> Credentials:
        try:
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
            if os.path.exists(MyCredentials.credentialToken_path):
                MyCredentials.creds = Credentials.from_authorized_user_file(MyCredentials.credentialToken_path, MyCredentials.SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not MyCredentials.creds or not MyCredentials.creds.valid:
                if MyCredentials.creds and MyCredentials.creds.expired and MyCredentials.creds.refresh_token:
                    MyCredentials.creds.refresh(Request())
                else:
                    flow = Flow.from_client_secrets_file(
                        MyCredentials.oauth2_credentials_path, MyCredentials.SCOPES)
                    flow.redirect_uri = 'http://localhost:8080/oauth/callback'
                    authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')
                    
                # Save the credentials for the next run
                # with open(MyCredentials.credentialToken_path, 'w') as token:
                #     token.write(MyCredentials.creds.to_json())
                return flask.redirect(authorization_url)
            state = flask.session['state']
            
            # callback page
            flow = Flow.from_client_secrets_file(
                'client_secret.json',
                scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'],
                state=state)
            flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

            authorization_response = flask.request.url
            flow.fetch_token(authorization_response=authorization_response)

            # Store the credentials in the session.
            credentials = flow.credentials
            flask.session['credentials'] = {
                'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials.scopes}
                    
        except Exception as e:
            logging.error(e)
            return None
    
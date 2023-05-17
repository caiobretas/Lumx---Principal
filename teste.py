if os.path.exists('json.json'):
                creds = Credentials.from_authorized_user_file(MyCredentials.credentialToken_path, MyCredentials.SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(MyCredentials.oauth2_credentials_path, MyCredentials.SCOPES)
                    flow.redirect_uri = 'http://localhost:8080/oauth/callback'
                    authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')
                with open(MyCredentials.credentialToken_path,'w') as token:
                    token.write(creds.to_json())  
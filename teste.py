import os
from flask import Flask, redirect, request
from google_auth_oauthlib.flow import InstalledAppFlow
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

flow = InstalledAppFlow.from_client_secrets_file('credentials/credentialsGoogle/oAuth2_credentials.json', SCOPES)
flow.run_local_server()
credentials = flow.credentials
refresh_token = credentials.refresh_token
print(f'Refresh Token: {refresh_token}')


def send_email():
    # Carrega as credenciais a partir do arquivo JSON
    creds = Credentials.from_authorized_user_file('credentials/credentialsGoogle/oAuth2_credentials.json', ['https://www.googleapis.com/auth/gmail.send'])

    # Atualiza as credenciais se expirarem
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # Cria o objeto de serviço da API do Gmail
    service = build('gmail', 'v1', credentials=creds)

    # Cria a mensagem do email
    message = create_message('seu-email@gmail.com', 'destinatario@example.com', 'Assunto do email', 'Conteúdo do email')

    try:
        # Envia o email
        send_message(service, 'me', message)
        print('Email enviado com sucesso!')
    except HttpError as error:
        print(f'Erro ao enviar o email: {error}')

def create_message(sender, to, subject, message_text):
    message = {
        'from': sender,
        'to': to,
        'subject': subject,
        'message': message_text
    }
    message['raw'] = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return message

def send_message(service, user_id, message):
    service.users().messages().send(userId=user_id, body=message).execute()

send_email()

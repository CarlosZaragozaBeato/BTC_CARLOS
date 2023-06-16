import os.path
import pyautogui
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import time
import threading

def generar_token(INFO):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    flow = InstalledAppFlow.from_client_secrets_file(INFO, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(f'./token/token.json', 'w') as token:
            token.write(creds.to_json())


INFO = "./credenciales/credentials.json"
generar_token(INFO)

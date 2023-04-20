from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class AuthenticateGoogle():

    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    SAMPLE_RANGE_NAME = 'Class Data!A2:E'

    def __init__(self, spotify_obj):
        self.spotify_obj = spotify_obj

    def authenticate(self, kwargs):
        self.set_token_path()
        self.attempt_set_credentials_from_file()
        self.attempt_set_credentials_from_user()

    def set_token_path(self):
        self.token_path = os.path.join(
            self.spotify_obj.authorisation_path,
            self.spotify_obj.google_token_file_name)

    def attempt_set_credentials_from_file(self):
        if os.path.exists(self.token_path):
            self.set_credentials_from_file()
        else:
            self.credentials = None

    def set_credentials_from_file(self):
        self.credentials = Credentials.from_authorized_user_file(
            self.token_path, self.SCOPES)

    def attempt_set_credentials_from_user(self):
        if self.need_credentials_from_user():
            self.set_credentials_from_user()
            self.save_credentials()

    def need_credentials_from_user(self):
        if self.credentials is None:
            return True
        else:
            return not self.credentials.valid

    def set_credentials_from_user(self):
        if self.need_to_refresh_credentials():
            self.refresh_credentials()
        else:
            self.generate_credentials()

    def need_to_refresh_credentials(self):
        return (self.credentials
                and self.credentials.expired
                and credentials.refresh_token)

    def refresh_credentials(self):
        self.credentials.refresh(Request())

    def generate_credentials(self):
        credentials_path = self.get_credentials_path()
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_path, self.SCOPES)
        self.credentials = flow.run_local_server(port=0)

    def get_credentials_path(self):
        credentials_path = os.path.join(self.spotify_obj.authorisation_path,
                                        self.spotify_obj.google_keys_file_name)
        return credentials_path

    def save_credentials(self):
        with open(self.token_path, 'w') as token:
            token.write(self.credentials.to_json())    

    def do_something_example(self):
        try:
            service = build('sheets', 'v4', credentials=self.creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range=self.SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return

            print('Name, Major:')
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print('%s, %s' % (row[0], row[4]))
        except HttpError as err:
            print(err)

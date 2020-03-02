#!/usr/bin/env python3

from __future__ import print_function
import pickle
import os.path
import time
from record import record
from weather import get_weather
from pprint import pprint
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

DATE_FORMAT = '%m/%d/%Y %I:%M:%S'

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '13OJp3qoi3TPOiTCSRLN72mzOHivhKTg6G64glTQjlyE'
RANGE = 'Flowering!A:C'

# How the input data should be interpreted.
value_input_option = 'USER_ENTERED'

# How the input data should be inserted.
insert_data_option = 'INSERT_ROWS'

client_secrets_file = os.path.abspath('/home/pi/workspace/Hortos/client_secrets.json')


try:
    current_time = str(time.strftime(DATE_FORMAT, time.localtime()))
    # Get weather reading
    weather = get_weather()
    print("Hortos:", weather)
    
    value_range_body = {
        "values": [
            [current_time, weather['temperature'], weather['humidity']]
        ]
    }
    record(weather)    
except:
    value_range_body = {
        "values": [
            [current_time,"None","None"]
        ]
    }

def main():

    creds = None
    
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    request = service.spreadsheets().values().append(
                                                        spreadsheetId=SPREADSHEET_ID,
                                                        range=RANGE,
                                                        valueInputOption=value_input_option, 
                                                        insertDataOption=insert_data_option,
                                                        body=value_range_body
                                                    )
    
    request.execute()

if __name__ == '__main__':
    main()
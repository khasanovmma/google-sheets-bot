# from a1range import A1Range
import os.path

from google.oauth2 import service_account
from googleapiclient.discovery import build


def write_google(lname, fname, mname, phone):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials1.json')
    print(SERVICE_ACCOUNT_FILE)
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,
                                                                        scopes=SCOPES)

    service = build('sheets', 'v4', credentials=credentials)

    lst = [[lname, fname, mname, phone]]
    resource = {
        "majorDimension": "ROWS",
        "values": lst
    }
    spreadsheetId = "1xcqARLS0TwJPDz-jlyZ7fk3lq--9L6WaQpnMybWp6oQ"
    range_sheets = "Info!A:D"
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId,
        range=range_sheets,
        body=resource,
        valueInputOption="USER_ENTERED"
    ).execute()

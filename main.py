from pprint import pprint
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery

CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1ozTfck06SXNrYFPvFLlJ-yVmrji5yWJQrEJkPNUq4pc'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', http=httpAuth)


values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E10',
    majorDimension='ROWS'
).execute
pprint(values)
exit()

values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "B3:C4",
             "majorDimension": "ROWS",}
        ]

    }
)
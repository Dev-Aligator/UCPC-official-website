from oauth2client.service_account import ServiceAccountCredentials
import gspread
import numpy as np

scope =["https://spreadsheets.google.com/feeds",
    'https://www.googleapis.com/auth/spreadsheets',
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
_name = "List_of_teams"
client = gspread.authorize(creds)
spreadsheet = client.open(_name)
wks = spreadsheet.worksheet("List_teams")

data = np.array([['thanh', 'nhan']])

idx = f'B{str(len(wks.get_all_values()) + 1)}'
wks.update(idx, data.tolist())
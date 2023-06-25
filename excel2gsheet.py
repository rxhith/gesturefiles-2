import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load credentials from the downloaded JSON file
credentials = ServiceAccountCredentials.from_json_keyfile_name('credible-acre-387913-c154a768a578.json')

# Authorize the client
client = gspread.authorize(credentials)

# Open the desired Google Sheet
spreadsheet = client.open('lday')

# Select the worksheet you want to update
worksheet = spreadsheet.get_worksheet(0)  # Use the index of the worksheet (0 for the first sheet)

# Read data from the Excel file using pandas
data = pd.read_excel('dynamic csv.xlsx')

# Write data to the worksheet
worksheet.update([data.columns.values.tolist()] + data.values.tolist())

print("Data has been successfully saved to Google Sheets.")

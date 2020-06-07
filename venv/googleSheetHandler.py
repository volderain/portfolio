import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('tactical-investing-3b6ab4a43a22.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("portfolio").sheet1

# Get one row's values
def getRowValues(row):
    return sheet.row_values(row)

# Get one column's values
def getColumnValues(col):
    return sheet.col_values(col)

# Get the value of a specific cell
def getCellValue(row, column):
    return sheet.cell(row, column).value

#update one cell with a value
def updateCellValue(col, row, cellValue):
    sheet.update_cell(col, row, cellValue)


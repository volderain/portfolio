import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('tactical-investing-3b6ab4a43a22.json', scope)

client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("portfolio").sheet1

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)

#print(sheet.row_values(1))

#print(sheet.col_values(1))

#print(sheet.cell(1, 1).value)

#sheet.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")

#print(sheet.cell(1, 1).value)

#sheet.update_cell(1, 1, "Hello")

def getRowValues(row):
    return sheet.row_values(row)

def getColumnValues(col):
    return sheet.col_values(col)

def getCellValue(row, column):
    return sheet.cell(row, column).value

def updateSheetWithTickerInfo(ticker, time, price):
    row = [ticker, time, price]
    index = 3
    sheet.update_cell(index, 1, ticker)
    sheet.update_cell(index, 2, time)
    sheet.update_cell(index, 3, price)

def updateSheetWithTickerInfo(col, row, cellValue):
    sheet.update_cell(col, row, cellValue)


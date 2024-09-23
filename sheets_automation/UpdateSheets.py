import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv


class UpdateSheets:
    @staticmethod
    def update_google_sheets(data_processed_event):

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'data-fetch-418617-0859e9e0218e.json', scope)

        try:

            client = gspread.authorize(creds)

            spreadsheet_title = 'teste'

            spreadsheet = client.open(spreadsheet_title)

            worksheet = spreadsheet.sheet1

            with open('data/Midia Kit Artistas_teste.csv', 'r') as file:
                reader = csv.reader(file)
                new_data = list(reader)

            cell_range = 'D5:AD42'

            values_to_update = [row[3:30] for row in
                                new_data[4:42]]

            worksheet.update(cell_range, values_to_update)

            print("Table updated successfully.")

        except gspread.exceptions.SpreadsheetNotFound:
            print(f"Spreadsheet '{spreadsheet_title}' not found.")

        except Exception as e:
            print(f"An error occurred: {e}")

        data_processed_event.set()

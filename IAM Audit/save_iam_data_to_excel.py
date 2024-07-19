import gspread
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_google_sheets(sheet_name, df):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your-service-account-file.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open(sheet_name).sheet1

    # Clear existing data
    sheet.clear()

    # Update sheet with new data
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

# upload_to_google_sheets('IAM Data', iam_df)
# upload_to_google_sheets('High Risk Permissions', high_risk_df)
# upload_to_google_sheets('Groups Permissions Count', groups_permissions_df)

import gspread
import json, os
from google.oauth2.service_account import Credentials

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

client = gspread.authorize(creds)
sheet = client.open("Job Tracker").sheet1

sheet.append_row([
    "IT Support",
    "Test Company",
    "Jakarta",
    "Test",
    "https://example.com",
    "Today",
    90,
    "No"
])

print("✅ Google Sheet write success")

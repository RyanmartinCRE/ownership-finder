import os, datetime as dt, gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SHEET_ID = os.getenv("GSHEET_ID")

def _sheet():
    creds = Credentials.from_service_account_file(os.getenv("GSHEET_SA_JSON"), scopes=SCOPES)
    return gspread.authorize(creds).open_by_key(SHEET_ID).sheet1

def run(rows: list[dict]) -> dict:
    sh = _sheet()
    for r in rows:
        r["Timestamp"] = dt.datetime.utcnow().isoformat()
        sh.append_row(list(r.values()), value_input_option="USER_ENTERED")
    return {"status": f"✅ {len(rows)} rows written"}

import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(key_path, scope)
client = gspread.authorize(creds)


df = pd.read_csv("50_Startups.csv")

df_filtered = df[['State', 'Profit', 'R&D Spend']]

pivot_table = pd.pivot_table(
    df_filtered,
    index='State',
    values=['Profit', 'R&D Spend'],
    aggfunc='sum',
    fill_value=0
)

pivot_table_reset = pivot_table.reset_index()
sheet = client.open("Stakeholder Dashboard").sheet1
set_with_dataframe(sheet, pivot_table_reset)
import streamlit as st
from streamlit_autorefresh import st_autorefresh
from gsheetsdb import connect
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def app(self):
    # st.header("Database")
    # Create a connection object.
    conn = connect()

    # Perform SQL query on the Google Sheet.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    # @st.cache(ttl=100)
    # parking_spots_db = sheet.get_all_records()
    # parking_spaces_master = pd.DataFrame.from_dict(parking_spots_db)
    # st_autorefresh(interval=5000, limit=1000, key="updatetable")

    def run_query(query):
        rows = conn.execute(query, headers=1)
        return rows

    sheet_url = "https://docs.google.com/spreadsheets/d/1nVvwzUo90R4xeJ--hCQXw-5PbXJkTtb449D6d4tW8p0/edit?usp=sharing"
    rows = run_query(f'SELECT * FROM "{sheet_url}"')

    self.parking_spaces_master = pd.DataFrame(rows)
    # st.table(self.parking_spaces_master)

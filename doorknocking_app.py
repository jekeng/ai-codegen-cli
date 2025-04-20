# # -*- coding: utf-8 -*-
# """
# Created on Tue Mar 25 09:10:42 2025

# @author: HP USER
# """

# import pandas as pd
# import numpy as np
# import time


print("Welcome to the Door Knocking App")

outcome_mapping = {
    1: "Knock",
    2: "Contact",
    3: "Not Interested",
    4: "Lead"
}

# Dictionary to store the count of each outcome
stats = {
    "Knock": 0,
    "Contact": 0,
    "Not Interested": 0,
    "Lead": 0
}

import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Works on local computer but for streamlit cloud we will use the link in the bottom
# creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\HP USER\Downloads\door-knocking-app-0eed563aaa36.json", scope)


import json
from oauth2client.service_account import ServiceAccountCredentials

# Access the secret stored in Streamlit Cloud
creds_dict = {
    "type": st.secrets["gcp"]["type"],
    "project_id": st.secrets["gcp"]["project_id"],
    "private_key_id": st.secrets["gcp"]["private_key_id"],
    "private_key": st.secrets["gcp"]["private_key"],
    "client_email": st.secrets["gcp"]["client_email"],
    "client_id": st.secrets["gcp"]["client_id"],
    "auth_uri": st.secrets["gcp"]["auth_uri"],
    "token_uri": st.secrets["gcp"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["gcp"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["gcp"]["client_x509_cert_url"],
    "universe_domain": st.secrets["gcp"]["universe_domain"]
}

# Load the credentials from the dict and use them
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)


client = gspread.authorize(creds)
sheet = client.open("Door Knocking Stats").sheet1

# Initialize session state
if "stats" not in st.session_state:
    st.session_state.stats = {"Knock": 0, "Contact": 0, "Not Interested": 0, "Lead": 0}

# Display header
st.title("Door Knocking Tracker")

outcome = st.selectbox("Select Outcome:", ["Knock", "Not Interested", "Lead"])

# Record Outcome
if st.button("Record Outcome"):
    st.session_state.stats["Knock"] += 1

    if outcome == "Not Interested":
        st.session_state.stats["Contact"] += 1
        st.session_state.stats["Not Interested"] += 1
    elif outcome == "Lead":
        st.session_state.stats["Contact"] += 1
        st.session_state.stats["Lead"] += 1

    st.success(f"Recorded: {outcome}")

    # Update Google Sheets Immediately
try:
    today_date = datetime.today().strftime('%Y-%m-%d')
    new_entry = [today_date, st.session_state.stats["Knock"], st.session_state.stats["Contact"],
                 st.session_state.stats["Not Interested"], st.session_state.stats["Lead"]]

    all_rows = sheet.get_all_values()
    
    # Search for today's date in column A
    row_index = None
    for idx, row in enumerate(all_rows):
        if row and row[0] == today_date:
            row_index = idx + 1  # +1 because gspread uses 1-based indexing
            break

    if row_index:  # Update existing row
        cell_range = f"A{row_index}:E{row_index}"
        sheet.update(cell_range, [new_entry])
        st.info("Today's stats updated in Google Sheets.")
    else:  # Append as new row
        sheet.append_row(new_entry)
        st.info("New day added to Google Sheets.")

except Exception as e:
    st.error(f"Failed to update Google Sheets: {e}")
    
# Display live stats
st.subheader("Current Stats")
for key, value in st.session_state.stats.items():
    st.write(f"{key}: {value}")

# End session button
if st.button("End Session"):
    st.subheader("Final Stats of the Session:")

    # Display final stats
    for key, value in st.session_state.stats.items():
        st.write(f"{key}: {value}")

    # Final Save to Google Sheets
    try:
        today_date = datetime.today().strftime('%Y-%m-%d')
        new_entry = [today_date, st.session_state.stats["Knock"], st.session_state.stats["Contact"],
                      st.session_state.stats["Not Interested"], st.session_state.stats["Lead"]]
        sheet.update('A2:E2', [new_entry])
        st.success("Final session data saved to Google Sheets.")
    except Exception as e:
        st.error(f"Final save failed: {e}")

    st.warning("Session has ended. Close the app manually if needed.")
    st.stop()



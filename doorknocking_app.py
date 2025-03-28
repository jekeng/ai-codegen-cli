# # -*- coding: utf-8 -*-
# """
# Created on Tue Mar 25 09:10:42 2025

# @author: HP USER
# """

# import pandas as pd
# import numpy as np
# import time

# street_name = 'Alderson'
# city_name = 'Hamilton'
# postal_code = 'L2C 2U8'



# def generate_addresses(street_name, city_name, postal_code, start, end, interval):
#     house_numbers = list(range(start, end + 1, interval))
#     addresses = [f"{num} {street_name}, {city_name}, {postal_code}" for num in house_numbers]
#     return addresses

# # Example usage
# street_name = 'Alderson'
# city_name = 'Hamilton'
# postal_code = 'L2C 2U8'

# addresses = generate_addresses(street_name, city_name, postal_code, 1, 20, 2)
# print(addresses)

# generate_addresses('north shore boulevard', 'burlington', 'L2C 2U8', 1, 65, 4)



# knocks = 0
# contact = 0
# not_interested = 0
# Leads = 0


# outcome_mapping = {
#     1: "Knock",
#     2: "Contact",
#     3: "Not Interested",
#     4: "Lead"
# }











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











# # We are commenting this because Streamlit needs these to be installed in the terminal not spyder
# # pip install gspread pandas oauth2client


# import gspread
# import pandas as pd
# from oauth2client.service_account import ServiceAccountCredentials

# # Authenticate with Google Sheets
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:/Users/HP USER/Downloads/door-knocking-app-0eed563aaa36.json", scope)
# client = gspread.authorize(creds)

# # Open Google Sheet (Replace with your actual sheet name)
# sheet = client.open("Door Knocking Stats").sheet1  





        
# sheet.update('A1', [["Date of Knocking", "Knock", "Contact", "Not Interested", "Lead"]])  # Headers
# sheet.update('A2', [[stats["Knock"], stats["Contact"], stats["Not Interested"], stats["Lead"]]])

# sheet.update(values=[[stats["Knock"], stats["Contact"], stats["Not Interested"], stats["Lead"]]], range_name='A2')

# from datetime import datetime

# # Get today's date
# today_date = datetime.today().strftime('%Y-%m-%d')

# while True:
#     try:
#         user_input = int(input("Enter outcome (1: Knock, 3: Not Interested, 4: Lead, 5: Exit): ").strip())

#         if user_input == 5:
#             print("\nFinal Stats:")
#             for key, value in stats.items():
#                 print(f"{key}: {value}")
#             print("Exiting the app. Goodbye!")
#             break  # Exit the loop

#         if user_input in outcome_mapping:
#             selected_outcome = outcome_mapping[user_input]

#             # Auto-increment logic
#             if user_input == 3:  # Not Interested (includes Knock + Contact)
#                 stats["Knock"] += 1
#                 stats["Contact"] += 1
#                 stats["Not Interested"] += 1
#             elif user_input == 4:  # Lead (includes Knock + Contact + Lead)
#                 stats["Knock"] += 1
#                 stats["Contact"] += 1
#                 stats["Lead"] += 1
#             else:  # Knock only
#                 stats[selected_outcome] += 1

#             # ✅ Update Google Sheet after every entry
#             sheet.update(values=[[stats["Knock"], stats["Contact"], stats["Not Interested"], stats["Lead"]]], range_name='A2')

#             print(f"Recorded: {selected_outcome}")

#             # Print live stats
#             print("\nCurrent Stats:")
#             for key, value in stats.items():
#                 print(f"{key}: {value}")
#             print("-" * 30)

#         else:
#             print("Invalid entry. Please enter a number between 1 and 5.")

#     except ValueError:
#         print("Invalid input. Please enter a number.")
        
# # After loop ends, record the day's stats
# new_entry = [today_date, stats["Knock"], stats["Contact"], stats["Not Interested"], stats["Lead"]]
# sheet.append_row(new_entry)  # ✅ Only runs once, after knocking is done


# #NEW VERSION THAT EXCLUDES CURRENT STATS, removed it because google colab script was ugly
# while True:
#     try:
#         user_input = int(input("Enter outcome (1: Knock, 3: Not Interested, 4: Lead, 5: Exit): ").strip())

#         if user_input == 5:
#             print("\nFinal Stats:")
#             for key, value in stats.items():
#                 print(f"{key}: {value}")
#             print("Exiting the app. Goodbye!")
#             break  # Exit the loop

#         if user_input in outcome_mapping:
#             selected_outcome = outcome_mapping[user_input]

#             # Auto-increment logic
#             if user_input == 3:  # Not Interested (includes Knock + Contact)
#                 stats["Knock"] += 1
#                 stats["Contact"] += 1  # Fixed incorrect += 11
#                 stats["Not Interested"] += 1
#             elif user_input == 4:  # Lead (includes Knock + Contact + Lead)
#                 stats["Knock"] += 1
#                 stats["Contact"] += 1
#                 stats["Lead"] += 1
#             else:  # Knock only
#                 stats[selected_outcome] += 1

#             # ✅ Update Google Sheet after every entry with the date included
#             sheet.update(values=[[today_date, stats["Knock"], stats["Contact"], stats["Not Interested"], stats["Lead"]]], range_name='A2')

          

#         else:
#             print("Invalid entry. Please enter a number between 1,3,4 or 5.")

#     except ValueError:
#         print("Invalid input. Please enter a number.")

# # After loop ends, record the day's stats
# new_entry = [today_date, stats["Knock"], stats["Contact"], stats["Not Interested"], stats["Lead"]]
# sheet.append_row(new_entry)  # ✅ Only runs once, after knocking is done

# #Reset the stats to zero for new entry3
# stats["Knock"] = 0
# stats["Contact"] = 0
# stats["Not Interested"] = 0
# stats["Lead"] = 0


# #Installing Streamlit for better removing pip install because it messes with the anaconda prompt        
# # pip install streamlit

# # streamlit doorknocking app.py

# streamlit run doorknocking app.py


import streamlit as st
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Works on local computer but for streamlit cloud we will use the link in the bottom
# creds = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\HP USER\Downloads\door-knocking-app-0eed563aaa36.json", scope)

client = gspread.authorize(creds)
sheet = client.open("Door Knocking Stats").sheet1

# Initialize session state
if "stats" not in st.session_state:
    st.session_state.stats = {"Knock": 0, "Contact": 0, "Not Interested": 0, "Lead": 0}

# Display header
st.title("Door Knocking Tracker")





# # User input (buttons instead of while loop)
# outcome = st.selectbox("Select Outcome:", ["Knock", "Not Interested", "Lead"])
# if st.button("Record Outcome"):
#     if outcome == "Knock":
#         st.session_state.stats["Knock"] += 1
#     elif outcome == "Not Interested":
#         st.session_state.stats["Knock"] += 1
#         st.session_state.stats["Contact"] += 1
#         st.session_state.stats["Not Interested"] += 1
#     elif outcome == "Lead":
#         st.session_state.stats["Knock"] += 1
#         st.session_state.stats["Contact"] += 1
#         st.session_state.stats["Lead"] += 1

#     # Update Google Sheet
#     today_date = datetime.today().strftime('%Y-%m-%d')
#     new_entry = [today_date, st.session_state.stats["Knock"], st.session_state.stats["Contact"], 
#                  st.session_state.stats["Not Interested"], st.session_state.stats["Lead"]]
#     sheet.append_row(new_entry)
    
#     st.success(f"Recorded: {outcome}")

# # Display live stats
# st.subheader("Current Stats")
# for key, value in st.session_state.stats.items():
#     st.write(f"{key}: {value}")
    

outcome = st.selectbox("Select Outcome:", ["Knock", "Not Interested", "Lead"])
if st.button("Record Outcome"):
    if outcome == "Knock":
        st.session_state.stats["Knock"] += 1
    elif outcome == "Not Interested":
        st.session_state.stats["Knock"] += 1
        st.session_state.stats["Contact"] += 1
        st.session_state.stats["Not Interested"] += 1
    elif outcome == "Lead":
        st.session_state.stats["Knock"] += 1
        st.session_state.stats["Contact"] += 1
        st.session_state.stats["Lead"] += 1

    st.success(f"Recorded: {outcome}")

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

    # Append final stats to Google Sheet
    today_date = datetime.today().strftime('%Y-%m-%d')
    new_entry = [today_date, st.session_state.stats["Knock"], st.session_state.stats["Contact"], 
                 st.session_state.stats["Not Interested"], st.session_state.stats["Lead"]]
    sheet.append_row(new_entry)

    st.success("Session data saved to Google Sheets.")
    st.warning("Session has ended. Close the app manually if needed.")
    st.stop()  # Stops further execution



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


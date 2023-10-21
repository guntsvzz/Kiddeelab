# python3 -m streamlit run immigration-bureau-alert.py

import streamlit as st
import pandas as pd

# Function to read traveler data from the text file
def read_traveler_data(file_path):
    data = pd.read_csv(file_path, sep=';', header=None, names=["Name", "Surname", "Passport Number", "Date of Birth"])
    return data

# Function to filter traveler data by Name and Last Name
def filter_traveler_data(data, name, last_name):
    filtered_data = data[(data["Name"] == name) & (data["Surname"] == last_name)]
    return filtered_data

# Streamlit UI
st.title("Immigration Bureau")
# Title and description
page = st.selectbox("Select a page", ["User Information Form", "View Data"])

if page == "User Information Form":
    # Text Input for Name and Last Name
    name = st.text_input("Enter Name")
    last_name = st.text_input("Enter Last Name")

    # Button to submit
    if st.button("Submit"):
        if name and last_name:
            # Read traveler data from the text file
            traveler_data = read_traveler_data("traveler_data.txt")

            # Filter data by Name and Last Name
            filtered_data = filter_traveler_data(traveler_data, name, last_name)

            # Display the filtered data as a table
            if not filtered_data.empty:
                st.write("Traveler Information:")
                st.dataframe(filtered_data, use_container_width=True)
            else:
                st.write("No traveler information found for the provided name and last name.")

    # Provide instructions
    st.write("Please enter the Name and Last Name to retrieve traveler information.")

elif page == "View Data":
    st.title("View Data")
    st.write("Here is the content of the text file:")
    
    with open('traveler_data.txt', mode='r') as file:
        data = file.read()
    
    # Display data in a table
    data_list = [line.split(';') for line in data.split('\n') if line]
    df = pd.DataFrame(data_list, columns=["Name", "Surname", "Passport Number", "Date of Birth"])
    # Skip the first row, which is the header
    st.dataframe(df.iloc[1:], use_container_width=True)
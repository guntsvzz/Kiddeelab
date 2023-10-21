'''
#import library 
pip install streamlit
pip install pandas 

# Running
python -m streamlit run your_script.py

# is equivalent to:
streamlit run your_script.py

# python3 -m streamlit run 6-streamlit-website.py
'''

import streamlit as st
import pandas as pd

def add_information(name, gender, age):
    with open('./file/streamlit-text.txt', mode='a') as file:
        file.write(f"{name};{gender};{age}\n")

# Title and description
page = st.selectbox("Select a page", ["User Information Form", "View Data"])

if page == "User Information Form":
    st.title("User Information Form")
    st.write("Please enter your information below:")
    
    # User inputs
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary"])
    age = st.slider("Age", 18, 30, 18, 1)

    # Display user information
    st.write("You entered the following information:")
    st.write(f"Name: {name}")
    st.write(f"Gender: {gender}")
    st.write(f"Age: {age}")

    # Additional action
    if st.button("Submit"):
        st.write("You have submitted the form!")
        add_information(name, gender, age)

    # Reset button
    if st.button("Reset"):
        st.text_input("Name")
        st.selectbox("Gender", ["Male", "Female", "Non-binary"])
        st.slider("Age", 18, 30, 18, 1)

elif page == "View Data":
    st.title("View Data")
    st.write("Here is the content of the text file:")
    
    with open('./file/streamlit-text.txt', mode='r') as file:
        data = file.read()
    
    # Display data in a table
    data_list = [line.split(';') for line in data.split('\n') if line]
    df = pd.DataFrame(data_list, columns=["Name", "Gender", "Age"])
    # Skip the first row, which is the header
    st.dataframe(df.iloc[1:], use_container_width=True)
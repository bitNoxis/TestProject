import streamlit as st
import pandas as pd
from registration_page import registration_page
from helpers import connect_to_collection

# set up the page
st.set_page_config(page_title="App with authentication",
                   page_icon="🔎")

# setup counter, so we only see login page once
if 'count' not in st.session_state:
    st.session_state.count = 0

# also set up a credential check
if 'credentials_check' not in st.session_state:
    st.session_state.credentials_check = False

# create a placeholder variable, so I can delete the form widget after using it
placeholder = st.empty()


def login_page():
    with placeholder.form("Login"):
        st.markdown(f'<p style="font-size: 20px; color:grey">Hello! Please enter your log in info.'
                    f'<br>If this is your first time on my app then please click on the Register Button.</p>',
                    unsafe_allow_html=True)
        user_name = st.text_input("Username", placeholder="Please enter your user name")
        password = st.text_input("Password", placeholder="Please enter your password", type="password")
        login_button = st.form_submit_button("Login")
        register_button = st.form_submit_button("Register")

    if login_button:
        # Connect to MongoDB
        db_name = 'Test'
        collection_name = 'users'
        collection = connect_to_collection(db_name, collection_name)

        # Normalize input
        user_name = user_name.strip().lower()
        password = password.strip()

        # Debug: Print user input
        st.write(f"Input username: '{user_name}'")
        st.write(f"Input password: '{password}'")

        # Fetch record
        user_record = collection.find_one({'username': {'$regex': f'^{user_name}$', '$options': 'i'}})

        if user_record:
            st.write(user_record)  # Debug: Print fetched record
            registered_password = user_record['password']
            if password == registered_password:
                st.session_state.credentials_check = True
            else:
                st.error("The username/password is not correct")
        else:
            st.error("Please provide correct user name or click on register as new user")

    if register_button:
        st.session_state.count = 1
        placeholder.empty()


if st.session_state.count == 0:
    login_page()

if st.session_state.count == 1:
    registration_page()

if st.session_state.credentials_check:
    placeholder.empty()  # clear everything
    st.title(f"Welcome Back!")
    st.image(
        "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGpubGNsZnI5cXJicjNpcXBkNGFzNWFjNW1rdHJ4ZnJmbWpkeDhicCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9dg/NTsD5QdhUOrEyU3TGC/giphy.gif")

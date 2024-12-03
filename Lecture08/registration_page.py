import streamlit as st
import datetime
import pandas as pd
from helpers import connect_to_collection


def registration_page():
    placeholder = st.empty()

    with placeholder.form("registration"):
        st.subheader("REGISTER USER")
        username = st.text_input("User Name*")
        password = st.text_input("Password*", type="password")
        repeat_password = st.text_input("Repeat Password*", type="password")
        name = st.text_input("Enter Name")
        age = st.number_input("Enter Age", min_value=18, step=1)
        pet = st.text_input("Enter Pet")
        submit_button = st.form_submit_button("Register")
        back_to_login_button = st.form_submit_button("Back to Login")

    if back_to_login_button:
        # Navigate back to login
        st.session_state.count = 0
        placeholder.empty()

    if submit_button:
        db_name = 'Test'
        collection_name = 'users'
        collection = connect_to_collection(db_name, collection_name)

        # Read the data from the collection and identify user names
        user_data = pd.DataFrame(list(collection.find()))
        usernames = list(user_data.username)

        if len(username) < 1 and len(password) < 1:
            st.error("ENTER USERNAME AND PASSWORD", icon="⚠️")
        elif len(username) < 1:
            st.error("ENTER USERNAME", icon="⚠️")
        elif len(password) < 1:
            st.error("ENTER PASSWORD", icon="⚠️")
        elif password != repeat_password:
            st.warning("PASSWORDS DON'T MATCH", icon="⚠️")
        elif username in usernames:
            st.warning("USERNAME ALREADY EXISTS", icon="🔥")
        else:
            # Create a document with the data we want to write to this collection
            document = {
                "username": username,
                "password": password,
                "name": name,
                "age": age,
                "pet": pet,
                "created_at": datetime.datetime.now()
            }

            # Write this document to the collection
            collection.insert_one(document)

            # Clear everything and set credential check flag to True
            placeholder.empty()
            st.title("Welcome New User")

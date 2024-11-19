import streamlit as st

st.title("Deleting Widget")

def show_snow():
    st.snow()

# Corrected placeholder usage
placeholder = st.empty()

# Pass the function reference without calling it (remove the `()`)
button = placeholder.button("Click me to delete", on_click=show_snow)

# Clear the placeholder if the button is clicked
if button:
    placeholder.empty()



import time
import segno
import streamlit as st

st.set_page_config(page_title="QR Code Generator", page_icon="🥶")

# st.image("./images/test.jpg")

st.title("QR Code Generator")
colour = st.color_picker("Pick A Color", "#00f900")
url = st.text_input("Enter the data you would like to encode here:")

# Add a button to trigger QR code generation
generate_button = st.button("Generate QR Code")


def generate_qrcode(url, colour):
    qrcode = segno.make_qr(url)
    qrcode.to_pil(scale=10, dark=colour).save("images/qrcode.png")


# Check if the button was clicked
if generate_button:
    if not url:
        st.warning("Please enter the data you would like to encode.")
    elif not colour:
        st.warning("Please pick a color for the QR code.")
    else:
        # create a spinner
        with st.spinner("Generating QR Code..."):
            time.sleep(3)
        # generate qrcode
        generate_qrcode(url, colour)
        # place qrcode
       # st.image("images/qrcode.png", caption="QR Code")

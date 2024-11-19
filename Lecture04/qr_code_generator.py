import time
import segno
from io import BytesIO
import streamlit as st

st.set_page_config(page_title="QR Code Generator", page_icon="🥶")

st.title("QR Code Generator")
colour = st.color_picker("Pick A Color", "#00f900")
url = st.text_input("Enter the data you would like to encode here:")

# Add a button to trigger QR code generation
generate_button = st.button("Generate QR Code")


def generate_qrcode(url, colour):
    # Generate the QR code
    qrcode = segno.make_qr(url)
    # Create an in-memory buffer to hold the QR code
    buffer = BytesIO()
    # Save the QR code as a PNG in the buffer
    qrcode.save(buffer, kind="png", scale=10, dark=colour)
    buffer.seek(0)
    return buffer


# Check if the button was clicked
if generate_button:
    if not url:
        st.warning("Please enter the data you would like to encode.")
    elif not colour:
        st.warning("Please pick a color for the QR code.")
    else:
        # Create a spinner
        with st.spinner("Generating QR Code..."):
            time.sleep(3)
        # Generate QR code and get the in-memory image
        qr_image = generate_qrcode(url, colour)
        # Display the generated QR code
        st.image(qr_image, caption="QR Code")

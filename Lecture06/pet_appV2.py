import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Fetch Unsplash API key from secrets
UNSPLASH_ACCESS_KEY = st.secrets["unsplash_api_key"]

# Function to fetch images from Unsplash
def fetch_unsplash_images(query, count=9):
    url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": count,
        "client_id": UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        st.error("Error fetching images from Unsplash")
        return []

# Streamlit App
st.title("Mood Board Generator")
st.write("Generate a mood board based on your favorite theme or keyword!")

# Input for keyword
keyword = st.text_input("Enter a theme or keyword:", "nature")

# Fetch and display images when button is clicked
if st.button("Generate Mood Board"):
    st.write(f"Fetching images for: **{keyword}**")
    images = fetch_unsplash_images(keyword)

    if images:
        # Create a grid layout to display images
        cols = st.columns(3)
        for idx, image in enumerate(images):
            with cols[idx % 3]:
                img_url = image["urls"]["small"]
                photographer = image["user"]["name"]
                photo_link = image["links"]["html"]

                # Load and display image
                response = requests.get(img_url)
                img = Image.open(BytesIO(response.content))
                st.image(img, caption=f"Photo by {photographer}", use_container_width=True)

                # Unsplash link
                st.markdown(f"[Unsplash Link]({photo_link})")

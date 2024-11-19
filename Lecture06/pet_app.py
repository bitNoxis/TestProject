import requests
import streamlit as st

st.header("Welcome to my PET App", divider='rainbow')
#st.set_page_config(page_title="My Pet App")


def get_cat_image():
    url = "https://cataas.com//cat"
    contents = requests.get(url)

    return contents.content

def get_dog_image_url():
    url = "https://random.dog/woof.json"
    contents = requests.get(url).json()
    dog_iamge_url = contents['url']

    return dog_iamge_url

c1, c2 = st.columns(2)

with c1:
    cat_button = st.button("Click here to see a CAT")
    if cat_button:
        st.image(get_cat_image())

with c2:
    dog_button = st.button("Click here to see a DOG")
    if dog_button:
        dog_iamge_url = get_dog_image_url()

        while dog_iamge_url[-4:] == ".mp4":
            dog_iamge_url = get_dog_image_url()

        st.image(dog_iamge_url, caption="Here's a Dog!", use_column_width=True)

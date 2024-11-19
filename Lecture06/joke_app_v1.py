import streamlit as st
import time
import requests

st.header("Welcome to my Joke APP")

button = st.button("Click here to laugh")
placeholder = st.empty()


def get_joke():
    url = "http://www.official-joke-api.appspot.com/random_joke"
    joke = requests.get(url).json()
    question = joke['setup']
    answer = joke['punchline']
    return question, answer


if button:
    question, answer = get_joke()

    placeholder.write(question)
    time.sleep(2)
    with st.spinner("Wait for it..."):
        for i in range(1, 101):
            time.sleep(0.02)
            placeholder.progress(i)

    placeholder.write(answer)

    # Play the local audio file
    with open("music/sound.mp3", "rb") as audio_file:
        st.audio(audio_file, format="audio/mp3")

import streamlit as st
from src.init_resources import init_resources
from src.song_utils import get_song
import re


# Don't show the setting sidebar
if "sidebar_state" not in st.session_state:
    st.session_state.sidebar_state = "collapsed"

st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)
db, chain = init_resources()

st.title("🎵🎤⭐ EmotiTuneOT 🎵🎤⭐")
st.markdown(
    """
*<small>Made with [DeepLake](https://www.deeplake.ai/) 🚀 and [LangChain](https://python.langchain.com/en/latest/index.html) 🦜⛓️</small>*

✨ Dive into an adventure where your emotions set the stage with our innovative app,
 turning your feelings into an "[Operación Triunfo](https://es.wikipedia.org/wiki/Operaci%C3%B3n_Triunfo_(Espa%C3%B1a))" performance! 🎤
  Share the rhythm of your soul, and join us on an exciting journey as we craft a musical piece inspired 
  by "Operación Triunfo" that echoes your unique essence. 🎶💫
""", unsafe_allow_html=True,
)
how_it_works = st.expander(label="How it works")

sentence = st.text_input(
    label="How are you feeling today?",
    placeholder="Give it gas!⛽🚗💨",
)
run_btn = st.button("Let my voice soar! 🎤")

with how_it_works:
    st.markdown(
        """
This project will aim to adapt the emotions that the user can express in the free text box

- User Emotion Input: The journey begins when the user shares their current emotional state via a textual input.
- Emotion Interpretation: This input is then processed by a Language Model (LLM), which interprets and translates these emotions into a specific format.
- Matching Process: The interpreted emotions are used to conduct a similarity search within a vector database, where each "Operación Triunfo" performance is represented through emotional embeddings.
- Performance Selection: The system identifies the best-matching performances and providing a list. This selection process is influenced by the popularity (field provided by spotify), favoring performances that are a closer emotional match.
- Performance Delivery: Finally, the application presents the user with an embedded player to enjoy the chosen performance. It also shares the LLM's interpretation of the emotional state that aligns with the selected performance, enhancing the user's connection to the song.
"""
    )

placeholder_emotions = st.empty()
placeholder = st.empty()


with st.sidebar:
    st.text("App settings")
    filter_threshold = st.slider(
        "Threshold used to filter out low scoring songs",
        min_value=0.0,
        max_value=1.0,
        value=0.8,
    )
    max_number_of_songs = st.slider(
        "Max number of songs we will shown",
        min_value=5,
        max_value=50,
        value=20,
        step=1,
    )

def set_song(docs, emotions):
    if sentence == "":
        return
    # take first 120 chars
    user_input = sentence

    with placeholder_emotions:
        st.markdown(f"Your emotions: `  {emotions}  `")
    with placeholder:
        iframes_html = ""
        for doc in docs:
            name = doc["name"]
            print(f"song = {name}")
            embed_url = doc["spotify_track_url"]
            embed_url = re.sub("track/", "embed/track/", embed_url)
            print(f"embed_url = {embed_url}")
            print(f"{doc['popularity']}")
            iframe_html = f"""
                <iframe
                style = "border-radius:12px"
                src = "{embed_url}"
                width = "100%"
                height = "152"
                frameBorder = "0"
                allowfullscreen = ""
                allow = "autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" </iframe>"""
            iframes_html += (iframe_html)

        st.markdown(
            f"<div style='display:flex;flex-direction:column'>{iframes_html}</div>",
            unsafe_allow_html=True,
        )

if run_btn:
    if sentence != "":
        docs, emotions = get_song(db=db,
                                  chain=chain,
                                  sentence=sentence,
                                  k=max_number_of_songs)
    set_song(docs, emotions)
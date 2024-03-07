import streamlit as st
from src.init_resources import init_resources
from src.song_utils import get_song



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
 turning your feelings into an "Operación Triunfo" performance! 🎤
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
For an "Operación Triunfo" themed application, adapting the process to match the user's emotions with performances or songs from the show would look something like this:

User Emotion Input: The journey begins when the user shares their current emotional state via a textual input.
Emotion Interpretation: This input is then processed by a Language Model (LLM), which interprets and translates these emotions into a specific format.
Matching Process: The interpreted emotions are used to conduct a similarity search within a vector database, where each "Operación Triunfo" performance is represented through emotional embeddings.
Performance Selection: The system identifies the best-matching performances, selecting one at random. This selection process is influenced by the similarity scores, favoring performances that are a closer emotional match.
Performance Delivery: Finally, the application presents the user with an embedded player to enjoy the chosen performance. It also shares the LLM's interpretation of the emotional state that aligns with the selected performance, enhancing the user's connection to the song.
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
        "Max number of songs we will retrieve from the db",
        min_value=5,
        max_value=50,
        value=20,
        step=1,
    )
    number_of_displayed_songs = st.slider(
        "Number of displayed songs", min_value=1, max_value=4, value=2, step=1
    )

def set_song(sentence):
    if sentence == "":
        return
    # take first 120 chars
    user_input = sentence
    docs, emotions = get_song(user_input, k=max_number_of_songs)
    print(docs)
    songs = []
    with placeholder_emotions:
        st.markdown(f"Your emotions: `  {emotions}  `")
    with placeholder:
        iframes_html = ""
        for doc in docs:
            name = doc.metadata["name"]
            print(f"song = {name}")
            songs.append(name)
            embed_url = doc.metadata["spotify_track_url"]
            iframes_html += (
                f'<iframe src="{embed_url}" style="border:0;height:100px"> </iframe>'
            )

        st.markdown(
            f"<div style='display:flex;flex-direction:column'>{iframes_html}</div>",
            unsafe_allow_html=True,
        )

if run_btn:
    set_song(sentence)
# 🎵🎤⭐ EmotiTuneOT 🎵🎤⭐
EmotiTuneOT is a music recommendation system based on emotions, designed to help you discover music from Operación Triunfo 2023
and other Spanish music reality shows. By analyzing your emotions, this system suggests songs that match your mood, 
providing an immersive music experience. 🎵🎉
Operación Triunfo is a Spanish TV Show focused on music.

This app has been focused on the following article [Recommendation Engine for Songs](https://www.activeloop.ai/resources/3-ways-to-build-a-recommendation-engine-for-songs-with-lang-chain/).

Made with [DeepLake](https://www.deeplake.ai/) 🚀 and [LangChain](https://python.langchain.com/en/latest/index.html) 🦜⛓

## Functionality

The application follows a sequence of steps to deliver Disney songs matching the user's emotions:

User Input: The application starts by collecting user's emotional state through a text input.
Emotion Encoding: The user-provided emotions are then fed to a Language Model (LLM). The LLM interprets and encodes these emotions.
Similarity Search: These encoded emotions are utilized to perform a similarity search within our [vector database](Deep Lake Vector Store in LangChain). This database houses Disney songs, each represented as emotional embeddings.
Song Selection: From the pool of top matching songs, the application randomly selects one. The selection is weighted, giving preference to songs with higher similarity scores.
Song Retrieval: The selected song's embedded player is displayed on the webpage for the user. Additionally, the LLM interpreted emotional state associated with the chosen song is displayed.

## Run it

Clone this repo.

Create a venv and install all the requirements.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You will need the following .env file
```bash
# Spotipy and Genius configuration for data extracting
SPOTIPY_CLIENT_ID=<SPOTIPY_CLIENT_ID>
SPOTIPY_CLIENT_SECRET=<SPOTIPY_CLIENT_SECRET>
GENIUS_TOKEN=<GENIUS_TOKEN>

# OPENAI Key
OPENAI_API_KEY=<OPENAI_API_KEY>

# Active Loop Token
ACTIVELOOP_TOKEN=<ACTIVELOOP_TOKEN>
ACTIVELOOP_ORG_ID="NachoCP"
```

To init the application run

```
streamlit run app.py
```

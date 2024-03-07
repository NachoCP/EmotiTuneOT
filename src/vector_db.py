import json

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake

from src.constants import EMBEDDING_MODEL
def create_db(json_path: str, dataset_path: str) -> DeepLake:
    with open(json_path, "r") as f:
        data_songs = json.load(f)
    plot_texts = []
    metadata_movies = []

    for data_song in data_songs:
        plot_texts.append(data_song["emotions"])
        metadata_movies.append({
            "name": data_song["name"],
            "spotify_track_url": data_song["spotify_track_url"],
            "spotify_api_track_url": data_song["spotify_api_track_url"],
            "popularity": data_song["popularity"],
            "uri": data_song["uri"],
            "release_date": data_song["release_date"]
        })
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    db = DeepLake.from_texts(
        plot_texts, embeddings, metadatas=metadata_movies, dataset_path=dataset_path
    )
    return db


def load_db(dataset_path: str, *args, **kwargs) -> DeepLake:
    db = DeepLake(dataset_path, *args, **kwargs)
    return db
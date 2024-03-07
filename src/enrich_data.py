import json
from src.llms import llm_lyrics_emotion


def get_emotions_from_lyrics():
    with open("data/ot-tracks.json") as f:
        data = json.load(f)
    chain = llm_lyrics_emotion()
    possible_emotions = set()
    for song in data:
        emotions = chain.run({"name": song["name"],
                              "lyrics": song["lyrics"],
                              "emotions_used": str(possible_emotions)})
        song["emotions"] = emotions
        emotions_list = emotions.split(", ")
    possible_emotions.update(set(emotions_list))


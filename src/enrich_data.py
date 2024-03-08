import json
from src.llms import llm_lyrics_emotion
from src.constants import TRACKS_JSON_PATH, TRACKS_EMOTIONS_JSON_PATH

def get_emotions_from_lyrics():
    with open(TRACKS_JSON_PATH, "r") as f:
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
    with open(TRACKS_EMOTIONS_JSON_PATH, "w") as f:
        json.dump(data, f)

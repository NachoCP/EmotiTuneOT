from langchain.chains import LLMChain
from langchain.vectorstores import DeepLake


def filter_scores(songs, th: float=0.8):
    return [doc for (doc, score) in songs if score > th]


def get_song(chain: LLMChain, db: DeepLake, sentence:str, k:int = 20):
    emotions = chain.run(sentence=sentence)
    songs = db.similarity_search_with_score(emotions, distance_metric="cos", k=k)
    songs_filtered = filter_scores(songs)

    return sorted(songs_filtered, key=lambda d: d["popularity"])

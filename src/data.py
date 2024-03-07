import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from lyricsgenius import Genius
import os
import re
import time
from dotenv import load_dotenv

load_dotenv()
# List containing the Operación Triunfo songs
OT_PLAYLIST = "https://open.spotify.com/playlist/37i9dQZF1DWZYJ3pS3pteL?si=4481b20beab24def"


def get_data():
    # Getting all the elements from the spotify list
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    all_tracks = []
    list_track = spotify.playlist_tracks(OT_PLAYLIST)
    while list_track["next"]:
        all_tracks.extend(list_track["items"])
        list_track = spotify.next(list_track)
    all_tracks.extend(list_track["items"])

    # Getting the lyrics from the tracks

    genius = Genius(os.environ["GENIUS_TOKEN"])
    genius.remove_section_headers = True
    records = []
    for i, item in enumerate(all_tracks):
        # Sleep time for not reaching timeout
        if i == 65:
            print("Sleeping 30 secs to avoid the timeout")
            time.sleep(30)
        song = genius.search_song(item["track"]["name"],
                                  item["track"]["artists"][0]["name"])
        if song:
            lyrics_text = song.lyrics.split("Lyrics\n")[1]
            lyrics_text = re.sub("\n", " ", lyrics_text)
            record = {"name": item["track"]["name"],
                      "spotify_track_url": item["track"]["external_urls"]["spotify"],
                      "spotify_api_track_url": item["track"]["href"],
                      "popularity": item["track"]["popularity"],
                      "uri": item["track"]["uri"],
                      "release_date": item["track"]["album"]["release_date"],
                      "lyrics": lyrics_text}
            records.append(record)
    return records

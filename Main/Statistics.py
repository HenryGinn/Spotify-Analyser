import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Statistics():

    def __init__(self, spotify_obj):
        self.spotify_obj = spotify_obj
        self.scope = "user-top-read"
        
    def do_something(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        results = sp.current_user_top_tracks()["items"]
        for i in results:
            print(i["name"])

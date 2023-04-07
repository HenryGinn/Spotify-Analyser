import os
import sys

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class Authenticate():

    def __init__(self, spotify_obj):
        self.spotify_obj = spotify_obj

    def authenticate(self):
        self.set_client_keys()
        self.do_something()

    def set_client_keys(self):
        path = os.path.join(self.spotify_obj.repository_path,
                            self.spotify_obj.spotify_keys_file_name)
        with open(path, "r") as file:
            self.get_keys_from_file(file)

    def get_keys_from_file(self, file):
        keys = self.read_keys_from_file(file)
        self.set_keys_from_file_keys(keys)

    def read_keys_from_file(self, file):
        try:
            return self.do_read_keys_from_file(file)
        except:
            self.exception_extract_keys_from_file(file)

    def do_read_keys_from_file(self, file):
        keys = [line.strip().split("=")
                    for line in file]
        return keys

    def exception_extract_keys_from_file(self, file):
        exception_message = (f"Could not extract API keys from {file.name}\n"
                             "Ensure file is of the following format:\n"
                             "SPOTIFY_CLIENT_ID=\"Your client id\"\n"
                             "SPOTIFY_CLIENT_SECRET=\"Your client secret\"")
        raise Exception(exception_message)

    def set_keys_from_file_keys(self, keys):
        try:
            self.set_keys_as_environment_variables(keys)
        except:
            raise Exception(f"Could not extract two keys from the following list:\n{keys}")

    def set_keys_as_environment_variables(self, keys):
        for key_name_value_pair in keys:
            key_name, key_value = key_name_value_pair
            os.environ[key_name] = key_value

    def do_something(self):
        spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
        name = "Coldplay"
        results = spotify.search(q='artist:' + name, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            artist = items[0]
            print(artist['name'], artist['images'][0]['url'])


import os
import sys

import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Authenticate():

    def __init__(self, spotify_obj):
        self.spotify_obj = spotify_obj
        self.load_default_settings()

    def load_default_settings(self):
        path = os.path.join(self.spotify_obj.default_settings_path,
                            f"{type(self).__name__}")
        with open(path, "r") as file:
            self.set_default_settings_from_file(file)

    def set_default_settings_from_file(self, file):
        for line in file:
            setting_name, setting_value = line.strip().split("=")
            setattr(self, setting_name, setting_value)

    def authenticate(self, kwargs):
        self.process_kwargs(kwargs)
        self.set_client_keys()
        self.set_redirect_uri()

    def process_kwargs(self, kwargs):
        self.kwargs = kwargs
        self.process_redirect_uri_kwarg()

    def process_redirect_uri_kwarg(self):
        if "redirect_uri" in self.kwargs:
            if self.kwargs["redirect_uri"] is not None:
                self.redirect_uri = self.kwargs["redirect_uri"]

    def output_authentification_kwargs(self):
        print(["redirect_uri"])

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

    def set_redirect_uri(self):
        os.environ["SPOTIPY_REDIRECT_URI"] = self.redirect_uri


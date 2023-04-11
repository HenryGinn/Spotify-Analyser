import os
import json

from Utils.PathManagement import make_folder

class Tracks():

    def __init__(self, spotify_obj):
        self.spotify_obj = spotify_obj

    def load(self):
        self.set_paths()
        if not self.is_saved():
            self.save()
        else:
            self.do_load()

    def set_paths(self):
        self.make_track_list_folder()
        self.set_file_paths()

    def make_track_list_folder(self):
        self.folder_path = os.path.join(self.spotify_obj.repository_path,
                                        "Track List")
        make_folder(self.folder_path, message=True)

    def set_file_paths(self):
        self.results_path = os.path.join(self.folder_path, "Track List")
        self.data_path = self.spotify_obj.files_obj.path

    def is_saved(self):
        return (os.path.exists(self.results_path))

    def save(self):
        self.set_tracks_dict()
        self.save_track_list()

    def set_tracks_dict(self):
        self.spotify_obj.tracks_dict = {}
        for file_name in os.listdir(self.data_path):
            file_path = os.path.join(self.data_path, file_name)
            self.add_to_track_list(file_path)

    def add_to_track_list(self, file_path):
        file_contents = self.get_file_contents_from_path(file_path)
        track_data = {track["spotify_track_uri"]: self.get_track_data(track)
                      for track in file_contents}
        self.spotify_obj.tracks_dict.update(track_data)

    def get_file_contents_from_path(self, file_path):
        with open(file_path, "r") as file:
            file_contents = json.load(file)
        return file_contents

    def get_track_data(self, track):
        track_data = {"Name": track["master_metadata_track_name"],
                      "Artist": track["master_metadata_album_artist_name"]}
        return track_data

    def save_track_list(self):
        with open(self.results_path, "w") as file:
            json.dump(self.spotify_obj.tracks_dict, file, indent=2)

    def do_load(self):
        with open(self.results_path, "r") as file:
            self.spotify_obj.tracks_dict = json.load(file)

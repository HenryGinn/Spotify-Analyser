import os
import json
import math

import numpy as np

from Utils.PathManagement import make_folder

class Files():

    data_folder_name = "my_spotify_data"
    songs_per_file = 250

    def __init__(self, spotify_obj):
        self.spotify_obj = spotify_obj

    def preprocess_files(self):
        files_unprocessed = self.check_if_files_processed()
        if files_unprocessed:
            self.do_preprocess_files()

    def check_if_files_processed(self):
        self.path = os.path.join(self.spotify_obj.repository_path, "Data")
        self.create_data_folder()
        data_folder_empty = (len(os.listdir(self.path)) == 0)
        return data_folder_empty

    def create_data_folder(self):
        if not os.path.isdir(self.path):
            make_folder(self.path)

    def do_preprocess_files(self):
        self.set_original_data_path()
        self.file_counter = 0
        self.split_files()

    def set_original_data_path(self):
        self.ensure_original_data_folder_exists()
        self.do_set_original_data_path()

    def ensure_original_data_folder_exists(self):
        directory_names = os.listdir(self.spotify_obj.repository_path)
        if self.data_folder_name not in directory_names:
            raise Exception(f"Could not find '{self.data_folder_name}' in the following location:\n"
                            f"{self.spotify_obj.repository_path}")

    def do_set_original_data_path(self):
        self.original_data_path = os.path.join(self.spotify_obj.repository_path,
                                               self.data_folder_name,
                                               "MyData")

    def split_files(self):
        for file_name in os.listdir(self.original_data_path):
            if file_name.startswith("endsong"):
                self.split_file(file_name)

    def split_file(self, file_name):
        print(f"Processing {file_name}")
        file_contents = self.get_file_contents(file_name)
        file_contents = self.remove_invalid_tracks(file_contents)
        group_indexes = self.get_group_indexes(file_contents.size)
        self.construct_new_files(file_contents, group_indexes)

    def get_file_contents(self, file_name):
        file_path = os.path.join(self.original_data_path, file_name)
        with open(file_path, "r") as file:
            file_contents = json.load(file)
        return file_contents

    def remove_invalid_tracks(self, file_contents):
        file_contents = [contents for contents in file_contents
                         if contents["master_metadata_track_name"] is not None]
        file_contents = np.array(file_contents)
        return file_contents

    def get_group_indexes(self, song_count):
        full_file_count = song_count // self.songs_per_file
        songs_in_full_files = full_file_count * self.songs_per_file
        remaining_songs = song_count - songs_in_full_files
        group_indexes = self.construct_group_indexes(songs_in_full_files, remaining_songs, full_file_count)
        return group_indexes

    def construct_group_indexes(self, songs_in_full_files, remaining_songs, full_file_count):
        group_indexes = np.arange(songs_in_full_files).reshape(full_file_count, -1)
        group_indexes += remaining_songs
        group_indexes = [np.arange(remaining_songs)] + list(group_indexes)
        return group_indexes

    def construct_new_files(self, file_contents, group_indexes):
        for indexes in group_indexes:
            self.file_counter += 1
            sub_file_contents = file_contents[indexes]
            self.save_sub_file_contents(sub_file_contents)

    def save_sub_file_contents(self, sub_file_contents):
        file_path = os.path.join(self.path, f"Streaming History {self.file_counter}")
        with open(file_path, "w") as file:
            json.dump(list(sub_file_contents), file, indent=2)
        
        
































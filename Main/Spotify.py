import os
import sys

from Main.Files import Files
from Main.Tracks import Tracks
from Authenticate.AuthenticateSpotify import AuthenticateSpotify
from Authenticate.AuthenticateGoogle import AuthenticateGoogle
from Statistics.Children.TimeListened import TimeListened
from Statistics.Children.TimeListenedFine import TimeListenedFine
from Statistics.Children.TimeOfDay import TimeOfDay
from Statistics.Children.MostListenedTracks import MostListenedTracks
from Statistics.Children.MostListenedTracksTime import MostListenedTracksTime
from Utils.PathManagement import make_folder

class Spotify():

    spotify_keys_file_name = "Spotify API Keys.json"
    google_keys_file_name = "Google Sheets API Keys.json"
    google_token_file_name = "Google Token.json"

    def __init__(self):
        self.setup_paths()
        self.create_results_folder()
        self.set_other_paths()
        self.set_authorisation_path()
        self.set_default_settings_path()

    def setup_paths(self):
        self.script_path = sys.path[0]
        self.repository_path = os.path.dirname(self.script_path)

    def create_results_folder(self):
        self.results_path = os.path.join(self.repository_path, "Results")
        make_folder(self.results_path, message=True)

    def set_other_paths(self):
        self.set_default_settings_path()
        self.set_authorisation_path()

    def set_default_settings_path(self):
        self.default_settings_path = os.path.join(self.script_path,
                                                  "Default Settings")

    def set_authorisation_path(self):
        self.authorisation_path = os.path.join(self.repository_path,
                                               "Authorisation Tokens and Keys")

    def preprocess_files(self):
        self.files_obj = Files(self)
        self.files_obj.preprocess_files()
        self.data_path = self.files_obj.path

    def set_unique_track_list(self):
        self.tracks_obj = Tracks(self)
        self.tracks_obj.load()

    def authenticate(self, **kwargs):
        self.authenticate_spotify(kwargs)
        self.authenticate_google(kwargs)

    def authenticate_spotify(self, kwargs):
        self.authenticate_spotify_obj = AuthenticateSpotify(self)
        self.authenticate_spotify_obj.authenticate(kwargs)

    def authenticate_google(self, kwargs):
        self.authenticate_google_obj = AuthenticateGoogle(self)
        self.authenticate_google_obj.authenticate(kwargs)
        self.authenticate_google_obj.do_something()

    def produce_statistics(self):
        self.set_statistics_list()
        for statistic_class in self.statistic_class_list:
            self.produce_statistic(statistic_class)

    def set_statistics_list(self):
        self.statistic_class_list = [TimeListened, TimeListenedFine,
                                     TimeOfDay, MostListenedTracks,
                                     MostListenedTracksTime]

    def produce_statistic(self, statistic_class):
        statistic_obj = statistic_class(self)
        statistic_obj.produce_statistics()

    def produce_statistic_last(self):
        self.set_statistics_list()
        statistic_class = self.statistic_class_list[-1]
        self.produce_statistic(statistic_class)

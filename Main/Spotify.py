import os
import sys

from Main.Authenticate import Authenticate
from Main.Files import Files
from Statistics.Children.TimeListened import TimeListened
from Statistics.Children.TimeListenedFine import TimeListenedFine
from Utils.PathManagement import make_folder

class Spotify():

    spotify_keys_file_name = "Spotify API Keys"

    def __init__(self):
        self.create_results_folder()
        self.set_default_settings_path()

    def create_results_folder(self):
        self.script_path = sys.path[0]
        self.repository_path = os.path.dirname(self.script_path)
        self.results_path = os.path.join(self.repository_path, "Results")
        make_folder(self.results_path, message=True)

    def set_default_settings_path(self):
        self.default_settings_path = os.path.join(self.script_path,
                                                  "Default Settings")

    def preprocess_files(self):
        self.files_obj = Files(self)
        self.files_obj.preprocess_files()
        self.data_path = self.files_obj.path

    def authenticate(self, **kwargs):
        self.authenticate_obj = Authenticate(self)
        self.authenticate_obj.authenticate(kwargs)

    def produce_statistics(self):
        self.set_statistics_list()
        for statistic_class in self.statistic_class_list:
            statistic_obj = statistic_class(self)
            statistic_obj.produce_statistics()

    def set_statistics_list(self):
        self.statistic_class_list = [TimeListened, TimeListenedFine]

import os
import sys

from Main.Authenticate import Authenticate
from Main.Statistics import Statistics
from Main.Files import Files
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

    def authenticate(self, **kwargs):
        self.authenticate_obj = Authenticate(self)
        self.authenticate_obj.authenticate(kwargs)

    def produce_statistics(self):
        self.statistics_obj = Statistics(self)
        self.statistics_obj.do_something()

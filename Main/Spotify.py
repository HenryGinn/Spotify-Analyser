import os
import sys

from Main.Authenticate import Authenticate
from Utils.PathManagement import make_folder

class Spotify():

    spotify_keys_file_name = "Spotify API Keys"

    def __init__(self, user_id, name=None):
        self.user_id = user_id
        self.set_name(name)
        self.create_results_folder()

    def set_name(self, name):
        self.name = name
        if name is None:
            self.name = self.user_id

    def create_results_folder(self):
        script_path = sys.path[0]
        self.repository_path = os.path.dirname(script_path)
        self.create_parent_results_folder()
        self.create_user_results_folder()

    def create_parent_results_folder(self):
        self.parent_results_path = os.path.join(self.repository_path, "Results")
        make_folder(self.parent_results_path, message=True)

    def create_user_results_folder(self):
        self.user_results_path = os.path.join(self.parent_results_path, self.name)
        make_folder(self.user_results_path, message=True)

    def authenticate(self):
        self.authenticate_obj = Authenticate(self)
        self.authenticate_obj.authenticate()

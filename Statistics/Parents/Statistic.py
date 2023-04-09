import os
import json

from Utils.PathManagement import make_folder

class Statistic():

    plot_format = "pdf"
    text_output_gap = 2
    units = ""

    def __init__(self, spotify_obj):
        self.spotify_obj = spotify_obj

    def produce_statistics(self):
        self.set_paths()
        self.iterate_through_files()
        self.post_process_results()
        self.output_results()

    def set_paths(self):
        self.set_statistic_name()
        self.parent_results_path = os.path.join(self.spotify_obj.results_path,
                                                self.name)
        make_folder(self.parent_results_path)

    def set_statistic_name(self):
        if not hasattr(self, "name"):
            self.name = type(self).__name__
            print(f"Warning: statistic class '{self.name}' has no name assigned")

    def iterate_through_files(self):
        for file_name in os.listdir(self.spotify_obj.data_path):
            file_path = os.path.join(self.spotify_obj.data_path, file_name)
            self.load_file_contents_from_path(file_path)

    def load_file_contents_from_path(self, file_path):
        with open(file_path, "r") as file:
            file_contents = json.load(file)
        self.process_file_contents(file_contents)

    def process_file_contents(self, file_contents):
        for track in file_contents:
            if self.track_valid(track):
                self.process_track(track)

    def track_valid(self, track):
        not_skipped = (not track["skipped"])
        not_unknown = (track["master_metadata_track_name"] != None)
        valid = not_skipped and not_unknown
        return valid

    def post_process_results(self):
        pass

    def output_results(self):
        self.output_results_text()
        self.output_results_plot()

    def output_results_text(self):
        if hasattr(self, "save_results_to_file"):
            self.set_results_path_text()
            with open(self.results_path_text, "w") as file:
                self.save_results_to_file(file)

    def set_results_path_text(self):
        self.results_path_text = os.path.join(self.parent_results_path,
                                              f"{self.name}.txt")

    def output_results_plot(self):
        if hasattr(self, "plot_results"):
            self.set_results_path_plot()
            self.plot_results()

    def set_results_path_plot(self):
        self.results_path_plot = os.path.join(self.parent_results_path,
                                              f"{self.name}.{self.plot_format}")

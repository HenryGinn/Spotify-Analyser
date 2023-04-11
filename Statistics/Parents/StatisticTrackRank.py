from Statistics.Parents.Statistic import Statistic
from Utils.DataProcessing import get_percentages
from Utils.Strings import save_file_contents_to_file

class StatisticTrackRank(Statistic):

    def __init__(self, spotify_obj):
        Statistic.__init__(self, spotify_obj)
        self.set_column_name()
        self.initialise_results_dict()

    def set_column_name(self):
        if not hasattr(self, "column_name"):
            self.column_name = self.name

    def initialise_results_dict(self):
        tracks = self.spotify_obj.tracks_dict.values()
        self.results_dict = {track["Name"]: 0 for track in tracks}

    def shorten_names(self):
        self.results_dict = {key[:60]: value for key, value in self.results_dict.items()}

    def sort_results(self):
        self.results = sorted(self.results_dict.items(),
                              key=lambda item: item[1], reverse=True)

    def save_results_to_file(self, file):
        names, values = zip(*self.results)
        percentages = get_percentages(values, self.total, decimal_places=4)
        file_contents = {"Names": names,
                         f"{self.column_name}{self.units}": values,
                         "Percentages": percentages}
        save_file_contents_to_file(file_contents, file)

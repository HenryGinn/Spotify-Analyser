from Statistics.Parents.Statistic import Statistic
from Utils.DataProcessing import get_percentages
from Utils.Strings import save_file_contents_to_file

class StatisticTrackRank(Statistic):

    def __init__(self, spotify_obj):
        Statistic.__init__(self, spotify_obj)
        self.initialise_results_dict()

    def initialise_results_dict(self):
        tracks = self.spotify_obj.tracks_dict.values()
        self.results_dict = {track["Name"]: 0 for track in tracks}

    def sort_results(self):
        self.results = sorted(self.results_dict.items(),
                              key=lambda item: item[1], reverse=True)

    def save_results_to_file(self, file):
        names, values = zip(*self.results)
        percentages = get_percentages(values, self.total)
        file_contents = {"Names": names,
                         "Times Listened": values,
                         "Percentages": percentages}
        save_file_contents_to_file(file_contents, file)

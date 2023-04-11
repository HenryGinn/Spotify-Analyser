from Statistics.Parents.StatisticTrackRank import StatisticTrackRank
from Utils.Strings import save_file_contents_to_file

class MostListenedTracksTime(StatisticTrackRank):

    name = "Most Listened Tracks Time"
    column_name = "Time Listened"
    units = " (minutes)"
    
    def process_track(self, track):
        name = track["master_metadata_track_name"]
        time = track["ms_played"]
        self.results_dict[name] += time

    def post_process_results(self):
        self.remove_rare_songs()
        self.shorten_names()
        self.convert_to_minutes()
        self.total = sum(list(self.results_dict.values()))
        self.sort_results()

    def remove_rare_songs(self):
        self.results_dict = {key: value for key, value in self.results_dict.items()
                             if value >= 10000}

    def convert_to_minutes(self):
        for key, value in self.results_dict.items():
            minutes = round(value / (1000 * 60), 1)
            self.results_dict[key] = minutes

from Statistics.Parents.StatisticTrackRank import StatisticTrackRank
from Utils.Strings import save_file_contents_to_file

class MostListenedTracks(StatisticTrackRank):

    name = "Most Listened Tracks"
    
    def process_track(self, track):
        name = track["master_metadata_track_name"]
        self.results_dict[name] += 1

    def post_process_results(self):
        self.total = sum(list(self.results_dict.values()))
        self.remove_rare_songs()
        self.sort_results()

    def remove_rare_songs(self):
        self.results_dict = {key: value for key, value in self.results_dict.items()
                             if value >= 5}

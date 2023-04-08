import json

from Statistics.Parents.StatisticRangeCoarse import StatisticRangeCoarse

class TimeListened(StatisticRangeCoarse):

    name = "Time Listened"
    range_end_points = [60, 120, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 270, 300, 360]
    units = " (s)"

    def process_file_contents(self, file_contents):
        for track in file_contents:
            if track["skipped"] is False:
                length = track["ms_played"] / 1000
                self.add_to_results_dict(length)

    def post_process_results(self):
        self.total = sum(list(self.results_dict.values()))

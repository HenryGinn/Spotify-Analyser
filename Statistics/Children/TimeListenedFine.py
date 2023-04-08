from Statistics.Parents.StatisticRangeFine import StatisticRangeFine

class TimeListenedFine(StatisticRangeFine):

    name = "Time Listened 2"
    start = 0
    stop = 360
    increment = 1
    units = " (s)"

    def process_file_contents(self, file_contents):
        for track in file_contents:
            if track["skipped"] is False:
                length = track["ms_played"] / 1000
                self.add_to_results_dict(length)

    def post_process_results(self):
        values = list(self.results_dict.values())
        self.total = values[0]
        processed_results = [sum(values[index:]) for index in range(len(values))]
        self.results_dict = {key: value for key, value in zip(self.results_dict, processed_results)}

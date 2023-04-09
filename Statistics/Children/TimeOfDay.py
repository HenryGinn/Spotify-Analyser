from Statistics.Parents.StatisticRangeFine import StatisticRangeFine
from Utils.DataProcessing import moving_average

class TimeOfDay(StatisticRangeFine):

    name = "Time of Day Listened"
    start = 0
    stop = 1440
    increment = 1
    units = " (s)"

    def process_track(self, track):
        time = track["ts"][11:19]
        time = [int(time_component) for time_component in time.split(":")]
        time = 60*time[0] + time[1]
        self.add_to_results_dict(time)

    def post_process_results(self):
        values = self.process_values()
        keys = [key / 60 for key in self.results_dict]
        self.results_dict = {key: value for key, value in zip(keys, values)}
        self.x_limits = [0, 24]
        self.total = sum(values)

    def process_values(self):
        values = list(self.results_dict.values())
        values = moving_average(values, 10)
        return values

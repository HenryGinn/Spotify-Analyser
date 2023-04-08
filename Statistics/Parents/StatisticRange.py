import os
import json

import matplotlib.pyplot as plt

from Statistics.Parents.Statistic import Statistic
from Utils.Strings import save_file_contents_to_file

class StatisticRange(Statistic):

    def __init__(self, spotify_obj):
        Statistic.__init__(self, spotify_obj)
        self.set_ranges_data()

    def set_ranges_data(self):
        self.do_set_ranges_data()

    def do_set_ranges_data(self):
        self.set_range_boundaries()
        self.set_range_names()
        self.set_results_dict()
    
    def set_results_dict(self):
        self.results_dict = {range_name: 0
                             for range_name in self.range_names}

    def add_to_results_dict(self, value):
        index = self.get_range_index(value)
        range_name = self.range_names[index]
        self.results_dict[range_name] += 1

    def save_results_to_file(self, file):
        percentages = self.get_percentages()
        file_contents = {f"{self.name}{self.units}": self.range_names,
                         "Value": self.results_dict.values(),
                         "Percentage": percentages}
        save_file_contents_to_file(file_contents, file)

    def get_percentages(self):
        percentages = [f"{round(100 * value / self.total, 1)}%"
                       for value in self.results_dict.values()]
        return percentages

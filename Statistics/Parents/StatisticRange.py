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
        if hasattr(self, "range_end_points"):
            self.do_set_ranges_data()
        else:
            raise AttributeError(f"'{self.name} has no attribute 'range_end_points'")

    def do_set_ranges_data(self):
        self.set_range_boundaries()
        self.set_range_names()
        self.set_results_dict()

    def set_range_boundaries(self):
        ends = [0] + self.range_end_points
        self.end = ends[-1]
        self.range_boundaries = list(zip(ends[:-1], ends[1:]))

    def set_range_names(self):
        self.range_names = [f"{start}-{stop - 1}"
                            for start, stop in self.range_boundaries]
        self.range_names.append(f"{self.end}+")

    def set_results_dict(self):
        self.results_dict = {range_name: 0
                             for range_name in self.range_names}

    def add_to_results_dict(self, value):
        index = self.get_range_index(value)
        range_name = self.range_names[index]
        self.results_dict[range_name] += 1

    def get_range_index(self, value):
        for index, range_end in enumerate(self.range_end_points):
            if value < range_end:
                return index
        return index + 1

    def save_results_to_file(self, file):
        percentages = self.get_percentages()
        file_contents = {f"{self.name}{self.units}": self.range_names,
                         "Value": self.results_dict.values(),
                         "Percentage": percentages}
        save_file_contents_to_file(file_contents, file)

    def get_percentages(self):
        total = sum(list(self.results_dict.values()))
        percentages = [f"{round(100 * value / total, 1)}%"
                       for value in self.results_dict.values()]
        return percentages

    def plot_results(self):
        self.fig, self.ax = plt.subplots()
        x_values, y_values = zip(*list(self.results_dict.items()))
        self.ax.bar(x_values, y_values)
        self.set_labels()
        plt.savefig(self.results_path_plot, bbox_inches="tight", format=self.plot_format)

    def set_labels(self):
        self.fig.suptitle(self.name)
        self.ax.xlabel = f"{self.name}{self.units}"
        plt.xticks(rotation=60, ha="right")

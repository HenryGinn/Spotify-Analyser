import os
import json

import matplotlib.pyplot as plt

from Statistics.Parents.StatisticRange import StatisticRange
from Utils.Strings import save_file_contents_to_file

class StatisticRangeFine(StatisticRange):

    def set_range_boundaries(self):
        self.ends = list(range(self.start, self.stop)) + [self.stop]
        self.range_boundaries = list(zip(self.ends[:-1], self.ends[1:]))

    def set_range_names(self):
        self.range_names = [end for end in self.ends]

    def get_range_index(self, value):
        for index, range_end in enumerate(self.ends[1:]):
            if value < range_end:
                return index
        return index

    def plot_results(self):
        self.fig, self.ax = plt.subplots()
        x_values = list(self.results_dict.keys())[:-1]
        y_values = list(self.results_dict.values())[:-1]
        self.ax.plot(x_values, y_values)
        self.set_labels()
        plt.savefig(self.results_path_plot, bbox_inches="tight", format=self.plot_format)

    def set_labels(self):
        self.fig.suptitle(self.name)
        self.ax.xlabel = f"{self.name}{self.units}"
        self.set_x_limits()
        #plt.xticks(rotation=60, ha="right")

    def set_x_limits(self):
        if hasattr(self, "x_limits"):
            plt.xlim(self.x_limits)

import matplotlib.pyplot as plt

from Statistics.Parents.StatisticRange import StatisticRange

class StatisticRangeCoarse(StatisticRange):

    def set_ranges_data(self):
        if hasattr(self, "range_end_points"):
            self.do_set_ranges_data()
        else:
            raise AttributeError(f"'{self.name} has no attribute 'range_end_points'")

    def set_range_boundaries(self):
        ends = [0] + self.range_end_points
        self.end = ends[-1]
        self.range_boundaries = list(zip(ends[:-1], ends[1:]))

    def set_range_names(self):
        self.range_names = [f"{start}-{stop - 1}"
                            for start, stop in self.range_boundaries]
        self.range_names.append(f"{self.end}+")

    def get_range_index(self, value):
        for index, range_end in enumerate(self.range_end_points):
            if value < range_end:
                return index
        return index + 1

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

import numpy as np

def moving_average(data, window_size=5):
    window = np.ones(window_size)
    numerator = np.convolve(data, window, "same")
    denominator = np.convolve(np.ones(len(data)), window, "same")
    moving_average = numerator / denominator
    return moving_average

def get_percentages(values, total, decimal_places=1):
    percentages = [f"{round(100 * value / total, decimal_places)}%"
                   for value in values]
    return percentages

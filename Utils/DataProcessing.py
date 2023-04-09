import numpy as np

def moving_average(data, window_size=5):
    window = np.ones(window_size)
    numerator = np.convolve(data, window, "same")
    denominator = np.convolve(np.ones(len(data)), window, "same")
    moving_average = numerator / denominator
    return moving_average

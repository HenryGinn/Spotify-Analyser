from Main.Spotify import Spotify

spotify = Spotify()
spotify.preprocess_files()
spotify.authenticate()
spotify.produce_statistic_last()

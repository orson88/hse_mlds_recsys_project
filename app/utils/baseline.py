import json
import numpy as np
from pathlib import Path


class Baseline:
    workdir = Path(__file__).parent

    def __init__(self):
        with open(self.workdir.parent / 'data' / 'top_songs_10k.json') as f:
            self.most_popular_songs = json.load(f)

    def predict_most_popular(self, k: int):
        """
        Predict k most popular songs
        :param k: number of songs to return
        :return: k most popular songs
        """
        return self.most_popular_songs[:k]

    def predict_random(self, k):
        """
        Predict k random songs from 10k most popular
        :param k: number of songs to return
        :return: k random songs
        """

        return list(np.random.choice(self.most_popular_songs,
                                     size=k,
                                     replace=False))

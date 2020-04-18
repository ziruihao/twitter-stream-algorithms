import json
from random import randint
from statistics import median
from streaming_algorithms.abstract_algorithm import AbstractStreamingAlgorithm

class MorrisCounter(AbstractStreamingAlgorithm):
    def __init__(self, t):
        super().__init__()
        self.t = t
        self.count = [0 for _ in range(t)]
    
    def process(self, token):
        for t in range(self.t):
            if (randint(1, 2**(self.count[t])) is 1):
                self.count[t] += 1

    def query(self, token):
        pass

    def query_all(self, id):
        to_compute_medians = []
        for t in range(self.t):
            to_compute_medians.append(2**self.count[t] - 1)
        print('Morris exporting to ' + id)
        with open('data/moris-' + id + '.json', 'w') as f:
            json.dump({'length': median(to_compute_medians)}, f)
        return median(to_compute_medians)
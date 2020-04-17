import copy
import json
from algorithms.frequency_estimation_algorithm import FrequencyEstimationAlgorithm

class Exact(FrequencyEstimationAlgorithm):
    def __init__(self):
        super.__init__()

    def process(self, token):
        if (token in self.freqs.keys()): self.freqs[token] += 1
        else: self.freqs[token] = 1

    def query_all(self):
        with open ('data/actual_freqs-' + str(hash(self)) + '.json', 'w', encoding='utf-8') as f:
        pairs = list(self.actual_freqs.items())
        pairs.sort(key=lambda e: e[1], reverse=True)
        json.dump(pairs, f)
    return self.actual_freqs
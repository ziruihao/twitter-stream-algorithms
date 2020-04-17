import json
from streaming_algorithms.abstract_algorithm import AbstractStreamingAlgorithm

class Exact(AbstractStreamingAlgorithm):
    def __init__(self):
        super().__init__()

    def process(self, token):
        self.count += 1
        if (token in self.freqs.keys()): self.freqs[token] += 1
        else: self.freqs[token] = 1

    def query(self, token):
        pass

    def query_all(self, id):
        print('Exporting exact data to ' + id)
        with open ('data/exact-' + id + '.json', 'w', encoding='utf-8') as f:
            pairs = list(self.freqs.items())
            pairs.sort(key=lambda e: e[1], reverse=True)
            json.dump({'length': self.count, 'freqs': pairs}, f)
        return self.freqs
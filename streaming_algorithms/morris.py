import json
from random import randint
from streaming_algorithms.abstract_algorithm import AbstractStreamingAlgorithm

class MorrisCounter(AbstractStreamingAlgorithm):
    def __init__(self):
        super().__init__()
    
    def process(self, token):
        if (randint(1, 2**self.count) is 1):
            self.count += 1

    def query(self, token):
        pass

    def query_all(self, id):
        print('Morris exporting to ' + id)
        with open('data/moris-' + id + '.json', 'w') as f:
            json.dump({'length': (2**self.count - 1)}, f)
        return 2**self.count - 1
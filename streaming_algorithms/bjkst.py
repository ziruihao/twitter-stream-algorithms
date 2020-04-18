import json
from statistics import median
from streaming_algorithms.abstract_algorithm import AbstractStreamingAlgorithm
from hash import Two_Universal_Hash
from word_to_number import WordToNumber

class BJKST(AbstractStreamingAlgorithm):
    def __init__(self, k, t):
        super().__init__()
        self.k = k
        self.t = t
        self.count = [0 for _ in range(t)]
        self.B = [[] for _ in range(t)]

        self.word_to_number = WordToNumber()
        distinct_elements_upper_bound = self.word_to_number.set_method('sha')

        self.H = Two_Universal_Hash(distinct_elements_upper_bound, distinct_elements_upper_bound)
        self.h = [self.H.pick_hash() for _ in range(t)]

    def process(self, token):
        token = self.word_to_number.convert(token)
        for t in range(self.t):
            if (self.zeros(self.h[t](token)) >= self.count[t]):
                self.B[t].append(self.zeros(self.h[t](token)))
                while (len(self.B[t]) >= self.k):
                    self.count[t] += 1
                    self.B[t] = list(filter(lambda e: e >= self.count[t], self.B[t]))

    def query(self, query):
        pass

    def query_all(self, id):
        to_compute_medians = []
        for t in range(self.t):
            to_compute_medians.append(len(self.B[t]) * (2**self.count[t]))
        print('BJKST exporting to ' + id)
        with open('data/bjkst-' + id + '.json', 'w') as f:
            json.dump({'distinct_elements': median(to_compute_medians)}, f)

    def zeros(self, n):
        b = bin(n)[2:]
        return len(b) - len(b.rstrip('0'))

import copy
import json
from random import choice
from statistics import median
from difflib import SequenceMatcher
import Levenshtein
from streaming_algorithms.abstract_algorithm import AbstractStreamingAlgorithm
from hash import Two_Universal_Hash
from word_to_number import WordToNumber

class CountSketch(AbstractStreamingAlgorithm):
    def __init__(self, k, t):
        super().__init__()
        self.k = k
        self.t = t
        self.freqs = [[0 for _ in range(k)] for _ in range(t)]

        self.word_to_number = WordToNumber()
        distinct_elements_upper_bound = self.word_to_number.set_method('sha')

        self.H = Two_Universal_Hash(self.k, distinct_elements_upper_bound)
        self.h = [self.H.pick_hash() for _ in range(t)]
        self.G = Two_Universal_Hash(2, distinct_elements_upper_bound)
        self.g = [self.G.pick_hash() for _ in range(t)]

    def process(self, token):
        token = self.word_to_number.convert(token)
        for t in range(self.t):
            delta = self.g[t](token)
            if (delta is 0): delta = -1
            else: delta = 1
            self.freqs[t][self.h[t](token)] += delta

    def query(self, query):
        query = self.word_to_number.convert(query)
        to_compute_medians = []
        for t in range(self.t):
            to_compute_medians.append(abs(self.freqs[t][self.h[t](query)]))
        return int(median(to_compute_medians))

    def query_all(self, id):
        print('CountSketch still in progress.. no export')
        # to-do
        # self.freqs = list(map(lambda l: list(map(abs, l)), self.freqs))
        # print('Exporting CountSketch to ' + id)
        # with open ('data/countsketch-' + id + '.json', 'w') as f:
        #     json.dump({'freqs': self.freqs}, f)
        # return self.freqs
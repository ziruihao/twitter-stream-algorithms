import copy
import json
from random import choice
from difflib import SequenceMatcher
import Levenshtein
from streaming_algorithms.abstract_algorithm import AbstractStreamingAlgorithm
from hash import Two_Universal_Hash
from word_to_number import WordToNumber

class CountSketch(AbstractStreamingAlgorithm):
    def __init__(self, k):
        super().__init__()
        self.k = k
        self.freqs = [0] * k

        self.word_to_number = WordToNumber()
        distinct_elements_upper_bound = self.word_to_number.set_method('sha')

        self.H = Two_Universal_Hash(self.k, distinct_elements_upper_bound)
        self.h = self.H.pick_hash()
        self.G = Two_Universal_Hash(2, distinct_elements_upper_bound)
        self.g = lambda : choice([-1, 1])

    def process(self, token):
        token = self.word_to_number.convert(token)
        self.freqs[self.h(token)] += self.g()

    def query(self, query):
        return self.freqs[self.h(self.word_to_number.convert(query))]

    def query_all(self, id):
        print('Exporting CountSketch to ' + id)
        with open ('data/countsketch-' + id + '.json', 'w') as f:
            json.dump({'freqs': self.freqs}, f)
        return self.freqs
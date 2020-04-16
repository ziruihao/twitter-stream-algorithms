import copy
import json
import difflib
import Levenshtein
from algorithms.frequency_estimation_algorithm import FrequencyEstimationAlgorithm

class MisraGries(FrequencyEstimationAlgorithm):
    def __init__(self):
        super().__init__()

    def initialize(self, k, scoring_method):
        self.est_freqs = {}
        self.actual_freqs = {}
        self.stream_length = 0
        self.k = k

        # determining scoring method: https://stackoverflow.com/questions/6690739/high-performance-fuzzy-string-comparison-in-python-use-levenshtein-or-difflib
        self.scorer = None
        if (scoring_method is 'levenshtein'):
            self.scorer = Levenshtein.ratio
        elif (scoring_method is 'sequence_match'):
            self.scorer = lambda t, e: difflib.SequenceMatcher(None, t, e).ratio()

    def process(self, token):
        print(token)
        self.stream_length += 1

        # if we are already logging this token
        best_match = self.found_in(token, self.est_freqs.keys(), self.scorer)
        if (best_match is not ''):
            self.est_freqs[best_match] += 1
            
        else:
            # if there is still space to log this token
            if (len(self.est_freqs.keys()) < self.k):
                self.est_freqs[token] = 1
            else:
                # decrement all est_freqs
                copy_of_keys = copy.copy(list(self.est_freqs.keys()))
                for key in copy_of_keys:
                    self.est_freqs[key] += -1
                    if (self.est_freqs[key] is 0):
                        self.est_freqs.pop(key)
        
        # also records the actual frequencies for comparison
        if (token in self.actual_freqs.keys()): self.actual_freqs[token] += 1
        else: self.actual_freqs[token] = 1

    def query(self, query):
        if (query in self.est_freqs.keys()):
            return self.est_freqs[query]
        else:
            return 'Too infrequent to provide estimate'

    def get_est_freqs(self):
        with open ('data/est_freqs-' + str(hash(self)) + '.json', 'w', encoding='utf-8') as f:
            json.dump(self.est_freqs, f)
        return self.est_freqs

    def get_actual_freqs(self):
        with open ('data/actual_freqs-' + str(hash(self)) + '.json', 'w', encoding='utf-8') as f:
            pairs = list(self.actual_freqs.items())
            pairs.sort(key=lambda e: e[1], reverse=True)
            json.dump(pairs, f)
        return self.actual_freqs

    # this method will return either itself or a word sufficiently 'close' to it from the list
    def found_in(self, token, list, scorer):
        if (len(list) is 0): return ''
        else:
            distances = []
            for element in list:
                # print({'token': token, 'element': element, 'distance': scorer(token, element)})
                distances.append({'element': element, 'distance': scorer(token, element)})
            distances.sort(key=lambda e: e['distance'])
            if (distances[0]['distance'] > 0.8):
                print('Substituting the word "' + token + '" for "' + distances[0]['element'] + '"')
                return distances[0]['element']
            else: return ''
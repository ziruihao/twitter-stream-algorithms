import copy
import json
from difflib import SequenceMatcher
import Levenshtein
from streaming_algorithms.abstract_algorithm import AbstractStreamingAlgorithm

class MisraGries(AbstractStreamingAlgorithm):
    def __init__(self, k, scoring_method):
        super().__init__()
        self.k = k

        # determining scoring method: https://stackoverflow.com/questions/6690739/high-performance-fuzzy-string-comparison-in-python-use-levenshtein-or-difflib
        self.scorer = None
        if (scoring_method is 'levenshtein'):
            self.scorer = Levenshtein.ratio
        elif (scoring_method is 'sequence_match'):
            self.scorer = lambda t, e: SequenceMatcher(None, t, e).ratio()


    def process(self, token):
        # if we are already logging this token
        best_match = self.found_in(token, self.freqs.keys(), self.scorer)
        if (best_match is not ''):
            self.freqs[best_match] += 1
            
        else:
            # if there is still space to log this token
            if (len(self.freqs.keys()) < self.k - 1):
                self.freqs[token] = 1
            else:
                # decrement all freqs
                copy_of_keys = copy.copy(list(self.freqs.keys()))
                for key in copy_of_keys:
                    self.freqs[key] += -1
                    if (self.freqs[key] is 0):
                        self.freqs.pop(key)

    def query(self, query):
        if (query in self.freqs.keys()):
            return self.freqs[query]
        else:
            return 'Too infrequent to provide estimate'

    def query_all(self, id):
        print('Exporting Misra-Gries to ' + id)
        with open ('data/misra-' + id + '.json', 'w') as f:
            json.dump({'freqs': self.freqs}, f)
        return self.freqs

    # this method will return either itself or a word sufficiently 'close' to it from the list
    def found_in(self, token, list, scorer):
        if (len(list) is 0): return ''
        else:
            distances = []
            for element in list:
                distances.append({'element': element, 'distance': scorer(token, element)})
            distances.sort(key=lambda e: e['distance'])
            if (distances[0]['distance'] > 0.8):
                print('Substituting the word "' + token + '" for "' + distances[0]['element'] + '"')
                return distances[0]['element']
            else: return ''
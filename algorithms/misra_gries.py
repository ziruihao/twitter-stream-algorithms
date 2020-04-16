import copy
import Levenshtein
from algorithms.frequency_estimation_algorithm import FrequencyEstimationAlgorithm

class MisraGries(FrequencyEstimationAlgorithm):
    def __init__(self, k):
        super().__init__()
        self.k = k

    def initialize(self):
        pass

    def process(self, token):
        print(token)
        self.stream_length += 1

        # if we are already logging this token
        best_match = self.found_in(token, dict.keys(self.est_freqs))
        if (best_match is not ''):
            self.est_freqs[best_match] += 1
            
        else:
            # if there is still space to log this token
            if (len(dict.keys(self.est_freqs)) < self.k):
                self.est_freqs[token] = 1
            else:
                # decrement all est_freqs
                copy_of_keys = copy.copy(list(dict.keys(self.est_freqs)))
                for key in copy_of_keys:
                    self.est_freqs[key] += -1
                    if (self.est_freqs[key] is 0):
                        self.est_freqs.pop(key)
        
        # also records the actual frequencies for comparison
        if (token in dict.keys(self.actual_freqs)): self.actual_freqs[token] += 1
        else: self.actual_freqs[token] = 1

    def query(self, query):
        if (query in dict.keys(self.est_freqs)):
            return self.est_freqs[query]
        else:
            return 'Too infrequent to provide estimate'

    def get_est_freqs(self):
        return self.est_freqs

    def get_actual_freqs(self):
        return self.actual_freqs

    # this method will return either itself or a word sufficiently 'close' to it from the list
    def found_in(self, token, list):
        if (len(list) is 0): return ''
        else:
            distances = []
            for element in list:
                distances.append({'element': element, 'distance': Levenshtein.distance(token, element)})
            distances.sort(key=self.levenshtein_list_sorter)
            if (distances[0]['distance'] < 1):
                # print('Substituting the word "' + token + '" for "' + distances[0]['element'] + '"')
                return distances[0]['element']
            else: return ''

    # sort helper for the list of Levenshtein distances
    def levenshtein_list_sorter(self, e):
        return e['distance']
import copy
from algorithms.frequency_estimation_algorithm import FrequencyEstimationAlgorithm

class MisraGries(FrequencyEstimationAlgorithm):
    def __init__(self, k):
        super().__init__()
        self.k = k

    def initialize(self):
        pass

    def process(self, token):
        print(token)
        # if we are already logging this token
        if (token in dict.keys(self.est_freqs)):
            self.est_freqs[token] += 1
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

    def query(self, query):
        if (query in dict.keys(self.est_freqs)):
            return self.est_freqs[query]
        else:
            return 'Too infrequent to provide estimate'

    def get_all_data(self):
        return self.est_freqs
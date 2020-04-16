from stream import Stream
from algorithms.misra_gries import MisraGries
import Levenshtein
import re
import json


algo = MisraGries()
algo.initialize(10, 'sequence_match')

s = Stream(10, algo)
s.set_mode('text')
s.set_filter(['college'])
print('Done, exported to ' + str(hash(algo)))

algo.get_est_freqs()
algo.get_actual_freqs()
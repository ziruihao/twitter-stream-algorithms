from stream import Stream
from algorithms.misra_gries import MisraGries
import Levenshtein
import re

algo = MisraGries()
algo.initialize(10, 'sequence_match')

s = Stream(10000, algo)
s.set_mode('text')
s.set_filter(['college'])
print('done')

algo.get_est_freqs()
algo.get_actual_freqs()
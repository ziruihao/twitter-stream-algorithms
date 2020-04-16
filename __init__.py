from stream import Stream
from algorithms.misra_gries import MisraGries
import Levenshtein
import re

# print(Levenshtein.distance('covid', 'COVID'))

algo = MisraGries(10)
s = Stream(5000, algo)
s.set_mode('text')
s.set_filter(['college'])
print(algo.get_actual_freqs())
print('estimate')
print(algo.get_est_freqs())
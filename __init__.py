from stream import Stream
from algorithms.misra_gries import MisraGries
import Levenshtein
import re

# print(Levenshtein.distance('covid', 'COVID'))

algo = MisraGries(10)
s = Stream(10, algo)
s.set_mode('text')
s.set_filter(['college'])

a = list(dict.items(algo.get_actual_freqs())).sort(key=lambda e: e[1])
print(a)
print('estimate')
print(algo.get_est_freqs())
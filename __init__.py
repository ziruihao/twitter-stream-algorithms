from stream import Stream
from algorithms.misra_gries import MisraGries
import Levenshtein

# print(Levenshtein.distance('covid', 'COVID'))

algo = MisraGries(10)
s = Stream(5000, algo)
s.set_filter(['USA'])
print(algo.get_all_data())
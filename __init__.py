from stream import Stream
from algorithms.misra_gries import MisraGries

algo = MisraGries(10)
s = Stream(100, algo)
s.set_filter(['USA'])
print(algo.get_all_data())
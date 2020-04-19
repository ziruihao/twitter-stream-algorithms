from twitter_stream import TwitterStream
from shakespeare_stream import ShakespeareStream
from streaming_algorithms import MisraGries
from streaming_algorithms import Exact
from streaming_algorithms import MorrisCounter
from streaming_algorithms import CountSketch
from streaming_algorithms import BJKST
import time

stamp = str(int(time.time()) % 10000)

algorithms = []

algorithms.append(Exact())
algorithms.append(MisraGries(k=25, scoring_method='sequence_match'))
algorithms.append(MorrisCounter(t=500))
algorithms.append(CountSketch(k=100, t=500))
algorithms.append(BJKST(k=10, t=500))

# twitter_stream = TwitterStream(1000, algorithms)
# twitter_stream.set_mode('text')
# twitter_stream.set_filter(['college'])

shakespeare_stream = ShakespeareStream(algorithms)
shakespeare_stream.stream('shakespeare', 6)

for algorithm in algorithms:
    algorithm.query_all(stamp)

# misra.query_all(stamp)
# morris.query_all(stamp)
# exact.query_all(stamp)
# count_sketch.query_all(stamp)
# bjkst.query_all(stamp)
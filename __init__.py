from stream import Stream
from streaming_algorithms import MisraGries
from streaming_algorithms import Exact
from streaming_algorithms import MorrisCounter
from streaming_algorithms import CountSketch
from streaming_algorithms import BJKST
import time

stamp = str(int(time.time()) % 10000)

exact = Exact()

misra = MisraGries(k=25, scoring_method='sequence_match')

morris = MorrisCounter(t=500)

count_sketch = CountSketch(k=100, t=500)

bjkst = BJKST(k=10, t=500)

s = Stream(1000, [misra, exact, morris, count_sketch, bjkst])
s.set_mode('text')
s.set_filter(['college'])

misra.query_all(stamp)
morris.query_all(stamp)
exact.query_all(stamp)
count_sketch.query_all(stamp)
bjkst.query_all(stamp)
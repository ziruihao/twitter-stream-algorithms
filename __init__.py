from stream import Stream
from streaming_algorithms import MisraGries
from streaming_algorithms import Exact
from streaming_algorithms import MorrisCounter
import time

stamp = str(int(time.time()) % 10000)

exact = Exact()

misra = MisraGries(10, 'sequence_match')

morris = MorrisCounter()

s = Stream(10, [misra, exact, morris])
s.set_mode('text')
s.set_filter(['college'])

misra.query_all(stamp)
morris.query_all(stamp)
exact.query_all(stamp)

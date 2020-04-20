# Streaming Algorithms

The streaming algoriothms I implement follow the below template.

```python
import abc
class AbstractStreamingAlgorithm(abc.ABC):
    def __init__(self):
        self.freqs = {} # default initial value for the dict of token frequencies
        self.count = 0 # default initial value for the count estimation

    # Processes a single `token`, invoked by a stream handler.
    @abc.abstractmethod
    def process(self, token):
        pass

    # Handles a single `query` that identifies a unique token.
    @abc.abstractmethod
    def query(self, query):
        pass

    # Exports all data to `data/`.
    @abc.abstractmethod
    def query_all(self, id):
        pass
```

## Word to Number

Words are hashed to a 16-bit integer using Python's classic `hash` functionality. I tried implementing other hasing techniques, found in [`word_to_number.py`](../blob/master/word_to_number.py), but found this to be the fasted and most space-efficient while preserving as much uniqueness as possible.

## 2-Universal Hashing

I generate 2-universal hash families using the [`TwoUniversalHash`](../blob/master/two_universal_hash.py) class. The family is generated for a given domain and range. Hash functions are of the form `((ax + b) % p) % k` where `p` is the first prime after the size of the domain and `k` is the size of the range.

The class has a `verify_2_universality` method to test the coefficient of variation for hashed pairs.

```python
class TwoUniversalHash:
    def __init__(self, bins, elements):
        self.bins = bins # range
        self.elements = elements # domain
        self.p = nth_prime(1, elements) # finds the first prime greater than `elements`
    
    # Draws a random hash function from the family.
    def pick_hash(self):
        a = randint(1, self.p - 1)
        b = randint(0, self.p - 1)
        return lambda x: (((a * x) + b) % self.p) % self.bins

    # Tests 2-universality by randomly hashing `iterations` elements and measuring the average coefficient of variation for the bins
    def verify_2_universality(self, iterations):
        mappings = [[0 for _ in range(self.bins)] for _ in range(self.bins)]

        for _ in range(iterations):
            h = self.pick_hash()
            x = randint(1, self.elements)
            y = randint(1, self.elements)
            mappings[h(x)][h(y)] += 1
        
        avg_cv = 0.0

        # for a fixed h(x), what is the coefficient of variation for the frequencies that some h(y) are picked in tandem?
        for i in range(self.bins):
            avg_cv += stdev(mappings[i]) / mean(mappings[i])
        
        print('The coefficient of variation is ' + str(int((avg_cv / self.bins) * 100)) + '%')
```
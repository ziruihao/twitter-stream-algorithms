from math import ceil, log2
from statistics import mean, variance, stdev
from random import randint
from primesieve import nth_prime

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
        
        print('The coefficient of variation is ' + str(((avg_cv / self.bins) * 100)) + '%')

if __name__ == '__main__':
    H = TwoUniversalHash(5, 1000)
    H.verify_2_universality(1000000)

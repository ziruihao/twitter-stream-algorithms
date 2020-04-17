import copy
import json
from random import randint
from math import pow 
from algorithms.counting_algorithm import CountingAlgorithm

class MorrisCounter(CountingAlgorithm):
    def __init__(self):
        super().__init__()
    
    def process(self, token):
        if (randint(0, pow(2, self.count)) is 0):
            self.count += 1

    def query(self):
        return pow(2, self.count) - 1
from numpy import prod
from hashlib import sha256

class WordToNumber():
    
    def __init__(self):
        self.prime_map = { 'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101 }
        self.char_map = { 'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26' }

    def set_method(self, method):
        self.method = method
        if (method is 'prime_factorization'):
            return 2**16
        elif (method is 'char_partition'):
            return 0
        elif (method is 'sha'):
            return 2**16
        else:
            return 0
    
    def convert(self, word):
        if (self.method is 'prime_factorization'):
            return self.prime_factorization(word)
        elif (self.method is 'char_partition'):
            return self.char_partition(word)
        elif (self.method is 'sha'):
            return self.sha(word)
        else:
            return word

    def prime_factorization(self, word):
        factors = list(map(lambda char: self.prime_map[char], word))
        raise_to_power = []
        for index, factor in enumerate(factors):
            raise_to_power.append((factor**(index + 1)))
        return int(prod(raise_to_power) % 2**16)

    def char_partition(self, word):
        return int('1' + ''.join(map(lambda char: self.char_map[char], word)))

    def sha(self, word):
        return int(sha256(word.encode('utf-8')).hexdigest(), 16) % 2**16
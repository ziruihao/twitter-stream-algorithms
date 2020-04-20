# 2-Universal Hashing

I generate 2-universal hash families given domain and range of the form `((ax + b) % p) % k` where `p` is the first prime after the size of the domain and `k` is the size of the range.


## Universality Testing

The class has a `verify_2_universality` method to test the coefficient of variation for hashed pairs. These are some results run on 1,000,000 iterations.

| Domain        | Range        | CV    |
| ------------- |:------------:| -----:|
| 1000          | 5 (0.5%)     | 0.4%  |
| 1000          | 10 (1%)      | 0.9%  |
| 1000          | 100 (10%)    | 10.4% |

These tests show that the hashing is sufficient good for 2-universality if the range is sufficiently smaller than the domain.
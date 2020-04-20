# Twitter Stream Algorithms Demo

After learning a few stream algorithms from COSC 35 (@ Dartmouth College taught by Prof. Chakrabarti), I wanted to implement some and see them performing with real data.

The first question was what kind of stream data can a college student get access to? The easiest one was from a platform that is very much just streams of data - Twitter.

![twitter hashtags streams](https://github.com/ziruihao/twitter-stream-algorithms/blob/master/misc/demo.gif "Twitter hashtags streaming")

### Get Started

Create a `.env` in root directory and paste the variables from [here](https://drive.google.com/file/d/1o04angBUMD4ATCupEaIACHP0IHjXxaRw/view?usp=sharing).

```
$ pip install -r requirements.txt
$ python __init__.py
```

## Results

| Twitter words   | Actual                        | Estimate (algorithm output) |
|-----------------|-------------------------------|-----------------------------|
| Total tokens    | 20,000                        | 16,383                      |
| Distinct tokens | 3,195                         | 3,586                       |
| Heavy hitters*   | See `data/exact-twitter.json` | See `data/misra-twitter.json`  |

| Shakespeare words   | Actual                        | Estimate (algorithm output) |
|---------------------|-------------------------------|-----------------------------|
| Total tokens        | 20,000                        | 16,383                      |
| Distinct tokens     | 3,615                         | 4,096                       |
| Heavy hitters*       | See `data/exact-shakespeare.json` | See `data/misra-shakespeare.json`  |

These estimates have too high of a variance and they land on the same number. I will implement some new methods we just learned in class to reduce this variance and make the space of possible estimates more dense.

* The heavy hitters approximation is not complete yet.

## Streaming

### Algorithms

I implement the following stream algorithms:

1. **Misra-Gries** - token frequencies to generate heavy hitters
   1. `k: number of bins`, `scoring_method: either Levenshtein or SequenceMatcher for word similarity`
2. **Moris** - total tokens counter
   1. `t: number of parallel estimators to then take the medians of`
3. **BJKST** - distinct tokens counter
   1. `k: number of bins`, `t: number of parallel estimators to then take the medians of`
4. **CountSketch** - token frequencies (work in progress)
   1. `k: number of bins`, `t: number of parallel estimators to then take the medians of`
5. Exact - not an algorithm, rather it just counts the exact number of tokens, distinct tokens, and frequencies for each token to provide a baseline of comparison for the other algorithms

### Data

A steady stream of data is fed into each of those algorithms via these two data sources.

#### Twitter API

I'm leveraging [Twitter's Stream API](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview) via the Python [Tweepy library](http://docs.tweepy.org/en/latest/streaming_how_to.html).

Once a stream is initiated, we receive continuous selected data from Twitter. This is not the entirety of Twitter's streams, but rather a percentage (controlled by Twitter based on allocations for free developer users).

#### Shakespeare's Works

A more offline comes from simulating a stream using words from 100 of Shakespeare's works. The raw text was accessed from [Project Gutenberg](http://www.gutenberg.org/cache/epub/100/pg100.txt), cleaned, and extracted into 219 separate works, each containing around a few thousand words. The stream chooses a particular work and feeds the words the same way as the Twitter streaming process.

## Next Steps

### Web Interface

I am planning to build an iteractive web app for better interaction with the algorithms, and to visualize how these streaming algorithms manipulate data in real-time. For example, for Misra-Gries, I want to animate the **size** of incoming tokens (words) to demonstrate their predicted accumulated counts held by the algorithm.

### Improvements

I want to improve the word matching process to better condense words based on similarity and gramatical connections. I also want to devise a better hashing method from word strings to integers that is more suited for this particular application. This would involve factoring in the domain of possible strings (length, arrangement of characters) to make the hashing more tailored to English words.

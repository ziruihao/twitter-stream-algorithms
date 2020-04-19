# Twitter Stream Algorithms Demo

After learning a few stream algorithms from COSC 35 (@ Dartmouth College taught by Prof. Chakrabarti), I wanted to implement some and see them performing with real data.

The first question was what kind of stream data can a college student get access to? The easiest one was from a platform that is very much just streams of data - Twitter.

```
$ pip install -r requirements.txt
$ python __init__.py
```

### Results

| Twitter words   | Actual                        | Estimate (algorithm output) |
|-----------------|-------------------------------|-----------------------------|
| Total tokens    | 20,000                        | 16,383                      |
| Distinct tokens | 3,195                         | 3,586                       |
| Heavy hitters   | See `data/exact-[run id].json` | See `data/misra_gries-[run id].json`  |

| Shakespeare words   | Actual                        | Estimate (algorithm output) |
|---------------------|-------------------------------|-----------------------------|
| Total tokens        | 20,000                        | 16,383                      |
| Distinct tokens     | 3,615                         | 11,456                      |
| Heavy hitters       | See `data/exact-[run id].json` | See `data/misra_gries-[run id].json`  |

## Streaming

### Algorithms

I implement the following stream algorithms:

1. Misra-Gries - token frequencies to generate heavy hitters
   1. `k: number of bins`, `scoring_method: either Levenshtein or SequenceMatcher for word similarity`
2. Moris - total tokens counter
   1. `t: number of parallel estimators to then take the medians of`
3. BJKST - distinct tokens counter
   1. `k: number of bins`, `t: number of parallel estimators to then take the medians of`
4. CountSketch - token frequencies (work in progress)
   1. `k: number of bins`, `t: number of parallel estimators to then take the medians of`

### Data

A steady stream of data is fed into each of those algorithms via these two data sources.

#### Twitter API

I'm leveraging Twitter's Stream API <https://developer.twitter.com/en/docs/tweets/filter-realtime/overview> via the Python Tweepy library <http://docs.tweepy.org/en/latest/streaming_how_to.html.>

Once a stream is initiated, we receive continuous selected data from Twitter. This is not the entirety of Twitter's streams, but rather a percentage (controlled by Twitter based on allocations for free developer users).

#### Shakespeare's Works

A more offline comes from simulating a stream using words from 100 of Shakespeare's works. The raw text was accessed from <http://www.gutenberg.org/cache/epub/100/pg100.txt>, cleaned, and extracted into 219 separate works, each containing around a few thousand words. The stream chooses a particular work and feeds the words the same way as the Twitter streaming process.

## Architecture

### Stream Handlers

A set of `algorithms` are passed in to the two stream handlers below.

#### Twitter

I create a wrapper for the incoming Twitter data in `twitter_stream.py`. The `set_filter` method connects to Twitter and begins the streaming channel. We can configure the tweets coming in with `filters`, such as `#USA` or `#travel`.

This class's most important method is `on_data(data)` which is invoked by `Tweepy`'s stream handler on each push of data, which is one tweet. The method parses the raw tweet data and sends individual words extracted from the tweet body to the stream algorithms as tokens.

This class can also send a tweet's hashtags or location data as tokens, depending on the `mode`.

#### Shakespeare

The streamer for Shakespeare handles the cleaning and extraction of words from a specified corpus and feeds it into the stream algorithms as tokens.

The cleaning process involves removing all whitespace, punctuation, character names, stage instructions, and other miscallenious symbols.

### Algorithms

All algorithms implement the `AbstractStreamingAlgorithm` template for which the methods `process(token j)`, `query(token j)`, and `query_all()` are defined.

### 2-Universal Hashing

I generate 2-universal hash families using the `TwoUniversalHash` class. The family is generated for a given domain and range. Hash functions are of the form `((ax + b) % p) % k` where `p` is the first prime after the size of the domain and `k` is the size of the range.

### Word Matching

After running the stream for a lot of tweets, I realized there's a lot of close matches between words, such as `COVID-19` versus `covid`. If applicable, each algorithm will first check for any close word matches on the arrival of a new token.
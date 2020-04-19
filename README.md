# Twitter Stream Algorithms Demo

After learning a few stream algorithms from COSC 35 (@ Dartmouth College taught by Prof. Chakrabarti), I wanted to implement some and see them performing with real data.

The first question was what kind of stream data can a college student get access to? The easiest one was from a platform that is very much just streams of data - Twitter.

## Streaming

### Algorithms

I implement the following stream algorithms:

1. Misra-Gries - token frequencies
2. Moris - total tokens counter
3. BJKST - distinct tokens counter
4. CountSketch - token frequencies (work in progress)

### Data

#### Twitter API

I'm leveraging Twitter's Stream API <https://developer.twitter.com/en/docs/tweets/filter-realtime/overview> via the Python Tweepy library <http://docs.tweepy.org/en/latest/streaming_how_to.html.>

Once a stream is initiated, we receive continuous selected data from Twitter. This is not the entirety of Twitter's streams, but rather a percentage (controlled by Twitter based on allocations for free developer users).

## Architecture

### Stream Handler Class

I create a wrapper for the incoming Twitter data in `stream.py`.

This class's most important method is `on_data(data)` which is invoked by `Tweepy`'s stream handler on each push of data, which is one tweet. The method parses the raw tweet data and sends individual words extracted from the tweet body to the stream algorithms as tokens.

This class can also send a tweet's hashtags or location data as tokens, depending on the `mode`.

### Word Matching

After running the stream for a lot of tweets, I realized there's a lot of close matches between words, such as `COVID-19` versus `covid`. If applicable, each algorithm will first check for any close word matches on the arrival of a new token.
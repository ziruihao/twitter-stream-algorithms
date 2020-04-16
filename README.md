# Twitter Stream Algorithms Demo

After learning a few stream algorithms from COSC 35 (@ Dartmouth College taught by Prof. Chakrabarti), I wanted to implement some and see them performing with real data.

The first question was what kind of stream data can a college student get access to? The easiest one was from a platform that is very much just streams of data - Twitter.

## Twitter API

I'm leveraging Twitter's Stream API <https://developer.twitter.com/en/docs/tweets/filter-realtime/overview> via the Python Tweepy library <http://docs.tweepy.org/en/latest/streaming_how_to.html.>

Once a stream is initiated, we receive continuous selected data from Twitter. This is not the entirety of Twitter's streams, but rather a percentage (controlled by Twitter based on allocations for free developer users).

### Stream Object

I create a wrapper for the incoming Twitter data in `stream.py`.

This class's most important method is `on_data(data)` which is invoked by `Tweepy`'s stream handler on each push of data, which is one tweet. The method parses the raw tweet data and saves the `hashtags` which are then sent to the selected algorithm.

### Hastag Word Matching

After running the stream for a lot of tweets, I realized there's a lot of close matches between hashtags, such as `COVID-19` versus `covid`. I this develop a procedure to best match a hashtag to one which the stream has already seen.

The first layer of this procedure calculates the Levenshtein distance between the words and substitutes an incoming `hashtag` with an already seen `hashtag` whose distance is equal to `1`.

Developing more layers...

## Stream Algorithms

I implement the following stream algorithms:
1. Misra-Gries
2. CountSketch
3. Implementing more variants of CountSketch...

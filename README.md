# Twitter Stream Algorithms Demo

After learning a few stream algorithms from COSC 30 (@ Dartmouth College taught by Prof. Chakrabarti), I wanted to implement some and see them performing with real data.

The first question was what kind of stream data can a college student get access to? The easiest one was from a platform that is very much just streams of data - Twitter.

## Twitter API

I'm leveraging Twitter's Stream API https://developer.twitter.com/en/docs/tweets/filter-realtime/overview via the Python Tweepy library http://docs.tweepy.org/en/latest/streaming_how_to.html.

Once a stream is initiated, we receive continuous selected data from Twitter. This is not the entirety of Twitter's streams, but rather a percentage (controlled by Twitter based on allocations for free developer users).


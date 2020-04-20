# Stream Handlers

Stream handlers resolve incoming data in whatever form, static, batches, other streams, etc. and stream it to a set of given `algorithms`.

## Twitter

I create a wrapper for the incoming Twitter data in `twitter_stream.py`. The `set_filter` method connects to Twitter and begins the streaming channel. We can configure the tweets coming in with `filters`, such as `#USA` or `#travel`.

This class's most important method is `on_data(data)` which is invoked by `Tweepy`'s stream handler on each push of data, which is one tweet. The method parses the raw tweet data and sends individual words extracted from the tweet body to the stream algorithms as tokens.

This class can also send a tweet's hashtags or location data as tokens, depending on the `mode`.

## Shakespeare

The streamer for Shakespeare handles the cleaning and extraction of words from a specified corpus and feeds it into the stream algorithms as tokens.

The cleaning process involves removing all whitespace, punctuation, character names, stage instructions, and other miscallenious symbols.
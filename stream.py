import dotenv
import os
import tweepy
import json

class Stream(tweepy.StreamListener):
    def __init__(self, limit, algorithm):
        dotenv.load_dotenv()
        self.limit = limit
        self.counter = 0
        self.algorithm = algorithm
        self.auth = tweepy.OAuthHandler(os.getenv('TWITTER_KEY'), os.getenv('TWITTER_KEY_SECRET'))
        self.auth.set_access_token(os.getenv('TWITTER_TOKEN'), os.getenv('TWITTER_TOKEN_SECRET'))
        self.stream = tweepy.Stream(self.auth, self)

    def set_filter(self, filters):
        self.stream.filter(track=filters)

    def close(self):
        self.stream.disconnect()

    def on_status(self, status):
            print(status.text)
      
    def on_data(self, data):
        if (self.counter >= self.limit): self.stream.disconnect()
        else:
            tweet = json.loads(data)
            self.counter += 1
            for hashtag in (tweet['entities']['hashtags']):
                self.algorithm.process(hashtag['text'])
            return True

    def on_error(self, status):
        print(status)
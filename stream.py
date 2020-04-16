import dotenv
import os
import tweepy
import json
import re

class Stream(tweepy.StreamListener):
    def __init__(self, limit, algorithm):
        dotenv.load_dotenv()
        self.limit = limit
        self.counter = 0
        self.algorithm = algorithm
        self.mode = 'hashtag'
        self.auth = tweepy.OAuthHandler(os.getenv('TWITTER_KEY'), os.getenv('TWITTER_KEY_SECRET'))
        self.auth.set_access_token(os.getenv('TWITTER_TOKEN'), os.getenv('TWITTER_TOKEN_SECRET'))
        self.stream = tweepy.Stream(self.auth, self)

    def set_filter(self, filters):
        self.stream.filter(track=filters, languages=['en'])

    def set_mode(self, mode):
        self.mode = mode

    def close(self):
        self.stream.disconnect()

    def on_status(self, status):
            print(status.text)
      
    def on_data(self, data):
        if (self.counter >= self.limit): self.stream.disconnect()
        else:
            tweet = json.loads(data)
            if (tweet['lang'] == 'en' and tweet['user']['followers_count'] > 1000):
                self.counter += 1
                if (self.mode is 'hashtag'):
                    for hashtag in (tweet['entities']['hashtags']):
                        self.algorithm.process(hashtag['text'].lower())
                elif (self.mode is 'text'):
                    raw_text = tweet['text'].replace('\n', ' ')
                    for word in re.findall('\w+', raw_text):
                        if (word is not ' ' and re.match('[^0-9]+', word)):
                            self.algorithm.process(word.lower())
                elif (self.mode is 'location'):
                    if (tweet['place']):
                        self.algorithm.process(tweet['place']['name'])
            return True

    def on_error(self, status):
        print(status)
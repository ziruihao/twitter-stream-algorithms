import dotenv
import os
import tweepy
import json
import re

class TwitterStream(tweepy.StreamListener):
    def __init__(self, limit, algorithms):
        dotenv.load_dotenv()
        self.limit = limit
        self.counter = 0
        self.algorithms = algorithms
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
                        print(hashtag['text'].lower())
                        for algorithm in self.algorithms:
                            algorithm.process(hashtag['text'].lower())
                elif (self.mode is 'text'):
                    for word in self.clean_twitter_text(tweet['text']):
                        print(word)
                        for algorithm in self.algorithms:
                            algorithm.process(word)
                elif (self.mode is 'location'):
                    if (tweet['place']):
                        print(tweet['place']['name'])
                        for algorithm in self.algorithms:
                            algorithm.process(tweet['place']['name'])
            return True

    def on_error(self, status):
        print(status)

    def clean_twitter_text(self, text):
        exclude_words = ['rt', ' ']
        extracted_words = []
        text = re.sub(r'[ ]{3}', '', text)
        text = re.sub(r'((http:\/\/|https:\/\/)([\S]+))', '', text).replace('\n', ' ')
        for word in re.findall(r"([a-zA-Z'-]+)", text):
            if (word not in exclude_words):
                extracted_words.append(word.replace("'", '').replace('-', '').lower())
        return extracted_words
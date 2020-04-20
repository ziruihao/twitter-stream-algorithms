import dotenv
import os
import tweepy
import json
import re

class TwitterStream(tweepy.StreamListener):
    def __init__(self, limit, algorithms):
        dotenv.load_dotenv()
        self.limit = limit
        self.algorithms = algorithms
        self.mode = 'body_text'
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
        if (self.limit <= 0): self.stream.disconnect()
        else:
            tweet = json.loads(data)
            if (tweet['id'] is not None):
                if (tweet['lang'] == 'en' and tweet['user']['followers_count'] > 1000):
                    if (self.mode == 'hashtags'):
                        hashtags = tweet['entities']['hashtags']
                        while (self.limit > 0 and len(hashtags) > 0):
                            self.limit += -1
                            hashtag = hashtags.pop(0)
                            print('#' + hashtag['text'].lower())
                            for algorithm in self.algorithms:
                                algorithm.process('#' + hashtag['text'].lower())
                    elif (self.mode == 'body_text'):
                        words = self.clean_twitter_text(tweet['text'])
                        while (self.limit > 0 and len(words) > 0):
                            self.limit += -1
                            word = words.pop(0)
                            print(word)
                            for algorithm in self.algorithms:
                                algorithm.process(word)
                    elif (self.mode == 'locations'):                        
                        if (tweet['place'] and self.limit > 0):
                            self.limit += -1
                            print(tweet['place']['name'])
                            for algorithm in self.algorithms:
                                algorithm.process(tweet['place']['name'])
                    else:
                        raise Exception('Bad Twitter mode')
            else:
                print(tweet)
            return True

    def on_error(self, status):
        print(status)

    def clean_twitter_text(self, text):
        exclude_words = ['rt', ' ', ' ']
        extracted_words = []
        text = re.sub(r'[ ]{3}', '', text)
        text = re.sub(r'((http:\/\/|https:\/\/)([\S]+))', '', text).replace('\n', ' ')
        for word in re.findall(r"([a-zA-Z'-]+)", text):
            if (word not in exclude_words):
                extracted_words.append(word.replace("'", '').replace('-', '').lower())
        return extracted_words
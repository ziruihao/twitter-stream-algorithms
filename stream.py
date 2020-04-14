import dotenv
import os
import tweepy

class Stream(tweepy.StreamListener):
    def __init__(self):
        dotenv.load_dotenv()
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
        print(data)
        return True

    def on_error(self, status):
        print(status)


print('hi')
s = Stream()
s.set_filter(['#covid-19'])


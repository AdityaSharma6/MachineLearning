# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import tweepy
import json

class SentimentAnalysis():
    def __init__(self):
        self.consumer_key = "kQo51pA3BgWEuBnF7I1srqFfM"
        self.consumer_secret = "mk1tY4gvLfh5lfXfECuC2WzWhR6VcRXuNuH7ri91s0EsKPSTPv"
        self.access_token = "1147611631448449027-FNo5Muxaa091HOWuKz2fXNXQPEYJkh"
        self.access_token_secret = "kKJVeI9Wgt1XdnwHYrbsYc2aI4Xt0up2t1WuORrr0HcoX"
    
    def setupTwitter(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)
    
    def findFollowers(self):
        following = self.api.followers("@Kajanth_K", count=200)
        
        for i in range(len(following)):
            print(i)
            print(following[i]._json["name"])
            print(following[i]._json["screen_name"])
            print("\n")
        print(len(following))
    
    def execute(self):
        self.setupTwitter()
        self.findFollowers()

if __name__ == "__main__":
    trial = SentimentAnalysis()
    trial.execute()

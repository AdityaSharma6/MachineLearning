# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import matplotlib as plt 
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

    
    def searchUser(self):
        self.publicTweets = self.api.search("Trump")
        self.sentiment = []
        self.count = {"negative": 0, "positive": 0}

        for i in self.publicTweets:
            print(i.text)
            analysis = TextBlob(i.text)
            value = analysis.sentiment.polarity
            self.sentiment.append(value)
    
            if (value) > 0:
                self.count["positive"] += 1
            elif (value) < 0:
                self.count["negative"] += 1
            else:
                continue


    def returnResults(self):
        average_perspective = sum(self.sentiment) / len(self.sentiment)
        frequent_perspective = self.count

        print(average_perspective)
        print(frequent_perspective)

    
    def execute(self):
        self.setupTwitter()
        self.searchUser()
        self.returnResults()


if __name__ == "__main__":
    trial = SentimentAnalysis()
    trial.execute()
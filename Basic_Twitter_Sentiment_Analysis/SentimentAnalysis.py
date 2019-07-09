# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import tweepy
import json

<<<<<<< HEAD
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
        following = self.api.followers("@Kajanth_K", count=200000)
        
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

'''
=======
consumer_key = "KEY"
consumer_secret = "KEY"
access_token = "TOKEN"
access_token_secret = "TOKEN"
>>>>>>> 2cda0b6336f9e5be931fddafbcab3c0cf4457cd5

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)

publicTweets = API.search("Kamal Khera Lib")
sentiment = []
count = {"negative": 0, "positive": 0}

for i in publicTweets:
    print(i.text)
    analysis = TextBlob(i.text)
    value = analysis.sentiment.polarity
    sentiment.append(value)
    
    if (value) > 0:
        count["positive"] += 1
    elif (value) < 0:
        count["negative"] += 1
    else:
        continue
        

average_perspective = sum(sentiment) / len(sentiment)
frequent_perspective = count

print(average_perspective)
print(frequent_perspective)
<<<<<<< HEAD
'''
=======

    
>>>>>>> 2cda0b6336f9e5be931fddafbcab3c0cf4457cd5

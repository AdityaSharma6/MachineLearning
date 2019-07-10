# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import matplotlib as plt
import tweepy
import json
import Authorization as Authorize


class SentimentAnalysis():

    def setupTwitter(self):
        auth = tweepy.OAuthHandler(Authorize.CONSUMER_KEY, Authorize.CONSUMER_SECRET)
        auth.set_access_token(Authorize.ACCESS_TOKEN, Authorize.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
    
    
    def searchUser(self):
        self.publicTweets = self.api.search(q = "Trump", count = 100)
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
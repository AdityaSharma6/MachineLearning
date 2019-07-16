# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import matplotlib as plt
import tweepy
import json
import Authorization as Authorize
import datetime
import csv
from Visualization import Visualization


class SentimentAnalysis():

    def __init__(self):
        ##################################################################################################
        self.CONSUMER_KEY = Authorize.CONSUMER_KEY
        self.CONSUMER_SECRET = Authorize.CONSUMER_SECRET
        self.ACCESS_TOKEN = Authorize.ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = Authorize.ACCESS_TOKEN_SECRET
        ##################################################################################################
        self.past_date = datetime.date(2019, 7, 5)
        self.next_day = datetime.date(2019, 7, 6)
        self.future_date = datetime.date(2019, 7, 15)
        ##################################################################################################
        self.tweets_list = [["Tweet Description", "Date", "Favorite Count", "Retweet Count", "Sentiment"]]
        self.query = "Logan Paul"
        self.daily_tweet_count = 50
        self.tweet_type = "mixed" #recent, popular, mixed
        ##################################################################################################
        self.sentiment_distribution = {"positive": 0, "negative": 0, "neutral": 0}

    def setupTwitter(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    
    #def getUser(self):
    #    user_object = self.api.get_user("@realDonaldTrump")

    
    def time_difference(self):
        self.difference = (self.future_date - self.past_date).days

    
    def search_tweets(self):
        for i in range(self.difference):
            self.past_date += datetime.timedelta(days = 1)
            self.next_day += datetime.timedelta(days = 1)
            print(self.past_date)
            tweets = tweepy.Cursor(self.api.search, q = self.query, since = self.past_date, until = self.next_day, lang = "en", tweet_mode = "extended", result_type = self.tweet_type).items(self.daily_tweet_count)
            # You can search for hashtags by replacing the Query with your designated Hashtag
            self.analyze_sentiment(tweets)


    def analyze_sentiment(self, tweets):
        for j in tweets:
            analysis = TextBlob(j.full_text)
            value = analysis.sentiment.polarity
            self.sentiment_spread(value)
            self.tweets_list.append([j.full_text, self.past_date, j.favorite_count, j.retweet_count, value])
    

    def sentiment_spread(self, value):
        if value > 0:
            self.sentiment_distribution["positive"] += 1
        elif value < 0:
            self.sentiment_distribution["negative"] += 1
        else:
            self.sentiment_distribution["neutral"] += 1


    def writeCSV(self):
        print("Hi")
        with open('Tweets.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.tweets_list)

    
    def execute(self):
        Visualize = Visualization()
        self.setupTwitter()
        self.time_difference()
        self.search_tweets()
        self.writeCSV()
        Visualize.plot_sentiment(self.sentiment_distribution["positive"], self.sentiment_distribution["negative"], self.sentiment_distribution["neutral"])



if __name__ == "__main__":
    trial = SentimentAnalysis()
    trial.execute()
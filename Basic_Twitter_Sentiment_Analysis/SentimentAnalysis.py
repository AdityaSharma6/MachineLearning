# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import matplotlib as plt
import tweepy
import json
import Authorization as Authorize
import datetime
import csv


class SentimentAnalysis():

    def __init__(self):
        self.CONSUMER_KEY = Authorize.CONSUMER_KEY
        self.CONSUMER_SECRET = Authorize.CONSUMER_SECRET
        self.ACCESS_TOKEN = Authorize.ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = Authorize.ACCESS_TOKEN_SECRET

        self.past_date = datetime.date(2019, 7, 5)
        self.next_day = datetime.date(2019, 7, 6)
        self.future_date = datetime.date(2019, 7, 10)

        self.tweets_list = []

        self.query = "Donald Trump"
        self.daily_tweet_count = 5

    def setupTwitter(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
    
    def getUser(self):
        user_object = self.api.get_user("@realDonaldTrump")
        print(user_object)
    
    def time_difference(self):
        self.difference = (self.future_date - self.past_date).days
    
    def extractTweets(self):
        for i in range(self.difference):
            self.past_date += datetime.timedelta(days = 1)
            self.next_day += datetime.timedelta(days = 1)
            tweets = tweepy.Cursor(self.api.search, q = self.query, since = self.past_date, until = self.next_day, lang = "en").items(self.daily_tweet_count) # You can search for hashtags by replacing the Query with your designated Hashtag
            tweet_counter = 0
            for j in tweets:
                print(tweet_counter)
                tweet_counter += 1
                print(self.past_date)
                self.tweets_list.append([j.text, self.past_date])
    
    def writeCSV(self):
        with open('Tweets.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.tweets_list)

            
        '''
        self.pastDate = datetime.datetime(2019,7,8)
        self.currentDate = datetime.datetime.now()
        self.difference = self.currentDate - self.pastDate
        print(self.difference)
        '''


    '''
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
    '''

    
    def execute(self):
        self.setupTwitter()
        #self.getUser()
        self.time_difference()
        self.extractTweets()
        self.writeCSV()
        #self.searchUser()
        #self.returnResults()


if __name__ == "__main__":
    trial = SentimentAnalysis()
    trial.execute()
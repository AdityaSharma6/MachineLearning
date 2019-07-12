# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import matplotlib as plt
import tweepy
import json
import Authorization as Authorize
import datetime


class SentimentAnalysis():

    def setupTwitter(self):
        auth = tweepy.OAuthHandler(Authorize.CONSUMER_KEY, Authorize.CONSUMER_SECRET)
        auth.set_access_token(Authorize.ACCESS_TOKEN, Authorize.ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
    
    def getUser(self):
        userObject = self.api.get_user("@realDonaldTrump")
        #print(userObject)
    
    def dateTime(self):
        pastDate = datetime.date(2019, 7, 5)
        untilDate = datetime.date(2019, 7, 6)
        currentDate = datetime.date(2019, 7, 10)
        difference = currentDate - pastDate
        print(difference)

        for i in range(difference.days):
            pastDate += datetime.timedelta(days = 1)
            untilDate += datetime.timedelta(days = 1)
            tweets = tweepy.Cursor(self.api.search, q = "Donald Trump", since = pastDate, until = untilDate).items(1000) # You can search for hashtags by replacing the Query with your designated Hashtag
            print("############################# \n")
            k = 0
            for j in tweets:
                print(k)
                k += 1
                print(pastDate)
                print(j.text)
            
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
        self.getUser()
        self.dateTime()
        #self.searchUser()
        #self.returnResults()


if __name__ == "__main__":
    trial = SentimentAnalysis()
    trial.execute()
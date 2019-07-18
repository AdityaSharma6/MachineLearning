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
        self.past_date = datetime.date(2019, 7, 7)
        self.next_day = datetime.date(2019, 7, 8)
        self.future_date = datetime.date(2019, 7, 17)
        ##################################################################################################
        self.tweets_list = [["Tweet Description", "Date", "Favorite Count", "Retweet Count", "Sentiment"]]
        self.query = "Donald Trump"
        self.daily_tweet_count = 10
        self.tweet_type = "popular" #recent, popular, mixed
        ##################################################################################################
        self.sentiment_distribution1 = {"Tweets": {"Pos": 0, "Neg": 0, "Neu": 0},
                                        "Population": {"Pos": 0, "Neg": 0, "Neu": 0} }
    
    def get_pos_pop_sentiment(self):
        return self.sentiment_distribution1["Population"]["Pos"]
    
    def get_neg_pop_sentiment(self):
        return self.sentiment_distribution1["Population"]["Neg"]
    
    def get_neu_pop_sentiment(self):
        return self.sentiment_distribution1["Population"]["Neu"]
    
    def get_pos_tweet_sentiment(self):
        return self.sentiment_distribution1["Tweets"]["Pos"]
    
    def get_neg_tweet_sentiment(self):
        return self.sentiment_distribution1["Tweets"]["Neg"]
    
    def get_neu_tweet_sentiment(self):
        return self.sentiment_distribution1["Tweets"]["Neu"]
    

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
            num_retweets = j.retweet_count
            self.sentiment_spread(value)
            self.population_sentiment_spread(value, num_retweets)
            self.tweets_list.append([j.full_text, self.past_date, j.favorite_count, num_retweets, value])
    

    def sentiment_spread(self, value):
        if value > 0:
            self.sentiment_distribution1["Tweets"]["Pos"] += 1
        elif value < 0:
            self.sentiment_distribution1["Tweets"]["Neg"] += 1
        else:
            self.sentiment_distribution1["Tweets"]["Neu"] += 1
    

    def population_sentiment_spread(self, value, num_retweets):
        if value > 0:
            if num_retweets > 0:
                self.sentiment_distribution1["Population"]["Pos"] += num_retweets
            else:
                self.sentiment_distribution1["Population"]["Pos"] += 1
        elif value < 0:
            if num_retweets > 0:
                self.sentiment_distribution1["Population"]["Neg"] += num_retweets
            else:
                self.sentiment_distribution1["Population"]["Neg"] += 1
        else:
            if num_retweets > 0:
                self.sentiment_distribution1["Population"]["Neu"] += num_retweets
            else:
                self.sentiment_distribution1["Population"]["Neu"] += 1


    def writeCSV(self):
        print("Hi")
        with open('Tweets.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(self.tweets_list)
    
    def visuals(self):
        Visualize = Visualization()
        Visualize.pie_plot_sentiment("Sentiment Spread from Tweets",self.get_pos_tweet_sentiment(), self.get_neg_tweet_sentiment(), self.get_neu_tweet_sentiment())
        Visualize.pie_plot_sentiment("Sentiment Spread from Population", self.get_pos_pop_sentiment(), self.get_neg_pop_sentiment(), self.get_neu_pop_sentiment())
        
        #Visualize.dashboard(plots)

    def execute(self):
        self.setupTwitter()
        self.time_difference()
        self.search_tweets()
        self.writeCSV()
        self.visuals()




if __name__ == "__main__":
    trial = SentimentAnalysis()
    trial.execute()
# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import tweepy

consumer_key = "KEY"
consumer_secret = "KEY"
access_token = "TOKEN"
access_token_secret = "TOKEN"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)

publicTweets = API.search("Trump")
sentiment = []
count = {"negative": 0, "positive": 0}

for i in publicTweets:
    
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

    

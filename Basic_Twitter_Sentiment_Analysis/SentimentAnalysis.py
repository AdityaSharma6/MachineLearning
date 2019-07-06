# API is a gate way that lets users access a server's internal functionality
from textblob import TextBlob
import tweepy

consumer_key = "kQo51pA3BgWEuBnF7I1srqFfM"
consumer_secret = "mk1tY4gvLfh5lfXfECuC2WzWhR6VcRXuNuH7ri91s0EsKPSTPv"
access_token = "1147611631448449027-FNo5Muxaa091HOWuKz2fXNXQPEYJkh"
access_token_secret = "kKJVeI9Wgt1XdnwHYrbsYc2aI4Xt0up2t1WuORrr0HcoX"

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

    
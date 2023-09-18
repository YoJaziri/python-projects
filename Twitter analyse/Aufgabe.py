from textblob import TextBlob
import json
import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_theme()
sns.set_context("paper", rc={"font.size": 4, "axes.titlesize": 10})

with open ("data.json", "r") as file:
    tweets = json.load(file)
    

# print (tweets)


tweets_obama = []

for x in tweets:
    x["topic"].lower()
    if x["topic"] == "obama":
        tweets_obama.append(x)
    
print (tweets_obama)

l = len(tweets_obama)
sum_polarity = 0

for dictt in tweets_obama:
    tweet = dictt["tweet"]
    tweet = TextBlob(tweet)
    polarity = tweet.sentiment.polarity
    
    if polarity > 0.2:
        dictt["sentiment"] = "positive"
    elif polarity < -0.2:
        dictt["sentiment"] = "negative"
    else:
        dictt["sentiment"] = "neutral"
    
    sum_polarity = sum_polarity + polarity
    
sum_polarity = sum_polarity/l
print(f'{sum_polarity: .2f}')

print (tweets_obama)

with open ("data_with_sentiment_obama.json", "w") as file:
    json.dump(tweets_obama, file, indent=4, separators=(", ", ": \n"))


    
sentiments = []

for sentiment in tweets_obama:
    sentiment = sentiment["sentiment"]
    sentiments.append(sentiment)
    
print(sentiments)

sns_plot = sns.histplot(data = sentiments, color ="purple")

sns_plot.figure.savefig("sentiments.png")

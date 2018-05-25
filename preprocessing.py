import re

def preProcessTweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    tweet = re.sub('@[^\s]+','USER',tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip('\'"')
    return tweet

fp = open('exampleTweet.txt', 'r')
line = fp.readline()

while line:
    finalTweet = preProcessTweet(line)
    print finalTweet
    line = fp.readline()
fp.close()
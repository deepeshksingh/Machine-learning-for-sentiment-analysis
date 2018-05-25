import json
#import simplejson as json
import twitter
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = '1355xxxxx'
ACCESS_SECRET = 'xxxxxxxx'
CONSUMER_KEY = '1xxxxxxxNR'
CONSUMER_SECRET = 'xxxxLLU'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_data = TwitterStream(auth=oauth)
twitter_rest_data = Twitter(auth=oauth)
getT = twitter_rest_data.search.tweets(q='#Hillary')

iterator = twitter_data.statuses.sample()
file = open('out.txt', 'w')
tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    pr = json.dumps(tweet, indent=4)
    file.write(pr)
    if tweet_count <= 0:
        break
file.close()

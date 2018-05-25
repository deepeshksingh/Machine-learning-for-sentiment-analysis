import json
#import simplejson as json
import twitter
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = '135594979-CfrCY67ZRN4xQtj543USjuancT74TLp9LAnLCKjL'
ACCESS_SECRET = 'ZifqYlmHuiNdH3UOMKwcNdNDDmYTGOTcR8zjSbIk6Y2GN'
CONSUMER_KEY = '1kRaxsx0WhdcXhorx7II490NR'
CONSUMER_SECRET = '8xqY2bDlrTaP96WF2OtmFIVBEr8L8NgPuoPhTUZ1izKuxKNLLU'

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
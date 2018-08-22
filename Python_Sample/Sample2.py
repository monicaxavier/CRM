#Tutorial2
#install tweepy==3.3.0
#pip install tweepy==3.3.0
#Author: Rick Rejeleene
"""
Created Tweepy Application in Twitter:

Consumer API keys
tuk6J4Wq9RoCNtynuEL0VidD9 (API key)

2hDXUEyLzOQqr1sCNP78RJTkoeNmHUTmTN97WmVeSfj9duFLSg (API secret key)


Access token & access token secret
1031730123534422017-97DiiaDWj3eDN5nYwsISl7CgYRn0uB (Access token)NEW

UWaGQ9kni3Uuio3SyOMFfUpnXNnocsUlmdZ4pV9ufUkh1 (Access token secret)NEW
Read and write (Access level)
"""

#Importing Library
import tweepy
import json
from tweepy import OAuthHandler

consumer_key= 'tuk6J4Wq9RoCNtynuEL0VidD9'
cosumer_secret= '2hDXUEyLzOQqr1sCNP78RJTkoeNmHUTmTN97WmVeSfj9duFLSg'

access_token = '1031730123534422017-97DiiaDWj3eDN5nYwsISl7CgYRn0uB'
access_secret = 'UWaGQ9kni3Uuio3SyOMFfUpnXNnocsUlmdZ4pV9ufUkh1'

auth = OAuthHandler(consumer_key, cosumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    #Process a single status
    print(status.text)

def procss_or_store(tweet):
    print(json.dumps(tweet))

for tweet in tweepy.Cursor(api.user_timeline).items():
    procss_or_store(tweet._json)

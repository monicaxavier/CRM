#Text-Mining, Draft


import tweepy
import json
from tweepy import OAuthHandler

consumer_key='tuk6J4Wq9RoCNtynuEL0VidD9'
consumer_secret = '2hDXUEyLzOQqr1sCNP78RJTkoeNmHUTmTN97WmVeSfj9duFLSg'

access_token = '1031730123534422017-97DiiaDWj3eDN5nYwsISl7CgYRn0uB'
access_secret = 'UWaGQ9kni3Uuio3SyOMFfUpnXNnocsUlmdZ4pV9ufUkh1'

auth =OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)

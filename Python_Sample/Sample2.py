#Tutorial2
#install tweepy==3.3.0
#pip install tweepy==3.3.0
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
from tweepy import OAuthHandler

consumer_key= 'tuk6J4Wq9RoCNtynuEL0VidD9'
cosumer_secret= '2hDXUEyLzOQqr1sCNP78RJTkoeNmHUTmTN97WmVeSfj9duFLSg'

access_token = '1031730123534422017-97DiiaDWj3eDN5nYwsISl7CgYRn0uB'
access_secret = 'UWaGQ9kni3Uuio3SyOMFfUpnXNnocsUlmdZ4pV9ufUkh1'

api = tweepy.API()

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)

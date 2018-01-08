# -*- coding: utf-8 -*-
import os

# to get your own keys:
# 1. go to https://apps.twitter.com/
# 2. fill out form and hit create
# 3. go to app and click "manage keys and access tokens"
# 4. copy into your bashrc

# TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
# TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']

TWITTER_API_KEY = 'uQwTXiYtKP116c6d4oXwqhPhv'
TWITTER_API_SECRET = 'FCFEkdMcFNeABT0NExmYUndp8Iji6HiUSPwn4EcRGQfQeTSaWj'


# Twitter allows 160 queries per 15 minute window
TWEETS_PER_SEARCH = 100
RATE_LIMIT = 1  # requests every 15 minutes, max is 450 for app twitter api
RATE_LIMIT_WINDOW = 900  # 15 minutes * 60

# referenced in cron.py
#REQUESTS_PER_WINDOW  = 
#RATE_LIMIT_WINDOW  = 
TWEETS_PER_REQUEST = 100
#RATE_DECAY =


DATA_PATH = 'data'
QUERIES = [u'ομπαμα%2BOR%2BΟμπαμα%2BOR%2Bομπάμα%2BOR%2BΟμπάμα', u'#ομπαμα%2BOR%2B#Ομπαμα%2BOR%2B#ομπάμα%2BOR%2B#Ομπάμα']
#QUERIES = [u'Ομπαμα']

PARAMS = {
        'q': '',
        'lang': 'el',
        'count': str(TWEETS_PER_REQUEST),
        'result_type': 'recent',
    }

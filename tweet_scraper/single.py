# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
#from builtins import str

import json
import os
import datetime
import gzip
import sys
from collections import defaultdict

from twython import Twython
from settings import DATA_PATH, TWITTER_API_KEY, TWITTER_API_SECRET, TWEETS_PER_REQUEST, QUERIES, PARAMS


id_counter = defaultdict(tuple)

def get_twitter():
    twitter = Twython(TWITTER_API_KEY, TWITTER_API_SECRET, oauth_version=2)
    return Twython(TWITTER_API_KEY, access_token=twitter.obtain_access_token())


def get_tweets(query, twitter=None, **kwargs):
    query = query
    twitter = twitter or get_twitter()

    params = PARAMS
    params.update(kwargs)

    # check to see if this is the first pass ; if not, use the max_id, since_id args to traverse the timeline
    
    if id_counter['query]:
        # top is the oldest tweet of the previous request
        top = id_counter['query][-1] - 1
        try:
            resp = twitter.search(max_id=top, **params)
        except TwythonError as e:
            print('Oops! : {}'.format(e.msg))
    else:
        try:
            resp = twitter.search(**params)
        except TwythonError as e:
            print('Oops! : {}'.format(e.msg))
            
    # rate_limit_remaining = twitter.get_lastfunction_header('x-rate-limit-remaining')
    # rate_limit_reset = twitter.get_lastfunction_header('x-rate-limit-reset')

    # add/update id_counter with a record of the most recent & oldest id of the tweets in this request for this query   
    since_id = resp['statuses'][0]['id'] 
    max_id = resp['statuses'][-1]['id']
    id_counter['query'] = (since_id, max_id) 

    return resp['statuses']


def save_tweets(tweets, query='', verbosity=1):
    now = datetime.datetime.utcnow()
    filename = os.path.join(DATA_PATH, '{}-{}.json'.format(query, now.isoformat()).replace(':', '_'))
    with open(filename, 'a') as f:
        f.write(json.dumps(tweets, indent=2))
    if verbosity > 0:
        print('{} tweets written to {}'.format(len(tweets), filename))


if __name__ == '__main__':
    #args, _ = process_argv(sys.argv)
    twitter = get_twitter()
    for q in QUERIES: #args
        tweets = get_tweets(query=q, twitter=twitter)
        save_tweets(tweets, q)

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
#from builtins import str

import json
import os
import time
import datetime
import sys
from collections import defaultdict

from twython import Twython
from settings import DATA_PATH, TWITTER_API_KEY, TWITTER_API_SECRET, TWEETS_PER_REQUEST, QUERIES, PARAMS

QUERIES = QUERIES
id_counter = defaultdict(tuple)
# update id_counter for testing
#id_counter[u'ομπαμα%2BOR%2BΟμπαμα%2BOR%2Bομπάμα%2BOR%2BΟμπάμα'] = (0,798753910483628032)
#id_counter[u'#ομπαμα%2BOR%2B#Ομπαμα%2BOR%2B#ομπάμα%2BOR%2B#Ομπάμα'] = (0,797095512331665408)

def get_twitter():
    '''calls the twitter api obtains token for oath 2.0 use
    returns twython object'''
    twitter = Twython(TWITTER_API_KEY, TWITTER_API_SECRET, oauth_version=2)
    return Twython(TWITTER_API_KEY, access_token=twitter.obtain_access_token())


def get_tweets(query, twitter=None, **kwargs):
    query = query
    twitter = twitter or get_twitter()

    params = PARAMS
    params.update({'q':query})

    # check to see if this is the first pass ; if not, use the max_id, since_id args to traverse the timeline
    
    if id_counter[query]:
        # the oldest tweet of the previous request ; decrease by one so as to not store again the same tweet
        oldest = id_counter[query][-1] - 1
        try:
            resp = twitter.search(max_id=oldest, **params)
        # check you are within the ratelimit
        except TwythonRateLimitError as e:
            print('Oops! : {}'.format(e.msg))
            wait = int(twitter.get_lastfunction_header('x-rate-limit-reset')) - int(time.time())
            time.sleep(wait)
        # catch any api errors    
        except TwythonError as e:
            print('Oops! : {}'.format(e.msg))
            
    else:
        id_counter[query] = (0,0)
        try:
            resp = twitter.search(**params)
        except TwythonRateLimitError as e:
            print('Oops! : {}'.format(e.msg))
            wait = int(twitter.get_lastfunction_header('x-rate-limit-reset')) - int(time.time())
            time.sleep(wait)
            
        except TwythonError as e:
            print('Oops! : {}'.format(e.msg))
            

    #check that the max_id has changed ; if not, you have captured all available tweets
    #remove the query term from the query list and return 0(false) to be caught in a while in __main__ 
    # also, if the relevant tweets are exhausted, resp['statuses'] will be empty
    if (not resp['statuses']) or id_counter[query][-1] == resp['statuses'][-1]['id'] :
        print('All available tweets concerning query {} have been captured'.format(query))
        QUERIES.remove(query)
        return 0, 0
        #raise SystemExit('It failed!')
    # add/update id_counter with a record of the most recent & oldest id of the tweets in this request for this query   
    else:
        since_id = resp['statuses'][0]['id'] 
        max_id = resp['statuses'][-1]['id']
        id_counter[query] = (since_id, max_id) 

    return resp['statuses'], max_id


def save_tweets(tweets, query='', max_id=0, verbosity=1):
    # get current datetime
    now = datetime.datetime.utcnow()
    # construct json pathfilename
    jsonfile = os.path.join(DATA_PATH, '{}-{}.json'.format(query, now.isoformat()).replace(':', '_'))
    # open and write tweets to json
    with open(jsonfile, 'a') as f:
        f.write(json.dumps(tweets, indent=2))
    #the code below is for stop/resume of the script , e.g. using cron to launch the script
    #idfile = os.path.join(DATA_PATH, '{}.txt'.format(query))
    #with open(idfile, 'wt') as f:
    #    text_id = '{}-{}'.format(query, max_id)
    #    f.write(text_id.encode('utf8'))
    # below is debug
    if verbosity > 0:
        print('{} tweets written to {}'.format(len(tweets), jsonfile))
        print('Requests remaining : {}'.format(twitter.get_lastfunction_header('x-rate-limit-remaining')))
        print('{} - oldest ID : {}'.format(query, max_id))



if __name__ == '__main__':
    #args, _ = process_argv(sys.argv)
    twitter = get_twitter()
    # check query list contains terms
    while QUERIES:
        # requests limit(oath2.0): 450/15min = 1 req/2secs
        counter = 450
        while counter:
            # iterate through each query search term
            for q in QUERIES:
                # retrieve tweetwss and the oldest id 
                tweets, max_id = get_tweets(query=q, twitter=twitter)
                # if retrieval sucessful
                if tweets:
                    # save tweets
                    save_tweets(tweets, q, max_id)
                # if near the request limit    
                if counter == 1 :
                    # force sleep script until twitter limit counter resets
                    wait = int(twitter.get_lastfunction_header('x-rate-limit-reset')) - int(time.time())
                    time.sleep(wait)
                    # reinitialize counter
                    counter = 450
                # if not near the request limit
                else :
                    # decrease counter by 1
                    counter -= 1
                    # force sleep of 2 secs
                    time.sleep(2)

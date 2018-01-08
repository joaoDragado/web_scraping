### tweet_scrapper

- Capture tweets about a query / group of related queries by :

---

### Algorithm


1. make a call to the twitter api for a get_tweet , max num of tweets is 100/150?

2. fetch the id of the first(most recent) tweet **{since_id}** & the id of the last (oldest) tweet **{max_id}**, and save it in :
    - a textfile, if the script will run/stop via cron.

    - in a defaultdict, if the scirpt will run continously e.g.
    **{'query':('since_id','max_id')}**


3. **max_id** is inclusive, so should be decreased by 1 , either on store or when specifed as a functiong argument

3. repeat the call to get_tweet, every time setting the last_id as a boundary

### Notes 

- update the `settings.py` file  with the query of interest. 


- Rate Limit for oath2.0 : 450 requests per 15 min = 900 sec aka 1 request every 2 secs


1. In each call store the tweets in a json file 

2. Set counter to requests limit

3. Loop 450 times 

```python
counter = 450

while counter:
    call get tweet
    save tweet
    sleep 2s
    if counter == 1 :
        wait = int(twitter.get_lastfunction_header('x-rate-limit-reset') - time.time())
        time.sleep(wait)
        counter = 450
    else :
        counter -= 1
        time.sleep(2)
```

---

test queries :

    ομπαμα%2BOR%2BΟμπαμα%2BOR%2Bομπάμα%2BOR%2BΟμπάμα
    ομπαμα%2BOR%2B#Ομπαμα%2BOR%2B#ομπάμα%2BOR%2B#Ομπάμα


---

### optional - use bash to automate the script 

```bash
# to issue a single request for 100 tweets (max allowed by twitter) and save it as json
python -m tweetget.single

# to request max tweets RATE_LIMIT times
python -m tweetget.core

# to hit Twitter's API every 15 minutes, run this in screen/tmux
python -m tweetget.cron
```

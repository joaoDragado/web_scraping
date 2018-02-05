import requests, bs4, csv

movies = []

# most voted films in 50 years

'''
# explicit url
# 1. by votes desc
url = 'http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012'
# 2. by rating
http://www.imdb.com/search/title?start=1&title_type=feature&year=1950,2012&sort=user_rating,desc
http://www.imdb.com/search/title?start=1&title_type=feature&year=1950,2012&sort=user_rating,desc
# 3. by US gross box office
http://www.imdb.com/search/title?start=1&title_type=feature&year=1950,2012&sort=boxoffice_gross_us,desc
'''

# base URL with GET dictionary
url = 'http://www.imdb.com/search/title'
params = dict(sort='num_votes,desc', start=1, title_type='feature', year='1950,2012')

r = requests.get(url, params=params)
try:
    r.raise_for_status()
except Exception as exc:
    print 'There was a problem : {}'.format(exc)

bs = bs4.BeautifulSoup(r.text, 'html.parser')
for movie in bs.findAll('td', 'title'):
    title = movie.find('a').contents[0]
    genres = movie.find('span', 'genre').findAll('a')
    genres = [g.contents[0] for g in genres]
    runtime = movie.find('span', 'runtime').contents[0]
    rating = movie.find('span', 'value').contents[0]
    print title, genres, runtime, rating
    entry = [title, genres, runtime, rating]
    tops.append(entry)

# write the full list into a csv file 
with open('movies.csv', mode='at', encoding='utf-8') as f:
    #f.write('\n'.join(tops))
    #json.dump(tops, f)   
    writer = csv.writer(f)
    writer.writerows(tops)

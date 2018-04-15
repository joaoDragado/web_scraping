import requests, bs4, re, json

'''
Script to iterate through all the pages of UserName's reddit history, and retrieve all imgur links.
 There is an issue with  retrieving the last reddit message of each page, which is important because that info is (needs to be) contained in the next page url. 

 The following is a rough draft of the solution ; needs reworking..

r.json()['data']['after']  

posts = r.json()['data']['children']

posts[0]['data']['url']

next_page = 'https://www.reddit.com/user/UserName/submitted/?count=25&after=t3_6potj5'

'''
reddit_pages = [
'https://www.reddit.com/user/UserName/submitted/',
'https://www.reddit.com/user/UserName/submitted/?count=25&after=t3_6potj5',
'https://www.reddit.com/user/UserName/submitted/?count=50&after=t3_66ardj ',
'https://www.reddit.com/user/UserName/submitted/?count=75&after=t3_5wi1go ',
'https://www.reddit.com/user/UserName/submitted/?count=100&after=t3_5u3x6o',
'https://www.reddit.com/user/UserName/submitted/?count=125&after=t3_5rzb5r'
]


pages = []
images = []

#after = 1
#url = 'https://www.reddit.com/user/UserName/submitted/'

for url in reddit_pages:
    r = requests.get(url , headers={'user-agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(r.content, 'html5lib')
    imgur_links = [ x['href'] for x in soup.findAll('a', {'class':"title may-blank outbound"}) ]
    pages.extend(imgur_links)
#after = r.json()['data']['after']
#url = 'https://www.reddit.com/user/UserName/submitted/?count=25&after='+after


for url in pages:
    if url.startswith('https://url_of_non_pertinent_Site'):
        continue
    r = requests.get(url)
    try:
        r.raise_for_status()
    except Exception as exc:
        print('There was a problem : {}'.format(exc))
    
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    origin = [x['src'] for x in soup.findAll('source') ]
    images.extend(origin)    

with open('urls.txt', mode='at', encoding='utf-8') as myfile:
    myfile.write('\n'.join(images))

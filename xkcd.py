''' Scraping images from simple tumblr-like site.
XKCD is a popular geek webcomic. http://xkcd.com/ 
The front web page has a Prev button that guides the user back through prior comics.'''

'''    ##  Script Requirements  ##

1. Loads the XKCD home page.
2. Saves the comic image on that page.
3. Follows the Previous Comic link.
4. Repeats until it reaches the first comic.
'''

'''    ##  Implementation  ##

1. Download pages with the requests module.
2. Find the URL of the comic image for a page using Beautiful Soup.
3. Download & save comic image locally with iter_content() .
4. Find the URL of the Previous Comic link, and repeat.
'''

'''     ## Targeted HTML Emements   ##

1. The URL of the comic's image file is on the href attribute of an <img> element. That <img> element is inside a <div id="comic"> element.
2. The Prev button has a rel HTML attribute with value=prev .
3. The 1st comic's Prev button links to the http://xkcd.com/# URL, indocating that there are no more previous pages, that is we have reached the 1st page.
 
'''


import requests, os, bs4
# starting url
base_url = 'http://xkcd.com'

# store comics in /xkcd ; exist_ok param since py3.2
try:
    os.makedirs('xkcd')
except OSError as e:
    print e
                 
    
# initialize url
url = base_url

while not url.endswith('#'):
    # 1. Download the page.
    print 'Downlaoding page {}...'.format(url)
    r = requests.get(url)
    try:
        r.raise_for_status()
    except Exception as exc:
        print 'There was a problem : {}'.format(exc)
        
    #create BeuatifulSoup object, store web page
    soup = bs4.BeautifulSoup(r.text)
    
    # 2. Find the URL of the comic image.
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print 'Could not find image element.'
    else:
        comic_url = comic_elem[0].get('src')
        # 3a. Download the image.
        print 'Downloading image {}'.format(comic_url)
        # need to add the 'http:' prefix to the image source link
        r = requests.get('http:' + comic_url)
        try:
            r.raise_for_status()
        except Exception as exc:
            print 'There was a problem : {}'.format(exc)
        
        # 3b. Save the image to ./xkcd
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:
            for tranche in r.iter_content(10000):
                image_file.write(tranche)
    
    # 4. Get the Prev button's url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = base_url + prev_link.get('href')
        

print 'All Done!!'    

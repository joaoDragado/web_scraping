import requests, bs4

'''
script that scrapes the links to all the images on the nameOfSite tumblr, and :
- saves it to a text file,
- downloads the image in a folder named "images".

Saving the links before downloading is advisable, to check and filter out avatar & non-pertinent images.

'''

images = []
posts = []

base_url = 'https://nameOfSite.tumblr.com/page/{}'

for i in range(50):

    url = base_url.format(i)
    r = requests.get(url)
    try:
        r.raise_for_status()
    except Exception as exc:
        print('There was a problem : {}'.format(exc))

    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    origin = [x['src'] for x in soup.findAll('img') ]
    images.extend(origin)

    content = [x.text.strip() for x in soup.findAll('div', class_='post-body')]
    posts.extend(content)

### Posts (text)

'''Save the content of each post to a text file
Uncomment below code to activate
'''

#with open('nameOfSite_posts.txt', mode='at', encoding='utf-8') as myfile:
#    myfile.write('\n'.join(posts))



### Images

'''Option 1 - Save the web links to the images to a text file
Uncomment below code to activate
'''

#with open('nameOfSite.txt', mode='at', encoding='utf-8') as myfile:
#    myfile.write('\n'.join(images))


'''Option 2 - Save the images to ./images
Uncomment below code to activate
'''

#for img_url in images:
#    img = img_url.split('/')[-1]
#    with open(os.path.join('images', os.path.basename(img)), 'wb') as image_file:
#        for tranche in r.iter_content(10000):
#            image_file.write(tranche)

import requests, bs4

r = requests.get('http://www.bubble.com')
try:
    r.raise_for_status()
except Exception as exc:
    print 'There was a problem : {}'.format(exc)

'''bs4.BeautifulSoup() function is called on a string containing the HTML it will parse. The bs4.BeautifulSoup() function returns a BeautifulSoup object.
'''

bs_object = bs4.BeautifulSoup(r.text)

'''Can also load a local HTML file by passing a File object to bs4.BeautifulSoup() 
'''

example_file = open('example.html')
example_Soup = bs4.BeautifulSoup(example_file)

'''Retrieve a web page element from a BeautifulSoup object by calling the select() method and passing a string of a CSS selector for the element. Selectors are like regular expressions.

The select() method returns a list of Tag objects, which is how Beautiful Soup represents an HTML element. The list will contain 1 Tag  object for every match in the BeautifulSoup object’s HTML. Tag values can be passed to the str() function to show the HTML tags they represent.

Tag values also have an attrs attribute that shows all the HTML attributes of the tag as a dictionary.
'''

exampleSoup = bs4.BeautifulSoup(exampleFile.read())

# select elements with attribute id 'author'
elems = exampleSoup.select('#author')
elems[0].getText() # outputs the viewed string
str(elems[0]) # outputs the entire HTML element
elems[0].attrs # outputs the attribute value i.e. 'author'

# select all <p> elements

pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()




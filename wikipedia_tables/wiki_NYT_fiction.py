import requests, bs4, re, json, csv

tops = []

# base url for all NYT bs lists
base_url = "https://en.wikipedia.org/wiki/The_New_York_Times_Fiction_Best_Sellers_of_{}"

for i in range(1993,2018): 
    # convert year to string for later
    year = str(i)
    #fetch the web page
    r = requests.get(base_url.format(i))
    try:
        r.raise_for_status()
    except Exception as exc:
        print('There was a problem : {}'.format(exc))
    # store page as bs4 object
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    
    # extract the table containing the info
    table = soup.find("table", { "class" : "wikitable" })
    
    # iterate over each row
    for row in table.findAll("tr"):
	
        cells = row.findAll("td")
        #For each "tr", assign each "td" to a variable.
        # rows with book data have 3 cells
        
        if len(cells) == 3:
            month = cells[0].find(text=True)
            title = cells[1].find(text=True)
            author = cells[2].find(text=True)
            #entry = ','.join([year, month, title, author])
            entry = [year, month, title, author]
            # add the book entry to our master list
            tops.append(entry)

# write the full list into a csv file 
with open('wiki_NYT.csv', mode='at', encoding='utf-8') as f:
    #f.write('\n'.join(tops))
    #json.dump(tops, f)   
    writer = csv.writer(f)
    writer.writerows(tops)


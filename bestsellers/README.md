# Obtaining NYT bestsellers dataset
---
Register with Goodreads and the New York Times Books APIs and obtain your keys ,a dn store them in a ```keys.json`` file. 
Extra :Update ```keys.local`` with those keys

```bash
cp keys.local keys.json
```
---
## Step 1. Scrap NY Times Bestsellers Lists Info

Scrape each year's NYT bestseller list (fiction - nonfiction) from Wikipedia.

Initial pages are :
 - [Lists of The New York Times Fiction Best Sellers](https://en.wikipedia.org/wiki/Lists_of_The_New_York_Times_Fiction_Best_Sellers) 
 - [Lists of The New York Times Non-Fiction Best Sellers](https://en.wikipedia.org/wiki/Lists_of_The_New_York_Times_Non-Fiction_Best_Sellers)

Save the data in ```wiki_NYT.csv``` , ```wiki_NYT_nonfiction.csv```

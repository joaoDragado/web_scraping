# Obtaining NYT bestsellers dataset
---
### Preliminaries :

- Register with Goodreads and the New York Times Books APIs and obtain your keys ,and store them in a ```keys.json`` file. 
> Extra :Update ```keys.local`` with those keys.

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

---
> The following steps should be executed for each book genre (fiction / non-fiction). Note that the non-fiction is considerably shorter due to lack of data & considerable repetition (same books stay on the list for long periods).
--- 
## Step 2. Get book and author id from Goodreads

Run ```get-goodreads-ids.py```. The output will be saved in ```fiction_goodreads-ids.csv```

Set start and end year in intervals, so as to identify missing IDs, which will need to be entered manually at the end of the script's  run.


---
## Repository Contents

```bash
.
├── apis
│   ├── goodreads_api.pdf
│   └── nyt_API.pdf
├── get-goodreads-ids.py
├── README.md
├── wiki_NYT_fiction.py
└── wiki_NYT_nonfiction.py

1 directory, 6 files

```
---

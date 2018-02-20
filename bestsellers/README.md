# Obtaining NYT bestsellers dataset
---
## Repository Contents

```bash
.
├── apis
│   ├── goodreads_api.pdf
│   └── nyt_API.pdf
├── get-book-info.py
├── get-goodreads-ids.py
├── README.md
├── wiki_NYT_fiction.py
└── wiki_NYT_nonfiction.py

1 directory, 7 files
```
---

### Preliminaries :

- Register with Goodreads and the New York Times Books APIs and obtain your keys ,and store them in a ```keys.json`` file. 
> Extra :Update ```keys.local`` with those keys.

```bash
cp keys.local keys.json
```
---
## Step 1. Scrap NY Times Bestsellers Lists Info

Scrape each year's NYT bestseller list (fiction - nonfiction) from Wikipedia, by running :
- ```wiki_NYT_fiction.py```, 
- ```wiki_NYT_nonfiction.py```

Initial pages are :
 - [Lists of The New York Times Fiction Best Sellers](https://en.wikipedia.org/wiki/Lists_of_The_New_York_Times_Fiction_Best_Sellers) 
 - [Lists of The New York Times Non-Fiction Best Sellers](https://en.wikipedia.org/wiki/Lists_of_The_New_York_Times_Non-Fiction_Best_Sellers)

Save the data in ```NYT_fiction.csv``` , ```NYT_nonfiction.csv```

---
> The following steps should be executed for each book genre (fiction / non-fiction). Note that the non-fiction is considerably shorter due to lack of data & considerable repetition (same books stay on the list for long periods).
--- 
## Step 2. Get book and author id from Goodreads

Run ```get-goodreads-ids.py```. The output will be saved in ```fiction_goodreads-ids.csv```

Set start and end year in intervals, so as to identify missing IDs, which will need to be entered manually at the end of the script's  run.

---

Using ```book_id``` from the previous step, run ```get-book-info.py```. This generates ```book-info.csv```. 

> Fields extracted :
**'title', 'image_url', 'publisher', 'num_pages', 'link', 'isbn', 'isbn13', 'publication_year', 'genres' .**

The **genres** field is populated by the top 5 genres associated with each book ; the full list of genres was obtained from the goodreads site. 
 
Set start and end year as in Step 2.

- Missing values (especially numOfPages) need to be entered manually.

> Careful examination of results is needed (via ISBNs), with respect to correct edition ; this will determine the year of 1st publication. When uncertain, we choose the 1st hardback edition.
---

  

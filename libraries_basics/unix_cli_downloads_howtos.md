### Remove all non-pertinent files from any images folder.
- run from inside the folder or in the parent of all associated folders. 

```bash
find . -type f -regex '.*\.\(html\|dat\|txt\|xml\|svg\|eot\|ttf\|woff\|css\|ico\)' -delete
```
---

### Keep all files with names matching the regex pattern in folder ; delete all other files. 
- run from inside the folder or in the parent of all associated folders. 

```bash
find . -not -name "*1000.jpg" -not -name "*1000.gif -not -type d" -delete
```
---

### Make a list of all image files in the folder and copy it in a text file.

```bash
ls | grep ".[gif|png|jpg]"$ > images.txt
```
---


### Filter out files with .jpg extension from in.txt and create new text file with only the rest.

```bash
sed '/.jpg$/d' in.txt > out.txt
```
---


### Filter out duplicates and create new file with only the unique items.

```bash
sort file.txt | uniq > file_sorted.txt
```
---

### Given file in.txt, select all lines that contain the keyword and create/append to new file with only those lines.

```bash
grep -r "keyword"  ./in.txt >> out.txt
```

---

### Given a file with urls (each row a url), iterate through all the liknks and download them in the present folder.

```bash
while read URL; do wget $URL; done < file.txt
```

---








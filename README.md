Simple web-scraper for finnish news sites "yle.fi" and "iltalehti.fi"
20-30 or so of the most recent stories will be scraped from either site
The data will be compiled to json format and one news story will contain the publication date, the title for the story and the actual text.

Build:
install required libraries with -pip install -r requirements.txt

Run:
Run with -python src/main/main.py 

-You will be asked which news site you want to scrape the data from
-Write into the prompt either "yle" or "iltalehti" 
-Next you will be asked to name the file that the json data will be stored into
-File will appear in the root of the project

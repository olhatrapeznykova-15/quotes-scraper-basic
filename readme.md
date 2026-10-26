Quote Scraper (basic)
A small Python script that downloads quotes from
quotes.toscrape.com (a website built for
scraping practice) and saves them to a text file and a CSV file.

What it does:
Downloads up to 3 pages of quotes from the site's JSON API
Pulls out the quote text, author and tags
Saves them to `quotes_report.txt` and `quotes.csv`

How to run:
Python 3 only, nothing to install:
    python scraper.py

Change `NUMBER_OF_PAGES` at the top of `scraper.py` to download more (the site has 10 pages).
What I practised
Loops and `if` statements
Lists and dictionaries
Downloading data with `urllib`
Reading JSON with `json`
`try / except` for errors
Writing text and CSV files

About AI use:
I used an AI assistant while building this project to work faster and to find ways to make my code cleaner. 
I reviewed the code until I understood each part and tested it.
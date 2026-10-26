# Quote Scraper - basic version
# Downloads quotes from quotes.toscrape.com (a website made for scraping practice)
# and saves them to a text file and a CSV file.

import csv                    # lets us write a CSV (spreadsheet) file
import json                   # lets us turn the website's text into a Python dictionary
import time                   # lets us pause between requests
import urllib.request         # lets us download a web page

# ---------- Settings (change these to experiment) ----------
URL = "https://quotes.toscrape.com/api/quotes?page="   # the page number goes at the end
NUMBER_OF_PAGES = 3                                    # how many pages to download

all_quotes = []   # an empty list - we will add every quote here

print("Starting...")

# Loop through the page numbers: 1, 2, 3 ...
for page_number in range(1, NUMBER_OF_PAGES + 1):
    print("Downloading page", page_number)

    try:
        # Download the page. timeout=10 means "give up after 10 seconds"
        response = urllib.request.urlopen(URL + str(page_number), timeout=10)
        text = response.read().decode("utf-8")      # bytes -> normal text
        data = json.loads(text)                     # text -> Python dictionary
    except Exception as error:
        # If anything goes wrong (no internet, website down), show the problem and stop
        print("Could not download the page:", error)
        break

    # data["quotes"] is a list. Each item in it is one quote (a dictionary).
    for item in data["quotes"]:
        quote_text = item["text"]
        author = item["author"]["name"]             # the author is a dictionary inside the quote
        tags = ", ".join(item["tags"])              # turn the list of tags into one text

        # Save this quote as a small dictionary and add it to our big list
        all_quotes.append({"text": quote_text, "author": author, "tags": tags})

    # "has_next" tells us if there is another page. If not, stop the loop.
    if data["has_next"] == False:
        break

    time.sleep(1)

# Optional
wanted_author = input("Author to keep (press Enter to keep everyone): ").strip()

if wanted_author != "":
    filtered_quotes = []                         # a new, empty list
    for quote in all_quotes:                     # look at every quote we downloaded
        if wanted_author.lower() in quote["author"].lower():
            filtered_quotes.append(quote)        # keep it
    all_quotes = filtered_quotes                 # replace the big list with the small one


print("Total quotes collected:", len(all_quotes))

if len(all_quotes) == 0:
    print("No quotes found.")
else:
    # Save to a text file
    with open("quotes_report.txt", "w", encoding="utf-8") as file:
        for quote in all_quotes:
            file.write("Quote:  " + quote["text"] + "\n")
            file.write("Author: " + quote["author"] + "\n")
            file.write("Tags:   " + quote["tags"] + "\n")
            file.write("-" * 30 + "\n")

    # Save to a CSV file
    with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=["text", "author", "tags"])
        writer.writeheader()                 # first row: the column names
        writer.writerows(all_quotes)         # then one row per quote

    print("Saved quotes_report.txt and quotes.csv")

print("Finished.")

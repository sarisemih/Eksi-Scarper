from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys
import concurrent.futures

## define the function to scrape a page
def scrape_page(page_link):
    r = requests.get(page_link, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    entries_block = soup.find("ul", {"id": "entry-item-list"}).find_all("li")
    page_entries = []
    for entry in entries_block:
        username = entry.get("data-author")
        content = entry.find("div", {"class": "content"}).text
        date = entry.find("a", {"class": "entry-date permalink"}).text
        page_entries.append((username, content, date))
    
    return page_entries

if __name__ == "__main__":
    
    mainLink = sys.argv[1] # get the link from the command line
    mainLink = mainLink.split("?")[0] # if the link has a query string, remove it
    
    headers = {
        "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31")
    }

    # get the page count
    r = requests.get(mainLink, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    pageCount = int(soup.find("div", {"class": "pager"}).get("data-pagecount")) + 1

    # create an empty list to store all entries
    all_entries = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        page_links = [mainLink + "?p=" + str(i) for i in range(1, pageCount)]
        results = executor.map(scrape_page, page_links)
        for result in results:
            all_entries.extend(result)

    EntryDF = pd.DataFrame(all_entries, columns=["username", "entry", "date"])
    EntryDF.set_index("username", inplace=True)
    
    EntryDF.to_csv("entries.csv", encoding="utf-8-sig")
    


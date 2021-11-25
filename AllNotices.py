from bs4 import BeautifulSoup
from FetchNotices import getNoticesFromBaseUrl
import json
from requests import get
import time
import threading

baseurl = 'https://nitdgp.ac.in/p/noticesnitd/general-2'

AllNotices = {}


def getCategoryNotice(category_url, category_name):
    print(f"fetching notices for url: {category_url}")
    start = time.time()
    category_notice = {
        category_name: getNoticesFromBaseUrl(category_url)
    }
    AllNotices.update(category_notice)
    end = time.time()
    print(
        f"Completed fetching notices for url: {category_url} in {int((end-start)//60)} minutes & {int((end-start)%60)} seconds...")


print("Getting Categories")
try:
    response = get(baseurl)
    print("got categories!")
except:
    print("Couldn't find categories!!!")


soup = BeautifulSoup(response.text, 'html.parser')

required_div = soup.find("div", {"id": "leftmenubar"})

categories = required_div.find_all('a', href=True)

jobs = []

for category in categories:

    url = category['href']

    name = category.get_text()

    thread = threading.Thread(target=getCategoryNotice, args=(url, name))

    thread.daemon = True

    jobs.append(thread)


for j in jobs:
    j.start()

for j in jobs:
    j.join()

with open("response.json", 'w') as outfile:
    json.dump(AllNotices, outfile, indent=2)

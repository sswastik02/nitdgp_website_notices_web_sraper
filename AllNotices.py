from bs4 import BeautifulSoup
from FetchNotices import FetchNotices
import json
from requests import get
import time
import threading





class AllNotices:

    def __init__(self,baseurl):
        self.AllNotices = {}
        self.baseurl = baseurl
        self.driver()

    def getCategoryNotice(self,category_url, category_name):
        print(f"Started fetching notices for url: {category_url}")
        start = time.time()
        fetchNotices = FetchNotices(category_url)
        category_notice = {
            category_name: fetchNotices.retAllNotices()
        }
        self.AllNotices.update(category_notice)
        end = time.time()
        print(
            f"Completed fetching {category_name} notices from url: {category_url} in {int((end-start)//60)} minutes & {int((end-start)%60)} seconds...")


    def driver(self):
        print("Getting Categories............")
        try:
            response = get(self.baseurl)
            print("Got categories!")
        except:
            print("Couldn't find categories!!!")


        soup = BeautifulSoup(response.text, 'html.parser')

        required_div = soup.find("div", {"id": "leftmenubar"})

        categories = required_div.find_all('a', href=True)

        jobs = []

        for category in categories:

            url = category['href']

            name = category.get_text()

            thread = threading.Thread(target=self.getCategoryNotice, args=(url, name))

            thread.daemon = True

            jobs.append(thread)


        for j in jobs:
            j.start()

        for j in jobs:
            j.join()

        with open("response.json", 'w') as outfile:
            json.dump(self.AllNotices, outfile, indent=2)

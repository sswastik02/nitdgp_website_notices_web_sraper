from bs4 import BeautifulSoup
from requests import get


def getDate(Date):
    dmy = Date.get_text().strip().replace('\n', '').replace('\t', '')
    date, month, year = '', '', ''
    for i in dmy:
        if i.isnumeric():
            if month == '':
                date += i
            else:
                year += i
        else:
            month += i
    return {"date": date, "month": month, "year": year}


def getLinkInfo(Link):
    link_href = Link['href']
    link_title = Link['title']
    return {"link_title": link_title, "link_href": link_href}


page = get("https://nitdgp.ac.in")

soup = BeautifulSoup(page.content, 'html.parser')


carousel = soup.find_all('div', class_='carousel-inner')
events_group = carousel[1].find_all('ul')
for events_group_iterator in events_group:
    event_group = events_group_iterator.find_all('li')
    for event in event_group:
        dateTag = event.find('div', class_='date')
        linkTag = event.find('a', href=True)
        print(getDate(dateTag))
        print(getLinkInfo(linkTag))

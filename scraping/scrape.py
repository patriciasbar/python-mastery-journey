import pprint as pp
import requests  #downloads html data
import pprint
from bs4 import BeautifulSoup #allows to use html and grab different data

COUNT_VOTES = 100

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

res2  = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

mega_link = links + links2
mega_subtext = subtext + subtext2

def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[i].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", "").replace(" point", ""))
            if points > COUNT_VOTES:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(mega_link, mega_subtext))






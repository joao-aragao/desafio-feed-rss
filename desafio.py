import requests
from bs4 import BeautifulSoup


def getUrl(url):
    resp = requests.get(url)

    soup = BeautifulSoup(resp.content, features='xml')

    return print(soup.prettify())


getUrl('https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')

# Lib necessárias para rodar script
import requests
import json
from bs4 import BeautifulSoup


def getUrl(url):
    resp = requests.get(url)

    soup = BeautifulSoup(resp.content, features='xml')

    itens = soup.findAll("item")

    lista_itens = []

    for item in itens:
        dic_item = {}
        dic_item['site:'] = item.link.text
        dic_item['data:'] = item.pubDate.text[1].split()
        lista_itens.append(dic_item)

    lista_itens = json.dumps(lista_itens)

    return print(lista_itens)


# getUrl('https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')
# getUrl('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
# getUrl('https://g1.globo.com/rss/g1/carros/')

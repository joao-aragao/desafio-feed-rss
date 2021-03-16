# Lib necessárias para rodar script
import requests
import json
from bs4 import BeautifulSoup


# Cria uma função para receber a url do xml
def getUrl(url):
    # Fazendo request
    resp = requests.get(url)

    # Verificar request
    if resp.status_code == 200:
        print('Ok')
    else:
        print('Error')
        exit()

    # Chamando construtor
    soup = BeautifulSoup(resp.content, features='xml')

    # Procurando tag tem e atribuindo a variável
    itens = soup.findAll("item")

    # crio lista para receber tudo que achou de item
    lista_itens = []

    # crio for para listar itens:
    for item in itens:
        # Seto um dicionário para adicionar os itens exibidos a lista_itens
        dic_item = {}
        # Pegando link
        dic_item['site:'] = item.link.text
        # Pegando Data de publicação
        dic_item['data:'] = item.pubDate.text
        # Adicionando itens a lista
        lista_itens.append(dic_item)

    # Função json.dumps para transformar lista em formato json
    lista_itens = json.dumps(lista_itens)

    print(lista_itens)


# Chamando função getUrl
getUrl('https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')
# getUrl('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
# getUrl('https://g1.globo.com/rss/g1/carros/')

# Desafio 02 - AvantSec 

## Introdução

- A aplicação foi construída em python 3 
- Bibliotecas utilizadas
  - requests
  - BeautifulSoup

## Instação das Bibliotecas

Com o pip já instalado 
```
pip install -r requirements.txt
```

## Iniciando o Script

Chame a função getUrl e passe como paramêtro para função o link do seu xml
```
getUrl('https://g1.globo.com/rss/g1/carros/')
```


## Explicação 

Crio uma função para receber a url, depois faço requisição se estiver ok continua, se não fecha o script.
Chamo o construtor da lib do bs atribuindo variável soup, chamo função findall e passo como paramêtro a tag que quero no xml
Crio lista para receber resultado da função findall
Crio For para listar itens, junto crio dicionário para fazer append para lista externa
Depois chamo função json.dumps para transformar lista em um json

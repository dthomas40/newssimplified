import sys
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet as wn
from newspaper import Article
import requests
from bs4 import BeautifulSoup

class Scraper():
    def find_link():
        page = requests.get('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US%3Aen')
        bSoup = BeautifulSoup(page.content, 'html.parser')
        links_list = bSoup.find_all('a')
        links = []
        for link in links_list:
            if 'href' in link.attrs:
                links.append(str(link.attrs['href']) + '\n')

        i = 0
        art1_url = links[i]
        while art1_url[:10] != './articles':
            art1_url = links[i]
            i += 1

        art2_url = art1_url

        while art1_url == art2_url or './publications' in art2_url or './topics' in art2_url or './stories' in art2_url:
            art2_url = links[i]
            i += 1

        art1_url = 'https://news.google.com/' + art1_url[2:]
        art2_url = 'https://news.google.com/' + art2_url[2:]

        article1 = scrape(art1_url)
        article2 = scrape(art2_url)

        return (article1,article2)

    def scrape(art_url):
        article = Article(art_url)
        article.download()
        article.parse()
        article.nlp()
        return article
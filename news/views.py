import requests
from django.shortcuts import render
from bs4 import BeautifulSoup as BSoup

#Web Scraper

#TOI

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[2:-13]  #To remove footers

toi_news = []

for toi in toi_headings:
    toi_news.append(toi.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news})

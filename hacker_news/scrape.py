''' scrape hacker news site'''
import requests
from bs4 import BeautifulSoup
import pprint

def main(pages, limiter):
    links = []
    subtext = []
    for p in range(1, int(pages)):
        url = 'https://news.ycombinator.com/news?p=' + str(p)
        soup_obj = read_html_page(url)
        links = links + soup_obj.select('.titleline')
        subtext = subtext + soup_obj.select('.subtext')
    return create_custom_news(links, subtext, limiter)
        
def read_html_page(url):  
    res = requests.get(url, timeout=3) 
    return BeautifulSoup(res.text,'html.parser') 

def create_custom_news(links,subtext, limiter):
    ''' scrapes hacker news and returns list of new article with > 99 points'''
    news = []
    for idx, item in enumerate(links):
        title = item.getText()        
        href = item.get('href', item)
        val = subtext[idx].select('.score')
        if len(val):
            val =  int(val[0].getText().replace(' points','').replace(' point',''))
            if val > limiter:
                news.append({'title':title, 'link': href, 'points': val})
    return sort_by_votes(news)

def sort_by_votes(news):
    return sorted(news, key = lambda k:k['points'])

pprint.pprint(main(2, 99))
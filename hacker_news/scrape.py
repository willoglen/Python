''' scrape hacker news site'''
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news') # add more ?p=x
soup_obj = BeautifulSoup(res.text,'html.parser')
links = soup_obj.select('.titleline')
subtext = soup_obj.select('.subtext')

def create_custom_news(links,subtext):
    ''' scrapes hacker news and returns list of new article with > 99 points'''
    news = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        val = subtext[idx].select('.score')
        if len(val):
            val =  int(val[0].getText().replace(' points','').replace(' point',''))
            if val > 99:
                news.append({'title':title, 'link': href, 'points': val})
    return sort_by_votes(news)

def sort_by_votes(news):
    return sorted(news, key = lambda k:k['points'])

pprint.pprint(create_custom_news(links, subtext))
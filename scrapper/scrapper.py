__author__ = 'jmeireles'

import bs4
import requests
import re
import urllib


class Scrapper():

    t = "http://playpanda.net/embed.php?w=600&h=438&vid=at/nw/terra_formars_-_09.mp4"

    def __init__(self, url):
        self.url = url
        self.title = ""
        pass

    def scrap(self):
        response = requests.get(self.url)

        soup = bs4.BeautifulSoup(response.text)
        title = soup.find('title')

        self.title = title.text.split(' - ')[0]

        links = soup.find_all('iframe')
        urls = []
        for link in links:
            urls.append(self.get_link(link.get('src')))

        return urls

    def get_title(self):
        return self.title

    def get_link(self, url):

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        javascript = soup.find_all('script')

        urls = []

        for script in javascript:

            text = script.get_text()
            url = re.search('(?P<url>https?://[^\s"]+)', str(text))

            if url is None:
                continue

            urls.append(urllib.unquote(url.group("url")).decode('utf8'))

        return urls

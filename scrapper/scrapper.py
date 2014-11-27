__author__ = 'jmeireles'

import bs4
import requests
import re
import urllib
import os

class Scrapper():

    t = "http://playpanda.net/embed.php?w=600&h=438&vid=at/nw/terra_formars_-_09.mp4"
    valid_extensions = ['.mp4', '.flv']

    def __init__(self, url):
        self.url = url
        self.title = ""

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

            url = urllib.unquote(url.group("url")).decode('utf8')

            name, ext = os.path.splitext(url)

            if not ext[len(filter(ext.startswith, self.valid_extensions+[''])[0]):]:
                continue

            urls.append(url)

        return urls

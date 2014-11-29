__author__ = 'jmeireles'

import bs4
import requests
import re
import urllib
import os
from gui.helper import Helper
import json
from tld import get_tld


class Scrapper():

    valid_extensions = ['.mp4', '.flv']

    def __init__(self, url):
        self.url = url
        self.domain = get_tld(self.url)
        self.title = ""
        stream = open(Helper.get_resource_path("test.json"), 'r')
        self.scrap_info = json.load(stream)

    def scrap(self):
        response = requests.get(self.url)

        soup = bs4.BeautifulSoup(response.text)
        title = soup.find(self.scrap_info[self.domain]['episode']['title']['tag'])

        self.title = title.text.split(self.scrap_info[self.domain]['episode']['title']['split'])[0]

        links = soup.find_all('iframe')

        urls = []

        for link in links:
            li = self.get_link(link.get( self.scrap_info[self.domain]['episode']['video']['tag']['iframe']['attr']))
            if li:
                urls.append(li)

        return urls

    def get_title(self):
        return self.title

    def get_link(self, url):

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        javascript = soup.find_all(self.scrap_info[self.domain]['episode']['video']['tag']['iframe']['sub']['tag'])

        urls = []

        for script in javascript:

            text = script.get_text()
            regex = urllib.unquote(self.scrap_info[self.domain]['episode']['video']['tag']['iframe']['sub']['regex'])
            url = re.search(regex, str(text))

            if url is None:
                continue

            url = urllib.unquote(url.group("url")).decode('utf8')

            name, ext = os.path.splitext(url)

            if not ext[len(filter(ext.startswith, self.valid_extensions+[''])[0]):]:
                continue

            urls.append(url)

        return urls

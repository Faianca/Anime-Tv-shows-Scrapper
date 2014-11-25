__author__ = 'jmeireles'

import bs4
import requests
import re
import urllib


class Scrapper():

    url = ""

    def __init__(self):
        pass

    def scrap(self):
        response = requests.get("http://playpanda.net/embed.php?w=600&h=438&vid=at/nw/terra_formars_-_09.mp4")

        soup = bs4.BeautifulSoup(response.text)
        links = soup.select('body')

        file = re.search('(?P<url>https?://[^\s"]+)', str(links)).group("url")
        return urllib.unquote(file).decode('utf8')
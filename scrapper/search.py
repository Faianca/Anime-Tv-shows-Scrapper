__author__ = 'jmeireles'
import bs4
import requests
import re
import urllib
import os


class Href():
    img = ""
    title = ""
    link = ""


class Search():

    domain = "http://www.animehere.com"
    href = []

    def __init__(self):
        pass

    def search(self, keyword):
        self.href = []
        url = "http://www.animehere.com/search.html?keyword="+keyword
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        links = soup.select("body > section.content.cfix > section.maincontent > section > ul > li")

        if links:
            for link in links:
                hrefs = link.select('> a')
                if hrefs:
                    for href in hrefs:
                        new_href = Href()
                        new_href.title = href.get('title')
                        new_href.link = self.domain+href.get('href')
                        new_href.img = self.domain+href.select('> img')[0].get('src')
                        self.href.append(new_href)

        return self.href
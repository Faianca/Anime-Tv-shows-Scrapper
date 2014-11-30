__title__ = 'Episode Scrapper'
__version__ = '0.1'
__author__ = 'Jorge Meireles'
__copyright__ = 'Copyright (c) 2013-2014 Jorge Meireles'
__license__ = "MIT"

import bs4
import requests
import re
import urllib
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Episode():

    valid_extensions = ['.mp4', '.flv']
    bad_domains = ['facebook']
    title = ''
    links = []

    def __init__(self, scrapper_json):
        self.scrapper_json = scrapper_json

    def scrap(self, url):
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        self._get_title(soup)
        self._get_links(soup)

    def get(self):

        return {
            'title': self.title,
            'links': self.links[0]
        }

    def _get_title(self, soup):
        title = soup.find(self.scrapper_json['title']['tag'])

        if 'split' in self.scrapper_json['title']:
            self.title = title.text.split(self.scrapper_json['title']['split'])[0]

    def _get_links(self, soup):
        urls = []

        video_scrap_info = self.scrapper_json['video']
        tag = video_scrap_info['tag']
        key = tag.keys()
        values = tag.values()[0]
        links = soup.find_all(key)

        if links:
            for link in links:
                link_url = link.get(values['attr'])

                bad_flag = False
                for bad_domain in self.bad_domains:
                    if bad_domain in link_url:
                        bad_flag = True
                        break

                if bad_flag:
                    continue

                if 'sub' in values:
                    li = self._get_link(link_url, values['sub'])
                    if li:
                        self.links.append(li)

    def _get_link(self, url, sub):

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        javascript = soup.find_all(sub['tag'])
        urls = []

        for script in javascript:
            text = script.get_text()
            regex = urllib.unquote(sub['regex'])
            url = re.search(regex, str(text))

            if url is None:
                continue

            url = urllib.unquote(url.group("url")).decode('utf8')

            name, ext = os.path.splitext(url)

            if not ext[len(filter(ext.startswith, self.valid_extensions+[''])[0]):]:
                continue

            urls.append(url)

        return urls


class EpisodeSimple():

    valid_extensions = ['.mp4', '.flv']
    bad_domains = ['facebook']
    title = ''
    links = []

    def __init__(self, scrapper_json):
        self.scrapper_json = scrapper_json

    def scrap(self, url):
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)
        self._get_title(soup)
        self._get_links(soup)

    def get(self):

        return {
            'title': self.title,
            'links': self.links
        }

    def _get_title(self, soup):
        title = soup.find(self.scrapper_json['title']['tag'])

        if 'split' in self.scrapper_json['title']:
            self.title = title.text.split(self.scrapper_json['title']['split'])[0]

    def _get_links(self, soup):
        urls = []

        video_scrap_info = self.scrapper_json['video']
        tag = video_scrap_info['tag']
        key = tag.keys()
        values = tag.values()[0]
        links = soup.find_all(key)

        if links:
            for link in links:
                link_url = link.get(values['attr'])

                if link_url:

                    bad_flag = False
                    for bad_domain in self.bad_domains:
                        if bad_domain in link_url:
                            bad_flag = True
                            break

                    if bad_flag:
                        continue

                    self.links.append(str(unicode(link_url)))

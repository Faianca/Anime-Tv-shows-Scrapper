__title__ = 'Episode Scrapper'
__version__ = '0.1'
__author__ = 'Jorge Meireles'
__copyright__ = 'Copyright (c) 2013-2014 Jorge Meireles'
__license__ = "MIT"

import bs4
import requests
from videospider import Spider


class Episode():

    valid_extensions = ['.mp4', '.flv']
    bad_domains = ['facebook', 'ad_iframe', 'showads']
    title = ''
    links = []

    def __init__(self, scrapper_json):
        self.scrapper_json = scrapper_json
        self.spider = Spider()

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

        video_scrap_info = self.scrapper_json['video']
        tag = video_scrap_info['tag']
        key = tag.keys()
        values = tag.values()[0]
        links = soup.find_all(key)

        if links:
            for link in links:
                link_url = link.get(values['attr'])

                if self.bad_url(link_url):
                    continue

                self.links.append(self.spider.fetch(link_url))

    def bad_url(self, url):
        bad_flag = False
        for bad_domain in self.bad_domains:
            if bad_domain in url:
                bad_flag = True
                break

        return bad_flag

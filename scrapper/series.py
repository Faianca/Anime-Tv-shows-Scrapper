__title__ = 'Series Scrapper'
__version__ = '0.1'
__author__ = 'Jorge Meireles'
__copyright__ = 'Copyright (c) 2013-2014 Jorge Meireles'
__license__ = "MIT"

__all__ = ['EpisodeLink', 'Series']

import bs4
import requests
from tld import get_tld


class EpisodeLink():
    href = ''
    title = ''

    def __init__(self):
        pass


class Series():

    title = ''
    description = ''
    image = ''
    genre = []
    stars = ''
    date = ''
    episodes = []
    external_domain = ''

    def __init__(self, scrapper_json):

        self.scrapper_json = scrapper_json

    def scrap(self, url):
        self.external_domain = "http://"+get_tld(url)
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text)

        self._description(soup)
        self._get_episodes(soup)

    def get(self):

        return {
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'genre': self.genre,
            'stars': self.stars,
            'date': self.date,
            'episodes': self.episodes
        }

    def _description(self, soup):

        try:
            self.title = soup.select(self.scrapper_json['title'])[0].text
            self.stars = soup.select(self.scrapper_json['stars'])[0].text
            self.description = soup.select(self.scrapper_json['description'])[0].text
            self.image = self.external_domain + soup.select(self.scrapper_json['image'])[0].get('src')
            self.date = soup.select(self.scrapper_json['date'])[0].text
            genres_tmp = soup.select(self.scrapper_json['genres']['css_path'])

            for genre in genres_tmp:
                self.genre.append(genre.text)

        except Exception:
            print Exception
            raise

    def _get_episodes(self, soup):

        links = soup.select(self.scrapper_json['episodes']['css_path'])
        links.reverse()

        if links:
            for link in links:
                episode_link = EpisodeLink()
                episode_link.href = self.external_domain + link.get('href')
                episode_link.title = link.text
                self.episodes.append(episode_link)

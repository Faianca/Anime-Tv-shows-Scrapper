__author__ = 'jmeireles'
import bs4
import requests
import re
import urllib
import os
from gui.helper import Helper
import json
from tld import get_tld
from javascript_scrapper import JavascriptHelper
import dryscrape
from gui.browser import Browser
import gtk
import gobject


class Scrapper():

    valid_extensions = ['.mp4', '.flv']
    bad_domains = ['facebook']

    def __init__(self):
        self.domain = ""
        self.title = ""
        self.links = ""
        stream = open(Helper.get_resource_path("test.json"), 'r')
        self.scrap_info = json.load(stream)

    def episode(self, url):
        self.domain = get_tld(url)

        if self.domain not in self.scrap_info:
            raise Exception(self.domain+" is not supported.")

        session = dryscrape.Session()
        session.visit(url)
        response = session.body()
        #response = requests.get(url)
        #soup = bs4.BeautifulSoup(response.text)

        soup = bs4.BeautifulSoup(response)

        self.title = self._get_title(soup)
        self.links = self._get_links(soup)

    def get_title(self):
        return self.title

    def get_links(self):
        return self.links

    def _get_title(self, soup):
        title = soup.find(self.scrap_info[self.domain]['episode']['title']['tag'])

        if 'split' in self.scrap_info[self.domain]['episode']['title']:
            title = title.text.split(self.scrap_info[self.domain]['episode']['title']['split'])[0]

        return title

    def _get_links(self, soup):
        urls = []

        video_scrap_info = self.scrap_info[self.domain]['episode']['video']
        tag = video_scrap_info['tag']
        key = tag.keys()
        values = tag.values()[0]
        links = soup.find_all(key)

        all_links = []

        hrefs = soup.find_all('a')
        for href in hrefs:

            onclick = href.get('onclick')
            if onclick:
                if onclick.startswith('addHit'):
                    group = re.findall("(?:'(?P<url>[A-Za-z0-9_]+)')", onclick)
                    all_links.append(group)


        payload = {'var1': all_links[0][0], 'var2': all_links[0][1]}
        response_post = requests.post("http://anime-exceed.com/minor.php", data=payload)
        test = bs4.BeautifulSoup(response_post.text).find('iframe').get('src')

        source = requests.get(test)

        iframes = bs4.BeautifulSoup(source.text).find_all('iframe')

        valid_link = ''
        for iframe in iframes:
            if "anime-exceed" in iframe.get('src'):
                continue

            valid_link = iframe.get('src')

        return valid_link

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

                print link_url
                if 'sub' in values:
                    li = self._get_link(link_url, values['sub'])
                    if li:
                        urls.append(li)

        return urls

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

gobject.threads_init()
scrapper = Scrapper()
scrapper.episode("http://anime-exceed.com/akame-ga-kill-episode-21-subbed-dubbed/")
title = scrapper.get_title()

# browser = Browser()
# win = gtk.Window()
# win.set_position(gtk.WIN_POS_CENTER)
# win.set_size_request(800, 600)
# win.set_icon_from_file(Helper.get_resource_path("icon.png"))
# win.set_resizable(False)
# title = scrapper.get_title()
# win.set_title(title)
# browser.open(scrapper.get_links())
# win.add(browser.get())
# win.show_all()
#
# gtk.main()
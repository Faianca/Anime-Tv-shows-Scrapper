#!/usr/bin/env python
__author__ = 'jmeireles'

import gtk
import gobject
from gui.gtk_c import Gtk
from gui.browser import Browser
from scrapper.scrapper import Scrapper
from gui.html import Html
from gui.helper import Helper


class Main():

    def __init__(self):
        self.window = Gtk()
        self.browser = Browser()
        self.scrapper = Scrapper("http://www.animehere.com/highschool-of-the-dead-episode-12.html")
        self.html = Html()

    def start(self):
        urls = self.scrapper.scrap()

        link = None

        for url in urls:
            if Helper.exists(url[0]):
                link = url[0]
                break

        movie = self.html.open(link)

        self.browser.open(movie)
        self.window.resize(800, 600)
        self.window.set_resizable(False)
        self.window.set_title(self.scrapper.get_title())
        self.window.add(self.browser.get())
        self.window.show_all()

    
gobject.threads_init()
main = Main()
main.start()
gtk.main()
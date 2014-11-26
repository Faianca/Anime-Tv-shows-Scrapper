#!/usr/bin/env python
import gtk
import gobject
from gui.gtk_c import Gtk
from gui.browser import Browser
from scrapper.scrapper import Scrapper
from gui.html import Html


class Main():

    def __init__(self):
        self.window = Gtk()
        self.browser = Browser()
        self.scrapper = Scrapper("http://www.animehere.com/hitsugi-no-chaika-avenging-battle-episode-8.html")
        self.html = Html()

    def start(self):
        urls = self.scrapper.scrap()
        movie = self.html.open(urls[1][0])

        self.browser.open(movie)
        self.window.resize(800, 600)
        self.window.set_resizable(False)
        self.window.set_title("Terra Formars 09")
        self.window.add(self.browser.get())
        self.window.show_all()


gobject.threads_init()
main = Main()
main.start()
gtk.main()
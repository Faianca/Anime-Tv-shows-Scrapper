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
        self.box = ''
        self.scrapper = ''
        self.window = Gtk()
        self.mainWindow = Gtk()
        self.browser = Browser()
        self.html = Html()


    def clicked(self, widget):
        self.mainWindow.hide()
        self.start(self.box.get_text())

    def go(self):
        self.mainWindow.resize(800, 600)
        self.mainWindow.set_resizable(False)
        self.mainWindow.set_title("Faianca Entertainment")

        button = gtk.Button("go")
        button.connect("clicked", self.clicked)

        self.box = gtk.Entry()

        hbox = gtk.HBox()
        hbox.set_size_request(200,200)
        hbox.pack_start(self.box)
        hbox.pack_start(button)

        self.mainWindow.add(hbox)

        self.mainWindow.show_all()

    def start(self, url):
        self.scrapper = Scrapper(url)
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
main.go()
#main.start("http://www.animehere.com/psychopass-2-episode-3.html")
gtk.main()
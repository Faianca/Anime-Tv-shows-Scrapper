#!/usr/bin/env python
import gtk
import gobject
from gui.gtk_c import Gtk
from gui.browser import Browser
from scrapper.scrapper import Scrapper


class Main():

    def __init__(self):
        self.window = Gtk()
        self.browser = Browser()
        self.scrapper = Scrapper()

    def start(self):
        self.browser.open(self.scrapper.scrap())
        self.window.add(self.browser.get())
        self.window.show_all()

gobject.threads_init()
main = Main()
main.start()
gtk.main()
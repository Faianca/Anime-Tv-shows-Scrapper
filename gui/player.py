__author__ = 'jmeireles'
from gi.repository import Gtk
from helper import Helper
from browser import Browser
from html import Html


class Player2():

    def __init__(self):
        self.browser = Browser()
        self.html = Html()
        self.win = Gtk.Window()
        #self.win.set_position(Gtk.WIN_POS_CENTER)
        self.win.set_icon_from_file(Helper.get_resource_path("icon.png"))
        self.win.set_resizable(False)

    def set_title(self, title):
        self.win.set_title(title)

    def open(self, url):
        movie = self.html.create(url)
        if self.win.get_window() is None:
            self.browser.open(movie)
            browser = self.browser.get()
            self.win.add(browser)
        else:
            self.browser.open(movie)

        self.win.show_all()

class Player():

    def __init__(self):
        self.browser = Browser()
        self.html = Html()
        self.win = Gtk.Window()
        #self.win.set_position(Gtk.WIN_POS_CENTER)
        self.win.set_icon_from_file(Helper.get_resource_path("icon.png"))
        self.win.set_resizable(False)

    def set_title(self, title):
        self.win.set_title(title)

    def open(self, url):
        movie = self.html.create(url)
        if self.win.get_window() is None:
            self.browser.open(movie)
            browser = self.browser.get()
            self.win.add(browser)
        else:
            self.browser.open(movie)

        self.win.show_all()




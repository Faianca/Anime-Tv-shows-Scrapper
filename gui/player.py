__author__ = 'jmeireles'
import gtk
from helper import Helper
from browser import Browser
from html import Html


class Player():

    def __init__(self):
        self.browser = Browser()
        self.html = Html()
        self.win = gtk.Window()
        self.win.set_position(gtk.WIN_POS_CENTER)
        self.win.set_size_request(800, 600)
        self.win.set_icon_from_file(Helper.get_resource_path("icon.png"))
        self.win.set_resizable(False)

    def set_title(self, title):
        self.win.set_title(title)

    def open(self, url):
        movie = self.html.create(url)
        self.browser.open(movie)
        self.win.add(self.browser.get())
        self.win.show_all()
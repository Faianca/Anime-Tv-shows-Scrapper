__author__ = 'jmeireles'
from gi.repository import Gtk, Gdk
from helper import Helper
from browser import Browser
from html import Html
import os


class Player:

    extra_links = []

    def __init__(self):

        self.browser = Browser()
        self.html = Html()
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(os.getcwd(), '../gui/src/player.glade'))
        self.win = self.builder.get_object('mainWindow')
        self.win.set_size_request(860, 600)

        self.win.set_resizable(False)
        self.mainBox = self.builder.get_object('mainBox')
        self.mainBox.set_size_request(800, 600)
        self.left = self.builder.get_object('left')
        self.win.connect("window-state-event", self.on_window_state_event)
        self.win.connect('destroy', Gtk.main_quit)
        self.win.connect('delete-event', Gtk.main_quit)
        self.win.set_icon_from_file(Helper.get_resource_path("icon.png"))
        self.left_handler()

    def on_window_state_event(self, widget, event, data=None):
        mask = Gdk.WindowState.FULLSCREEN
        fullscreen = widget.get_window().get_state() & mask == mask

        if fullscreen:
            self.mainBox.set_homogeneous(True)
        else:
            self.mainBox.set_homogeneous(False)

    def set_title(self, title):
        self.win.set_title(title)

    def set_links(self, links):
        self.extra_links = links[:]

    def left_handler(self):
        browser = self.browser.get()
        self.left.add(browser)

    def link_clicked(self, widget, link):
        self.browser.open(link)

    def open(self, url):
        movie = self.html.create(url)
        self.browser.open(movie)
        self.win.show_all()






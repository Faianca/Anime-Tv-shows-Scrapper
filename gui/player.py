__author__ = 'jmeireles'
from gi.repository import Gtk, Gdk
from helper import Helper
from browser import Browser
from html import Html
import os, sys


class Player2():

    extra_links = []

    def __init__(self):
        self.browser = Browser()
        self.html = Html()
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(os.getcwd(), 'player.glade'))
        self.win = self.builder.get_object('mainWindow')
        self.win.set_size_request(860, 600)

        self.win.set_resizable(False)
        self.mainBox = self.builder.get_object('mainBox')
        self.mainBox.set_size_request(800, 600)

        self.right = self.builder.get_object('right')
        self.left = self.builder.get_object('left')
        self.left.set_size_request(802, 604)

        browser = self.browser.get()
        self.win.add(browser)

        self.win.connect("window-state-event", self.on_window_state_event)
        self.win.set_icon_from_file(Helper.get_resource_path("icon.png"))
        self.left_handler()

    def on_window_state_event(self, widget, event, data=None):
        mask = Gdk.WindowState.FULLSCREEN
        fullscreen = widget.get_window().get_state() & mask == mask

        if fullscreen:
            self.right.set_visible(False)
            self.mainBox.set_homogeneous(True)
        else:
            self.right.set_visible(True)
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

    def right_handler(self):
        box = Gtk.VBox()
        i = 1

        for episod in self.extra_links:
            name = "Link "+str(i)
            button = Gtk.Button(name)
            box.pack_start(button, False, False, 0)
            button.connect('clicked', self.link_clicked, episod)
            i += 1

        box.show()
        self.right.add(box)

    def open(self, url):
        movie = self.html.create_simple(url)
        self.browser.open(movie)
        self.right_handler()
        self.win.show_all()


class Player():

    def __init__(self):
        self.browser = Browser()
        self.html = Html()
        self.win = Gtk.Window()
        #self.win.set_position(Gtk.WIN_POS_CENTER)
        #self.win.set_icon_from_file(Helper.get_resource_path("icon.png"))
        self.win.set_resizable(False)

    def set_title(self, title):
        self.win.set_title(title)

    def open(self, url):
        movie = self.html.create_simple(url)

        if self.win.get_window() is None:
            self.browser.open(movie)
            browser = self.browser.get()
            self.win.add(browser)
        else:
            self.browser.open(movie)

        self.win.show_all()




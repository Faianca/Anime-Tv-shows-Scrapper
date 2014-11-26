__author__ = 'jmeireles'

import gtk
from helper import Helper

class Gtk():

    def __init__(self):
        self.win = gtk.Window()
        self.win.set_position(gtk.WIN_POS_CENTER)
        self.win.set_size_request(400, 400)
        self.win.connect("destroy", gtk.main_quit)
        self.win.set_icon_from_file(Helper.get_resource_path("icon.png"))

    def set_resizable(self, flag):
        self.win.set_resizable(flag)

    def set_border(self, flag):
        self.win.set_decorated(flag)

    def set_title(self, title):
        self.win.set_title(title)

    def resize(self, width, height):
        self.win.set_size_request(width, height)

    def add(self, object):
        self.win.add(object)

    def show_all(self):
        self.win.show_all()


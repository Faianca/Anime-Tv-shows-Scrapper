__author__ = 'jmeireles'

import gtk


class Gtk():

    def __init__(self):
        self.win = gtk.Window()
        self.win.resize(400, 400)

    def resize(self, height, width):
        self.win.resize(height, width)

    def add(self, object):
        self.win.add(object)

    def show_all(self):
        self.win.show_all()


#!/usr/bin/env python
__author__ = 'jmeireles'

from gi.repository import Gtk


class Main():

    def __init__(self):
        gladefile = "gui.glade"
        builder = Gtk.Builder()
        builder.add_from_file(gladefile)
        window = builder.get_object("MainWindow")
        window.show()

main = Main()
Gtk.main()
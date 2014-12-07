__author__ = 'jmeireles'
import os, sys
import urllib2
from gi.repository import Gtk, Gdk
from scrapper.scrapper import Scrapper
from scrapper.search import Search
from helpers.drawers import Grid
from gi.repository.GdkPixbuf import Pixbuf
from gi.repository import Gio
from gui.player import Player2

scrapper = Scrapper()
player = Player2()
builder = Gtk.Builder()
builder.add_from_file(os.path.join(os.getcwd(), 'player.glade'))
window = builder.get_object('mainWindow')
links = scrapper.get_episode("http://www.animehere.com/terra-formars-episode-11.html")['links']
print links

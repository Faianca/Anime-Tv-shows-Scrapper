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
import json

scrapper = Scrapper()
player = Player2()
links = scrapper.get_episode("http://www.animehere.com/terra-formars-episode-11.html")
t = json.dumps(links)
print t
link = links['links'][0]

player.set_title('dsaad')
player.open(link[0])

Gtk.main()
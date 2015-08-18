from gi.repository import Gtk, Gdk
from gui.player import Player
from videospider import Spider

Gdk.threads_enter()

player = Player()

spider = Spider()
link = spider.fetch("http://vodlocker.com/embed-5fw744toleey-650x370.html")
#player.set_title("etas")
player.open(link)

Gtk.main()
Gdk.threads_leave()

from gi.repository import Gtk, Gdk
from gui.player import Player
from videospider import Spider

Gdk.threads_enter()

player = Player()

spider = Spider()
link = spider.fetch("http://videowing.me/embed?w=600&h=438&video=ongoing/the_japan_animator_expo_-_26.mp4")
#player.set_title("etas")
player.open(link)

Gtk.main()
Gdk.threads_leave()

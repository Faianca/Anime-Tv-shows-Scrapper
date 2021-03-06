__author__ = 'jmeireles'

from gi.repository import Gtk
from scrapper.scrapper import Scrapper
from gui.player import Player

def main():
    url = "http://www.animehere.com/psychopass-2-episode-9.html"
    player = Player()
    scrapper = Scrapper()
    test = scrapper.get_episode(url)

    link = test['links'][0]
    player.set_title(test['title'])
    player.set_links(test['links'])
    player.open(link)


if __name__ == '__main__':
    main()
    Gtk.main()
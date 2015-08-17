import os, sys
import urllib2
from gi.repository import Gtk, Gdk
from scrapper.scrapper import Scrapper
from scrapper.search import Search
from helpers.drawers import Grid
from gi.repository.GdkPixbuf import Pixbuf
from gi.repository import Gio
from gui.player import Player

css = """
#faiancaWindow {
   /* background-color: #ffffff; */
}

"""


class UI:

    grid = ""

    def __init__(self):
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        self.player = Player()
        self.scrapper = Scrapper()
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(os.getcwd(), 'gui/src/gui2.glade'))
        self.window = self.builder.get_object('mainWindow')
        self.window.set_title("Anime Tv Scrapper")
        self.window.set_size_request(860, 600)
        self.entry = self.builder.get_object('searchinput')

        self.back_button = self.builder.get_object('toolbutton1')
        self.back_button.connect("clicked", self.go_back)

        self.left_pane = self.builder.get_object('box2')
        self.links_frame = self.builder.get_object('scrolledwindow1')
        self.mainBox = self.builder.get_object('box1')
        self.test_frame = self.builder.get_object('viewport1')
        self.grid_helper = Grid()

        self.grid = self.grid_helper.get()
        self.links_frame.add(self.grid)

        self.entry.connect("activate", self.on_searchinput_activate)
        self.window.connect("window-state-event", self.on_window_state_event)
        self.window.connect('destroy', Gtk.main_quit)
        self.window.connect('delete-event', Gtk.main_quit)
        self.window.show_all()

    def on_searchinput_activate(self, widget):
        self.open()

    def on_window_state_event(self, widget, event, data=None):
        mask = Gdk.WindowState.FULLSCREEN
        fullscreen = widget.get_window().get_state() & mask == mask

        if fullscreen:
            #self.left_pane.set_visible(False)
            self.mainBox.set_homogeneous(True)
        else:
            #self.left_pane.set_visible(True)
            self.mainBox.set_homogeneous(False)

    def serie_clicked(self, widget, event, link):
        serie = self.scrapper.get_series(link.link)
        self.show_links(serie)

    def episode_clicked(self, widget, event, link):
        links = self.scrapper.get_episode(link.href)['links']
        self.player.set_links(links)
        self.player.set_title(link.title)
        self.player.open(links[0])

    def go_back(self, widget):
        self.test_frame.hide()
        self.links_frame.show()

    def show_links(self, serie):
        box = Gtk.VBox()

        for episod in serie['episodes']:
            button = Gtk.Button(episod.title)
            box.pack_start(button, False, False, 0)
            button.connect("button-press-event", self.episode_clicked, episod)
            button.show()

        box.show()
        self.links_frame.hide()
        self.test_frame.add(box)
        self.test_frame.show()

    def open(self, *args):
        search = Search()
        links = search.search(self.entry.get_text())

        self.grid_helper.refresh()

        for link in links:
            url = link.img
            text = Gtk.Label(link.title)
            text.set_line_wrap(True)
            response = urllib2.urlopen(url)
            input_stream = Gio.MemoryInputStream.new_from_data(response.read(), None)
            pixbuf = Pixbuf.new_from_stream(input_stream, None)
            image = Gtk.Image()
            image.set_from_pixbuf(pixbuf)

            box = Gtk.VBox()
            box.pack_start(image, False, False, 0)
            box.pack_start(text, False, False, 0)
            event_box = Gtk.EventBox()
            event_box.add(box)

            event_box.connect("button-press-event", self.serie_clicked, link)

            self.grid_helper.add_widget(event_box)

        self.grid_helper.load_widgets()
        self.window.show_all()

if __name__ == '__main__':
    Gdk.threads_init()
    Gdk.threads_enter()
    ui = UI()
    Gtk.main()
    Gdk.threads_leave()
import os, sys
from gi.repository import Gtk, Gdk
from gi.repository import WebKit
from gui.html import Html
from scrapper.scrapper import Scrapper
from scrapper.search import Search
from helpers.drawers import Grid

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

        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(os.getcwd(), 'easy-entry.ui'))
        self.window = self.builder.get_object('faiancaWindow')
        self.window.set_size_request(860, 600)

        self.go_btn = self.builder.get_object('go_btn')
        self.close_btn = self.builder.get_object('close_btn')
        self.entry = self.builder.get_object('searchinput')

        self.left_pane = self.builder.get_object('box2')
        self.player_frame = self.builder.get_object('viewport1')
        self.links_frame = self.builder.get_object('links')
        self.mainBox = self.builder.get_object('box1')

        self.grid_helper = Grid()

        self.grid = self.grid_helper.get()
        self.links_frame.add(self.grid)

        self.entry.connect("activate", self.on_searchinput_activate)
        self.window.connect("window-state-event", self.on_window_state_event)
        self.window.connect('delete-event', self.quit)
        self.go_btn.connect('clicked', self.open)
        self.close_btn.connect('clicked', self.quit)
        self.window.show_all()

    def on_searchinput_activate(self, widget):
        self.open()

    def on_window_state_event(self, widget, event, data=None):
        mask = Gdk.WindowState.FULLSCREEN
        fullscreen = widget.get_window().get_state() & mask == mask

        if fullscreen:
            self.left_pane.set_visible(False)
            self.mainBox.set_homogeneous(True)
        else:
            self.left_pane.set_visible(True)
            self.mainBox.set_homogeneous(False)

    def serie_clicked(self, widget, link):
        print link

    def open(self, *args):
        search = Search()
        links = search.search(self.entry.get_text())

        for link in links:
            button1 = Gtk.Button(label=link.title)
            button1.connect("clicked", self.serie_clicked, link.link)
            self.grid_helper.add_widget(button1)

        self.grid_helper.refresh()
        self.window.show_all()

    def quit(self, *args):
        Gtk.main_quit()

if __name__ == '__main__':
    Gdk.threads_init()
    Gdk.threads_enter()
    ui = UI()
    Gtk.main()
    Gdk.threads_leave()
import os, sys
from gi.repository import Gtk, Gdk
from gi.repository import WebKit
from gui.html import Html

css = """
#faiancaWindow {
   /* background-color: #ffffff; */
}

"""


class UI:
    def __init__(self):
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.html = Html()
        self.builder = Gtk.Builder()
        self.browser = WebKit.WebView()
        self.builder.add_from_file(os.path.join(os.getcwd(), 'easy-entry.ui'))
        self.window = self.builder.get_object('faiancaWindow')
        self.window.set_size_request(860, 600)

        self.go_btn = self.builder.get_object('go_btn')
        self.close_btn = self.builder.get_object('close_btn')
        self.entry = self.builder.get_object('searchInput')

        self.left_pane = self.builder.get_object('box2')
        self.player_frame = self.builder.get_object('viewport1')
        self.mainBox = self.builder.get_object('box1')
        self.player_frame.add(self.browser)

        #self.list_episode()

        self.window.connect("window-state-event", self.on_window_state_event)
        self.window.connect('delete-event', self.quit)
        self.go_btn.connect('clicked', self.open)
        self.close_btn.connect('clicked', self.quit)
        self.window.show_all()

    def on_window_state_event(self, widget, event, data=None):
        mask = Gdk.WindowState.FULLSCREEN
        fullscreen = widget.get_window().get_state() & mask == mask

        if fullscreen:
            self.left_pane.set_visible(False)
            self.mainBox.set_homogeneous(True)
        else:
            self.left_pane.set_visible(True)
            self.mainBox.set_homogeneous(False)

    def list_episode(self):
        grid = Gtk.Grid()

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach(button5, 1, 1, 1, 1)

        self.player_frame.add(grid)

    def print_text(self, *args):
        print '%s' % (self.entry.get_text())

    def open(self, *args):
        movie = self.html.create("http://gateway.videofun.me/videos/ongoing/terra_formars_-_10.mp4?st=hbZR4lXuR1PO8zU43TtEYA&e=1417374304&server=videofun")
        self.browser.open(movie)
        self.window.set_title("Terraformars")

    def quit(self, *args):
        Gtk.main_quit()

if __name__ == '__main__':
    ui = UI()
    Gtk.main()

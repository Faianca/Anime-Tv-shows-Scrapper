import os, sys
from gi.repository import Gtk, Gdk
from gi.repository import WebKit
from gui.html import Html
from scrapper.scrapper import Scrapper


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

        self.scrapper = Scrapper()

        self.html = Html()
        self.builder = Gtk.Builder()
        self.browser = WebKit.WebView()
        #self.browser.connect("load-finished", self.load_finished)

        #browser_settings = WebKit.WebSettings()
       # useragent = browser_settings.get_property('user-agent')

        #browser_settings.set_property('user-agent', 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10')

        #self.browser.set_settings(browser_settings)
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

    def load_finished(self, webview, frame):
        #self.browser.execute_script("console.log(document.querySelector('#flowplayer div'))")
        pass

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
        episode = self.scrapper.get_episode("http://www.animehere.com/akame-ga-kill-episode-22.html")
        link = episode['links'][0]
        movie = self.html.create(link)
        self.browser.open(movie)
        self.window.set_title(episode['title'])

    def quit(self, *args):
        Gtk.main_quit()

if __name__ == '__main__':
    ui = UI()
    Gtk.main()

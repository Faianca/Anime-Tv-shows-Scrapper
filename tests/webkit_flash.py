__author__ = 'jmeireles'

from gi.repository import Gtk, WebKit

win = Gtk.Window()
win.set_size_request(800, 600)
browser = WebKit.WebView()
browser.open('http://www.dailymotion.com/video/x2bah9j_ladron-movil-dosis-karma-instantaneo_people')

win.add(browser)
win.show_all()
Gtk.main()



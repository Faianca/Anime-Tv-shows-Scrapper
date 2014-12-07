__author__ = 'jmeireles'

from gi.repository import WebKit


class Browser():

    def __init__(self):
        self.browser = WebKit.WebView()
        self.browser.connect("load-finished", self.load_finished)

    def load_html(self, html):
        self.browser.load_html_string(html, '')

    def open(self, url):
        self.browser.open(url)

    def load_finished(self, webview, frame):
        #self.browser.execute_script("alert('yo')")
        pass

    def get(self):
        return self.browser
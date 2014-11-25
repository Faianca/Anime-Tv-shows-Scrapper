__author__ = 'jmeireles'

import webkit


class Browser():

    def __init__(self):
        self.browser = webkit.WebView()

    def open(self, url):
        self.browser.open(url)

    def get(self):
        return self.browser
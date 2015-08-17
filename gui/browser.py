__author__ = 'jmeireles'

from gi.repository import WebKit


class Browser():

    def __init__(self):
        self.browser = WebKit.WebView()
        self.browser.connect("load-finished", self.load_finished)
        browser_settings = WebKit.WebSettings()
        test = 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
        #test = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'
        #test = 'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10'
        #browser_settings.set_property('user-agent', test)
        browser_settings.set_property("enable-plugins", True)
        browser_settings.set_property("enable-html5-database", True)
        browser_settings.set_property("enable-html5-local-storage", True)
        browser_settings.set_property("enable-scripts", True)
        self.browser.set_settings(browser_settings)


    def load_html(self, html):
        self.browser.load_html_string(html, '')

    def open(self, url):
        self.browser.open(url)
        self.browser.show()

    def load_finished(self, webview, frame):
        #self.browser.execute_script("alert('yo')")
        pass

    def get(self):
        return self.browser
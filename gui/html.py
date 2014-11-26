__author__ = 'jmeireles'
import string
from helper import Helper


class Html():

    def __init__(self):
        self.html_page = Helper.get_resource_path("test.html")
        self.html = string.Template('''
        <html>
            <head>
                <script type="text/javascript" src="$jwplayer"></script>
                <script type="text/javascript">jwplayer.key="sZhno26KBTT4wkrwM5dYR7Gv2ncG0T/DTjmDlQ==";</script>
                <style>
                    html {
                        background: black;
                    }

                    body {
                        width:400px;
                        height:400px;
                        margin:0
                    }
                </style>
            </head>
            <body>
                    <div id="myElement">Loading the player...</div>

                    <script type="text/javascript">
                        jwplayer("myElement").setup({
                            autostart: true,
                            timeoutInSeconds: 20,
                            height: 600,
                            width: 800,
                            file: "$url"
                        });
                    </script>
            </body>
            </html>
        ''')

    def open(self, url):
        jwplayer = Helper.get_resource_path("jwplayer.js")
        values = {'url': url, 'jwplayer': jwplayer}
        html = self.html.substitute(values)
        self.save(html)

        return self.html_page

    def save(self, html):
        html_file = open(self.html_page,"w")
        html_file.write(html)
        html_file.close()


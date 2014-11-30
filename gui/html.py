__author__ = 'jmeireles'
import string
from helper import Helper


class Html():

    def __init__(self):
        self.html_page = Helper.get_resource_path("test.html")
        #self.html_simple_page = Helper.get_resource_path("test2.html")
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

        self.html_simple = string.Template('''
<!DOCTYPE html>
<html>
<head lang="en">
    <script>
        var blocklist = new Array();

        blocklist["IMG"] = [["src", /.*doubleclick.net.*/],
                            ["src", /.*last.fm\/adserver.*/]];

        blocklist["SCRIPT"] = [["src", /.*doubleclick.net.*/]];

        blocklist["IFRAME"] = [["src", /.*gogoanime.*/],
                               ["name", /.*google_ads.*/],
                               ["id", /.*ad-google.*/]];

        function adblock(event)
        {
            var tag = event.target.tagName;
            if (!blocklist[tag])
                return;
            for(var i = 0; i < blocklist[tag].length; i++) {
                if (event.target.getAttribute(blocklist[tag][i][0])) {
                    if (event.target.getAttribute(blocklist[tag][i][0]).match(blocklist[tag][i][1])) {
                        event.preventDefault();
                        return;
                    }
                }
            }
        }

        document.addEventListener("beforeload", adblock, true);
    </script>
    <style>
        html {
        background: black;
        }

        body {
                        width:800px;
                        height:600px;
                        margin:0
                    }
    </style>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<iframe frameborder="0" background="black" width="800" height="600" src="$iframeurl"></iframe>
</body>
</html>
        ''')


    def create_simple(self, url):
        values = {'iframeurl': url}
        html = self.html_simple.substitute(values)
        self.save_simple(html)

        return self.html_simple_page

    def create(self, url):
        jwplayer = Helper.get_resource_path("jwplayer.js")
        values = {'url': url, 'jwplayer': jwplayer}
        html = self.html.substitute(values)
        self.save(html)

        return self.html_page

    def save(self, html):
        html_file = open(self.html_page, "w")
        html_file.write(html)
        html_file.close()

    def save_simple(self, html):
        html_file = open(self.html_simple_page, "w")
        html_file.write(html)
        html_file.close()


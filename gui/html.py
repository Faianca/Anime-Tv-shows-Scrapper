__author__ = 'jmeireles'
import string
from helper import Helper


class Html():

    def __init__(self):
        self.html_page = Helper.get_resource_path("test.html")
        self.html_simple_page = Helper.get_resource_path("test2.html")
        self.html = string.Template('''
        <html>
    <head>
        <script type="text/javascript" src="$jwplayer"></script>
        <script type="text/javascript">jwplayer.key="sZhno26KBTT4wkrwM5dYR7Gv2ncG0T/DTjmDlQ==";</script>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
        <title>tete</title>
        <style>
            html {
                background: black;
            }

            body {
                margin:0 auto;
                color: white;
            }
            #episodes::-webkit-scrollbar {
                width: 1em;
            }

            #episodes::-webkit-scrollbar-track {
                -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
            }

            #episodes::-webkit-scrollbar-thumb {
              background-color: green;
              outline: 1px solid slategrey;
            }
            ul {
            padding:5px;
            }
            #player { float:left; }

        </style>
    </head>
    <body>
    <div id="player">
         <div id="myElement">Loading the player...</div>
    </div>
    <div id="episodes">
        <ul id="episodes-list">
        </ul>
    </div>

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
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
   <link rel="stylesheet" href="/home/jmeireles/PycharmProjects/anime/gui/style.css" media="all" type="text/css" />
    <script>
        var blocklist = new Array();

        blocklist["IMG"] = [["src", /.*doubleclick.net.*/],
                            ["src", /.*rubiconproject.*/],
                            ["src", /.*anime44.*/],
                            ["src", /.*last.fm\/adserver.*/]];

        blocklist["SCRIPT"] = [
                                ["src", /.*doubleclick.net.*/],
                                ["src", /.*anime44.*/],
                                ["src", /.*rubiconproject.*/]
                                ];

        blocklist["IFRAME"] = [["src", /.*gogoanime.*/],
                               ["src", /.*ad_iframe.*/],
                               ["src", /.*anime44.*/],
                               ["src", /.*rubiconproject.*/],
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
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<div aria-busy="true" aria-label="Loading" role="progressbar" class="container">
  <div class="swing">
    <div class="swing-l"></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div class="swing-r"></div>
  </div>
  <div class="shadow">
    <div class="shadow-l"></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <div class="shadow-r"></div>
  </div>
 </div>
<iframe id="player" frameborder="0" background="black" width="800" height="600" src="$iframeurl"></iframe>
<script>
    jQuery('#player').on('load',function() {
        jQuery('.container').hide();
        jQuery('html').css('background', 'black');
        jQuery(this).show();
    });
</script>
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


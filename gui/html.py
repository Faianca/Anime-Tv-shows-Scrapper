__author__ = 'jmeireles'
import string
from helper import Helper


class Html:

    def __init__(self):
        self.html_page = Helper.get_resource_path("test.html")
        self.html = string.Template('''
        <!DOCTYPE HTML>
<html>
<head>
    <title>Projekktor - simply mighty video</title>
    <style type="text/css">
    body { background-color:#000;; padding:0; margin:0; }
    </style>

    <!-- Load player theme -->
    <link rel="stylesheet" href="/home/jmeireles/Anime-Tv-shows-Scrapper/themes/maccaco/projekktor.style.css" type="text/css" media="screen" />

    <!-- Load jquery -->
    <script type="text/javascript" src="/home/jmeireles/Anime-Tv-shows-Scrapper/jquery-1.9.1.min.js"></script>

    <!-- load projekktor -->
    <script type="text/javascript" src="/home/jmeireles/Anime-Tv-shows-Scrapper/projekktor-1.3.09.min.js"></script>

</head>
<body>
    <div id="player_a" class="projekktor"></div>

    <script type="text/javascript">
    jQuery(document).ready(function() {
        projekktor('#player_a', {
        //poster: '/home/jmeireles/Anime-Tv-shows-Scrapper/media/intro.png',
        title: 'this is projekktor',
        autoplay: true,
        playerFlashMP4: '/home/jmeireles/Anime-Tv-shows-Scrapper/swf/StrobeMediaPlayback/StrobeMediaPlayback.swf',
        playerFlashMP3: '/home/jmeireles/Anime-Tv-shows-Scrapper/swf/StrobeMediaPlayback/StrobeMediaPlayback.swf',
        width: 860,
        height: 600,
        videoScaling: "aspectratio",
        playlist: [
            {
            0: {src: "$url", type: "video/mp4"},
            }
        ]
        }, function(player) {} // on ready
        );
    });
    </script>
</html>

        ''')

    def create(self, url):
        values = {'url': url}
        html = self.html.substitute(values)
        self.save(html)

        return self.html_page

    def save(self, html):
        html_file = open(self.html_page, "w")
        html_file.write(html)
        html_file.close()
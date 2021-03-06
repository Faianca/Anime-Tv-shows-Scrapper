__author__ = 'jmeireles'
import string
from helper import Helper


class Html:

    def __init__(self):
        self.html_page = "/home/jmeireles/Anime-Tv-shows-Scrapper/server/public/index.html"#Helper.get_resource_path("test.html")
        self.html = string.Template('''
        <!DOCTYPE HTML>
<html>
<head>
    <title>Projekktor - simply mighty video</title>
    <style type="text/css">
    body { background-color:#000;; padding:0; margin:0; }
    </style>

    <!-- Chang URLs to wherever Video.js files will be hosted -->
    <link href="video-js.css" rel="stylesheet" type="text/css">

    <!-- video.js must be in the <head> for older IEs to work. -->
    <script src="video.js"></script>

    <!-- Load jquery -->
    <script type="text/javascript" src="jquery-1.9.1.min.js"></script>


</head>
<body>
    <video id="example_video_1" class="video-js vjs-default-skin" controls preload="none" width="860" height="600"
      poster="http://video-js.zencoder.com/oceans-clip.png"
      data-setup="{}">
    <source src="$url" type='video/mp4' />
    <track kind="captions" src="demo.captions.vtt" srclang="en" label="English"></track><!-- Tracks need an ending tag thanks to IE9 -->
    <track kind="subtitles" src="demo.captions.vtt" srclang="en" label="English"></track><!-- Tracks need an ending tag thanks to IE9 -->
  </video>
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
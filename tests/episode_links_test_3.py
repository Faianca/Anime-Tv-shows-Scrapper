__author__ = 'jmeireles'
from scrapper.scrapper import Scrapper
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

testS = Scrapper()
episode = testS.get_episode("http://www.animehere.com/terra-formars-episode-10.html")
link = episode['links'][0]


class VideoPlayerApp(App):

    def build(self):
        video = VideoPlayer(fullscreen=True, allow_fullscreen=True, source=link[0], state='play', options={'allow_stretch': True, 'fullscreen': True})
        return video


if __name__ == '__main__':
    VideoPlayerApp().run()

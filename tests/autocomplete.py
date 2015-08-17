import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.lang import Builder

Builder.load_string ('''
<MyVideoPlayer>:
    orientation: "vertical"
    VideoPlayer:
        source: "http://www.animehere.com/terra-formars-episode-10.html"
    Button:
        text: "Add Video Dynamically"
        on_press: root.add(*args)
    Button:
        text: "Change video Dynamically"
        on_press: root.change(*args)
''')

class MyVideoPlayer(BoxLayout):

    def add(self, instance):
        self.video_player = VideoPlayer(source = "http://www.animehere.com/terra-formars-episode-10.html")
        self.add_widget(self.video_player)

    def change(self, instance):
        self.video_player.source = "http://www.animehere.com/terra-formars-episode-10.html"

class MyVideoPlayerApp(App):
    def build(self):
        return MyVideoPlayer()

if __name__ == '__main__':
    MyVideoPlayerApp().run()
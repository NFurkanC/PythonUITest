from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.image import Image

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongApp().run()
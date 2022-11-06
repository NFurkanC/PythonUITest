from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics.vertex_instructions import Line

class AniBox(Widget):
    pass
    
class UIBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(200,300,600,300),width=3)
#class AniBox aktif değil!
class AniUI(App):
    pass

AniUI().run()

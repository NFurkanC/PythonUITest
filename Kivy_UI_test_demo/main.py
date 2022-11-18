from kivy.app import App
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
import serial


class AniBox(Widget):
    pass
    
class UIBox(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.gauge_line = Line(points=(210,300,600,300),width=3)
            Color(0,1,0)
    def on_button1_click(self):
        x, y, x2, y2 = self.gauge_line.points
        y= y- dp(20)
        y2 += dp(20)
        self.gauge_line.points = (x,y,x2,y2)
    def on_button2_click(self):
        x, y, x2, y2 = self.gauge_line.points
        y2= y2- dp(20)
        y += dp(20)
        print(y,y2)
        self.gauge_line.points = (x,y,x2,y2)
#class AniBox aktif değil!
class MizanUI(App):
    pass

MizanUI().run()

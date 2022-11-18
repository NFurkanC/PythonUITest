from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import BooleanProperty
import serial

count = 0
arduino= serial.Serial(port = 'COM4', baudrate = 9600, timeout =.1)
    
class UIBox(Widget):
    loop_thread = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.gauge_line = Line(points=(210,300,600,300),width=3)
            Color(0,1,0)
    def callback_to_loop(self,dt): #dt = loop interval
        x, y, x2, y2 = self.gauge_line.points
        d1 = arduino.readline().rstrip().decode()
        print(d1) 
        if d1:
            data = int(d1)
            y = dp(160 + (data * 0.27))
            y2 = dp(440 - (data * 0.27))
            self.gauge_line.points = (x,y,x2,y2)

    def on_button1_click(self, widget):
        if widget.state == "normal":
            widget.text = "Kapalı"
            self.loop_thread = Clock.unschedule(self.callback_to_loop)
        if widget.state == "down":
            widget.text = "Açık"
            self.loop_thread = Clock.schedule_interval(self.callback_to_loop, .025) #interval = 0.025 saniye, serial'i yakalamak için delay'in yarısı kadar interval 

class MizanUI(App):
    pass

MizanUI().run()

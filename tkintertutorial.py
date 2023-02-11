import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk, ImageDraw
from tkinter import Button
from tkinter import Frame
import cv2
from tkinter import Label
import serial

#mizu = serial.Serial(port = '', baudrate = 9600, timeout = .1)
class OrientDisplay(ttk.Label):
    def __init__(self,parent,**kwargs):
        self.arc = None
        self.im = Image.new('RGBA', (1000, 1000))
        self.min_value = kwargs.get('minvalue') or 0
        self.max_value = kwargs.get('maxvalue') or 100
        self.size = kwargs.get('size') or 200
        self.halfsize = kwargs.get('halfsize') or 100
        self.font = kwargs.get('font') or 'helvetica 12 bold'
        self.background = kwargs.get('background')
        self.foreground = kwargs.get('foreground') or '#777'
        self.troughcolor = kwargs.get('troughcolor') or '#e0e0e0'
        self.indicatorcolor = kwargs.get('indicatorcolor') or '#01bdae'
        self.arcvariable = tk.IntVar(value='text')
        self.arcvariable.trace_add('write', self.update_arcvariable)
        self.textvariable = tk.StringVar()
        self.setup()

        super().__init__(parent, image=self.arc, compound='center', style='Gauge.TLabel', textvariable=self.textvariable, **kwargs)
    def setup(self):
            """Setup routine"""
            style = ttk.Style()
            style.configure('Gauge.TLabel', font=self.font, foreground=self.foreground)
            if self.background:
                style.configure('Gauge.TLabel', background=self.background)
            draw = ImageDraw.Draw(self.im)
            draw.arc((0, 0, 990, 990), 180, 360, self.troughcolor, 100)
            self.arc = self.im.resize((self.size,self.size), Image.LANCZOS)
            #self.arc = self.arc.crop([0,100,200,200])
            self.arc = ImageTk.PhotoImage(self.arc)
    def update_arcvariable(self, *args):
        """Redraw the arc image based on variable settings"""
        angle = int(float(self.arcvariable.get())) + 90
        self.im = Image.new('RGBA', (1000, 1000))
        draw = ImageDraw.Draw(self.im)
        draw.arc((0, 0, 990, 990), 180, 360, self.troughcolor, 100)
        draw.arc((0, 0, 990, 990), angle - 10, angle + 10, self.indicatorcolor, 100)
        self.arc = ImageTk.PhotoImage(self.im.resize((self.size, self.size), Image.LANCZOS))
        self.configure(image=self.arc)
    def addVal(self):
        global arcval
        arcval = arcval + 5
        self.arcvariable.set(arcval)
def show_frames():
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    img = img.resize((500,300),Image.LANCZOS)
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    label.after(20, show_frames)
def show_frames2():
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    img = img.resize((500,300), Image.LANCZOS)
    imgtk = ImageTk.PhotoImage(image = img)
    label2.imgtk = imgtk
    label2.configure(image=imgtk)
    label2.after(20, show_frames)
if __name__ == '__main__':
    root = tk.Tk()
    style = ttk.Style()
    cap= cv2.VideoCapture(0)
    #Frame'lerin setupı
    btnFrame = Frame(root, width = 600, height = 50)
    btnFrame.grid(row = 2, column = 0, padx = 10, pady = 5)
    topFrame = Frame(root, width = 600, height = 100)
    topFrame.grid(row = 1, column = 0, padx = 10, pady = 5)
    camFrame = Frame(root, width = 600, height = 300)
    camFrame.grid(row = 0, column = 0, padx = 10, pady = 5)
    #------------------------------------------------------
    label =Label(camFrame)
    label2 = Label(camFrame)
    label.grid(row=0, column=0)
    label2.grid(row = 0, column=1)
    gauge0 = OrientDisplay(topFrame)
    gauge1 = OrientDisplay(topFrame)
    gauge2 = OrientDisplay(topFrame)
    #root.resizable(False,False)
    root.title("Zağanos UI")
    gauge0.grid(row = 0, column = 0, padx=20, pady=20)
    gauge1.grid(row = 0, column = 1, padx = 20, pady = 20)
    gauge2.grid(row = 0, column = 2,padx= 20, pady = 20)
    arcval = 90
    #------------------------------------------------------
    #ttk.Scale(btnFrame, from_=90, to=270, variable=gauge1.arcvariable).grid(row = 0, column = 0, padx=10, pady=10)
    btn = Button(btnFrame, text = 'Başlat', bd = '5', command = gauge0.addVal).grid(row = 0, column= 1)
    #textvariable'ı güncelle
    gauge0.arcvariable.set(150)
    gauge1.arcvariable.set(180)
    gauge2.arcvariable.set(200)
    gauge0.textvariable.set("X ekseni")
    gauge1.textvariable.set("Y ekseni")
    gauge2.textvariable.set("Z ekseni")
    gauge1.arcvariable.trace_add('write', lambda *args, g=gauge1: g.textvariable.set(f'{g.arcvariable.get()} deg'))
    gauge0.arcvariable.trace_add('write', lambda *args, g=gauge0: g.textvariable.set(f'{g.arcvariable.get()} deg'))
    show_frames()
    show_frames2() #kamerayı göster
    root.mainloop()




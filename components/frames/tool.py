from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from PIL import ImageTk, Image
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
import os

class ToolLeft(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,width="30" ,relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.__initUI()
  
    def __initUI(self):
        self.pack(side=LEFT,fill="y")
        Tools(self)

class Tools(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent,width="30" ,relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.pathMain = os.getcwd()
        self.__initUI()
  
    def __initUI(self):
        self.pack(side=LEFT,fill="y")

        #img = ImageTk.PhotoImage(Image.open('/data/public/cursor.svg'))
        #Label(self, image=img).pack()
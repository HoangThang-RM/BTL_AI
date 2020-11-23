from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from components.frames.config import BGWHITE, WHITE

class GraphFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGWHITE,relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.pack(side=LEFT, fill="both", expand=True)
        
        label = Label(self,text="Đồ thị", pady=10,bg=WHITE ,font="Arial 18 bold")
        label.pack(fill=BOTH)
from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame


class ToolLeft(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,width="30" ,relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.__initUI()
  
    def __initUI(self):
        self.pack(side=LEFT,fill="y")
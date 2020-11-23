from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from components.frames.config import BGGREY

class BottomFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, height="30", relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.pack(side=BOTTOM,fill="x")
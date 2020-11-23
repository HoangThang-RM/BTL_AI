from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from components.frames.config import BGGREY,GREY

class TopFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent,height="100",relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.__initUI()
    
    def __initUI(self):
        self.pack(fill="x")

        label = Label(self,text="Thuật toán tối ưu", pady=10, bg=GREY,font="Arial 18 bold")
        label.pack(fill=BOTH)

        #frame Tool
        wrap = Frame(self, height="80", style=BGGREY)
        wrap.pack(fill=BOTH,pady=10)

        toolFrame = Frame(wrap, style=BGGREY)
        toolFrame.pack()

        alg_value = StringVar()
        algchoosen = Combobox(toolFrame, state="readonly", textvariable = alg_value, font="Arial 12")
        algchoosen["values"] = ("Thuật toán 1", "Thuật toán 2", "Thuật toán 3", "Thuật toán 4")
        algchoosen.current(0)
        algchoosen.grid(column=0,row=0,pady=2)

        def btnClicked():
            print(alg_value.get())
        button = Button(toolFrame, text="Tính", command=btnClicked)
        button.grid(column=1,row=0, padx=3, pady=2)
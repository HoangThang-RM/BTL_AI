from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox, Canvas,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from lib.Node import Node
from components.frames.config import BGWHITE, WHITE
from lib.global_variable import set_variable,get_variable

class GraphFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGWHITE,relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.pack(side=LEFT, fill="both", expand=True)
        #label = Label(self,text="Đồ thị", pady=10,bg=WHITE ,font="Arial 18 bold")
        #label.pack(fill=BOTH)

        self.canvas = Canvas(self,bg=WHITE,bd=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=5, pady=5)

        nodeList = get_variable("nodeList")
        
        A = Node(self.canvas,"A",300,None,200,10,30)
        B = Node(self.canvas,"B",100,A,150,60,30)
        C = Node(self.canvas,"C",200,A,250,60,30)
        D = Node(self.canvas,"D",500,C,300,120,30)
        
        A.add_child(B,30)
        A.add_child(C,10)
        C.add_child(D,50)
          
        #A._childNodes = [{"Node":B,"g":30},{"Node":C,"g":10}]
        #C._childNodes = [{"Node":D,"g":50}]

        nodeList = [A,B,C,D]
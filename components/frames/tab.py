from tkinter import GROOVE,LEFT
from tkinter.ttk import Frame,Notebook
from components.frames import graph,matrix
from components.frames.config import BGWHITE, WHITE
from lib.global_variable import set_variable

class TabFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGWHITE,relief=GROOVE, borderwidth=1)
        self._parent = parent
        self.__initUI()
    
    def __initUI(self):
        self.pack(side=LEFT, fill="both", expand=True)
        tabControl = Notebook(self)
        tabControl.pack(side=LEFT, fill="both", expand=True)
        tab1 = graph.GraphFrame(self._parent)
        tab2 = matrix.MatrixFrame(self._parent)
        tabControl.add(tab1,text="Cây")
        tabControl.add(tab2,text="Ma trận")

        set_variable("matrix",tab2)
        set_variable("tabControl",tabControl)
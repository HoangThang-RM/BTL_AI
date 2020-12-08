from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox, Canvas,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE,LAST,SUNKEN
from tkinter.ttk import Style, Notebook, Combobox, Frame
from lib.node import Node
from components.frames.config import BGWHITE, WHITE
from lib.global_variable import set_variable,get_variable

class MatrixFrame(Frame):
    def __init__(self, parent,height = 3,width = 3):
        Frame.__init__(self, parent,style=BGWHITE,relief=GROOVE, borderwidth=0)
        self._parent = parent
        self._height = height
        self._width = width
        self._cellStart = [[0 for x in range(width)] for y in range(height)] 
        self._cellEnd = [[0 for x in range(width)] for y in range(height)] 
        self.__initUI()

    def __initUI(self):
        self.pack(side=LEFT, fill="both", expand=True)

        self.cover = Frame(self,style=BGWHITE)
        self.cover.pack(fill=None, expand=True)

        Label(self.cover,text="Trạng thái đầu",font="Arial 10 bold",bg = WHITE).pack()
        self._frmStart =Frame(self.cover,style=BGWHITE)
        self._frmStart.pack(pady=20)
        for i in range(self._height):
            for j in range(self._width):
                self._cellStart[i][j] = StringVar()
                Entry(self._frmStart,width=5,textvariable=self._cellStart[i][j],borderwidth=2,relief=GROOVE).grid(row = i, column = j)

        Label(self.cover,text="Trạng thái cuối",font="Arial 10 bold",bg = WHITE).pack()
        self._frmEnd =Frame(self.cover,style=BGWHITE)
        self._frmEnd.pack(pady=20)
        for i in range(self._height):
            for j in range(self._width):
                self._cellEnd[i][j] = StringVar()
                Entry(self._frmEnd,width=5,textvariable=self._cellEnd[i][j],borderwidth=2,relief=GROOVE).grid(row = i, column = j)

    def get_cell_start(self):
        cell = [[0 for x in range(self._width)] for y in range(self._height)]
        for i in range(self._height):
            for j in range(self._width):
                cell[i][j] = self._cellStart[i][j].get()
        return cell

    def get_cell_end(self):
        cell = [[0 for x in range(self._width)] for y in range(self._height)]
        for i in range(self._height):
            for j in range(self._width):
                cell[i][j] = self._cellEnd[i][j].get()
        return cell


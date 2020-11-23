from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from components.frames.config import GREY

class childNode(Frame):
    def __init__(self,parent,name,h):
        Frame.__init__(self, parent)
        self.parent = parent
        self.name = name
        self.h = h
        self.__initUI()

    def __initUI(self):
        self.pack()

        lbl = Label(self, text=self.name, width="10",bg=GREY)
        lbl.grid(column=0, row=0, padx=5,pady=5)
        e = Entry(self, width=10)
        e.grid(column=1, row=0, padx=5, pady=5)
        e.insert(END,self.h)

class InforNodeRight(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,width="200", relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.__initUI()
  
    def __initUI(self):
        self.pack(side=RIGHT,fill="y")

        Label(self, text="Tên điểm", bg=GREY).pack(padx=20, pady=(20,10))
        Entry(self).pack(padx=20)
        Label(self, text="G",bg=GREY).pack(padx=20, pady=(20,10))
        Entry(self).pack(padx=20)
        
        Label(self, text="Danh sách điểm con",bg=GREY).pack(padx=20, pady=(30,5))
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)
        self.childFrame.pack(padx=20,pady=10,ipadx=5,ipady=5)
        
        self.titleFrame = Frame(self.childFrame)
        self.titleFrame.pack()
        Label(self.titleFrame, text="Tên điểm", width="10", bg=GREY).grid(column=0, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="Chỉ số H", width="10", bg=GREY).grid(column=1, row=0, padx=5,pady=5)

        self.listChild = [childNode(self.childFrame,"A",10),childNode(self.childFrame,"B",20),childNode(self.childFrame,"C",30)]
        
        Button(self, text="Edit", command = lambda: self.edit([])).pack(side=BOTTOM, pady=50)

    def edit(self,listChild):
        self.listChild = [] #giai phong bo nho childNode
        self.listChild = listChild

        self.childFrame.destroy()
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)
        self.childFrame.pack(padx=20,pady=10,ipadx=5,ipady=5)
        self.titleFrame = Frame(self.childFrame)
        self.titleFrame.pack()
        Label(self.titleFrame, text="Tên điểm", width="10", bg=GREY).grid(column=0, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="Chỉ số H", width="10", bg=GREY).grid(column=1, row=0, padx=5,pady=5)

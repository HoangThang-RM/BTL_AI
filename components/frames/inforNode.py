from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from components.frames.config import GREY
from lib.global_variable import set_variable,get_variable

class InforNodeRight(Frame):
    def __init__(self, parent, target = {}):
        Frame.__init__(self, parent,width="200", relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.target = target
        self.__initUI()
  
    def __initUI(self):
        self.pack(side=RIGHT,fill="y")

        self.entNode = StringVar()
        self.entNode.set("D")
        #entNode = self.target.get("nameNode")
        Label(self, text="Tên điểm", bg=GREY).pack(padx=20, pady=(20,10))
        Entry(self, textvariable = self.entNode).pack(padx=20)


        self.entH = StringVar()
        #entCost = self.target.get("cost")
        Label(self, text="giá trị đỉnh", bg=GREY).pack(padx=20, pady=(20,10))
        Entry(self, textvariable = self.entH).pack(padx=20)
        self.entH.set("100")
        
        Label(self, text="Danh sách điểm con", bg=GREY).pack(padx=20, pady=(30,5))
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)
        self.childFrame.pack(padx=20,pady=10,ipadx=5,ipady=5)
        
        self.titleFrame = Frame(self.childFrame)
        self.titleFrame.pack()
        Label(self.titleFrame, text="Tên điểm", width="10", bg=GREY).grid(column=0, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="Chỉ số H", width="10", bg=GREY).grid(column=1, row=0, padx=5,pady=5)

        self.listChild = [childNode(self.childFrame,"A",10),childNode(self.childFrame,"B",20),childNode(self.childFrame,"C",30)]
        
    def edit(self,listChild):
        self.listChild = [] #giai phong bo nho childNode
        self.listChild = listChild
        
        #infor Node
        self.entNode.set(self.target._nameNode)
        self.entH.set(self.target._heuristic)

        #list child
        self.childFrame.destroy()
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)
        self.childFrame.pack(padx=20,pady=10,ipadx=5,ipady=5)
        self.titleFrame = Frame(self.childFrame)
        self.titleFrame.pack()
        Label(self.titleFrame, text="Tên điểm", width="10", bg=GREY).grid(column=0, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="Chỉ số H", width="10", bg=GREY).grid(column=1, row=0, padx=5,pady=5)

class childNode(Frame):
    def __init__(self,parent,name,heuristic):
        Frame.__init__(self, parent)
        self._parent = parent
        self._name = name
        self._heuristic = heuristic
        self.__initUI()

    def __initUI(self):
        self.pack()

        lbl = Label(self, text=self._name, width="10",bg=GREY)
        lbl.grid(column=0, row=0, padx=5,pady=5)
        e = Entry(self, width=10)
        e.grid(column=1, row=0, padx=5, pady=5)
        e.insert(END,self._heuristic)
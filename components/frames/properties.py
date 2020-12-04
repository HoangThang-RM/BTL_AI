from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from components.frames.config import GREY
from lib.global_variable import set_variable,get_variable

class Properties(Frame):
    def __init__(self, parent, target = {}):
        Frame.__init__(self, parent,width="200", relief=GROOVE, borderwidth=1)
        self.parent = parent
        self.target = target
        self.listChild = []
        self.__initUI()
  
    def __initUI(self):
        self.pack(side=RIGHT,fill="y")

        self.varName = StringVar()
        Label(self, text="Tên điểm", bg=GREY).pack(padx=20, pady=(20,10))
        self._entName = Entry(self, textvariable = self.varName)
        self._entName.pack(padx=20)
        self._entName.bind("<Return>", self.edit_name)


        self.varHeuristic = StringVar()
        Label(self, text="giá trị đỉnh", bg=GREY).pack(padx=20, pady=(20,10))
        self._entHeuristic = Entry(self, textvariable = self.varHeuristic)
        self._entHeuristic.pack(padx=20)
        self._entHeuristic.bind("<Return>", self.edit_heuristic)

        Label(self, text="Danh sách điểm con", bg=GREY).pack(padx=20, pady=(30,5))
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)
        self.childFrame.pack(padx=20,pady=10,ipadx=5,ipady=5)
        
        self.titleFrame = Frame(self.childFrame)
        self.titleFrame.pack()
        Label(self.titleFrame, text="Tên điểm", width="10", bg=GREY).grid(column=0, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="Chỉ số H", width="10", bg=GREY).grid(column=1, row=0, padx=5,pady=5)
    
    def edit_name(self,e):
        nameNode = self.varName.get() 
        
        if(self.target == {}):
            return
        
        nodeList = get_variable("nodeList")
        for item in nodeList:
            if(item._nameNode.lower() == nameNode.lower()):
                self._entName.config(highlightthickness=1,highlightcolor="red")
                return
                
        self.target.edit_node(name = nameNode)
        self._entHeuristic.focus()

    def edit_heuristic(self,e):
        if(self.target == {}):
            return
        heuristicNode = self.varHeuristic.get()
        try:
            int(heuristicNode)
            self.target.edit_node(heuristic = heuristicNode)
            self.focus()
            return
        except Exception:
            self._entHeuristic.config(highlightthickness=1,highlightcolor="red")
            return
    
    def focus_name(self):
        self._entName.focus()

    def target_node(self,node):
        self.listChild = [] #giai phong bo nho childNode
        self._entHeuristic.config(highlightthickness=0,highlightcolor="black")
        self._entName.config(highlightthickness=0,highlightcolor="black")
        self._entName.focus()

        #highlight node
        if(self.target != {}):
            self.target._canvas.itemconfig(self.target._oval, outline="black")
        node._canvas.itemconfig(node._oval, outline="red")
        self.target = node

        #infor Node
        self.varName.set(self.target._nameNode)
        self.varHeuristic.set(self.target._heuristic)

        #show title
        self.childFrame.destroy()
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)
        self.childFrame.pack(padx=20,pady=10,ipadx=5,ipady=5)
        self.titleFrame = Frame(self.childFrame)
        self.titleFrame.pack()
        Label(self.titleFrame, text="Tên điểm", width="10", bg=GREY).grid(column=0, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="Chỉ số H", width="10", bg=GREY).grid(column=1, row=0, padx=5,pady=5)
        
        #show childs
        for item in node._childNodes:
            self.listChild.append(ChildNode(self.childFrame, item.get("Node"), item.get("cost")))

class ChildNode(Frame):
    def __init__(self,parent,node,cost):
        Frame.__init__(self, parent)
        self._parent = parent
        self._node = node
        self._cost = cost
        self.__initUI()

    def __initUI(self):
        self.pack()

        lblName = Label(self, text=self._node._nameNode, width="10",bg=GREY)
        lblName.grid(column=0, row=0, padx=5,pady=5)
        eCost = Entry(self, width=10)
        eCost.grid(column=1, row=0, padx=5, pady=5)
        eCost.insert(END,self._cost)
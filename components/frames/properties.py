from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, GROOVE, FLAT
from tkinter.ttk import Style, Combobox, Frame
from components.frames.config import GREY
from lib.global_variable import set_variable,get_variable
from lib.node import Node

class Properties(Frame):
    def __init__(self, parent, target = None):
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
        self._entName.bind("<FocusOut>", self.edit_name)


        self.varHeuristic = StringVar()
        Label(self, text="Giá trị đỉnh", bg=GREY).pack(padx=20, pady=(20,10))
        self._entHeuristic = Entry(self, textvariable = self.varHeuristic)
        self._entHeuristic.pack(padx=20)
        self._entHeuristic.bind("<Return>", self.edit_heuristic)
        self._entHeuristic.bind("<FocusOut>", self.edit_heuristic)

        Label(self, text="Danh sách điểm con", bg=GREY).pack(padx=20, pady=(30,5))
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)

        self.target_node()

    def edit_name(self,e = None):
        self._entName.config(highlightthickness=0)
        nameNode = self.varName.get() 
        
        if(self.target == None):
            return
        
        nodeList = get_variable("nodeList")
        for item in nodeList:
            if(item._nameNode.lower() == nameNode.lower() and item._nameNode.lower() != self.target._nameNode.lower()):
                self._entName.config(highlightthickness=1,highlightcolor="red")
                return
                
        self.target.edit_node(name = nameNode)

    def edit_heuristic(self,e = None):
        self._entHeuristic.config(highlightthickness=0)
        if(self.target == None):
            return
        heuristicNode = self.varHeuristic.get()
        try:
            int(heuristicNode)
            self.target.edit_node(heuristic = heuristicNode)
            return
        except Exception:
            self._entHeuristic.config(highlightthickness=1,highlightcolor="red")
            return
          
    def edit_cost(self,child,cost):
        if(self.target == None):
            return
        try:
            int(cost)
            self.target.edit_node(child = [child,cost])
            return
        except Exception:
            self._entHeuristic.config(highlightthickness=1,highlightcolor="red")
            return
    
    def focus_name(self):
        self._entName.focus()
    
    def focus_cost(self,nodeCost):
        for child in self.listChild:
            if(child._node == nodeCost):
                child._eCost.focus()
                break

    def target_node(self,node = None):
        #save old node
        if(self.target != None):
            self.target._canvas.itemconfig(self.target._oval, outline="black")
            self.edit_name()
            self.edit_heuristic()

        self.listChild = [] #giai phong bo nho childNode
        self._entHeuristic.config(highlightthickness=0,highlightcolor="black")
        self._entName.config(highlightthickness=0,highlightcolor="black")
        self.focus_name()
        
        #highlight node
        
        self.target = node
        if(node != None):
            node._canvas.itemconfig(node._oval, outline="red")
            self.varName.set(self.target._nameNode)
            self.varHeuristic.set(self.target._heuristic)
        else:
            self.varName.set("")
            self.varHeuristic.set("")

        #show title
        self.childFrame.destroy()
        self.childFrame = Frame(self, width="160", heigh="50", relief=GROOVE, borderwidth=1)
        self.childFrame.pack(padx=20,pady=10,ipadx=5,ipady=5)
        self.titleFrame = Frame(self.childFrame)
        self.titleFrame.pack()
        Label(self.titleFrame, text="Tên điểm", width="10", bg=GREY).grid(column=0, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="Giá trị cạnh", width="10", bg=GREY).grid(column=1, row=0, padx=5,pady=5)
        Label(self.titleFrame, text="",width="1",bg=GREY).grid(column=2,row=0)
        btnAdd = Button(self.childFrame, font = ("Times New Roman", 10), width=6, text="+"
                        ,bg=GREY,relief=GROOVE,command=self.create_new_child)
        btnAdd.pack(side=BOTTOM,pady=5)
        
        #show childs
        if(node != None):
            for item in node._childNodes:
                self.listChild.append(ChildNodeFrame(self.childFrame,self ,item.get("Node"), item.get("cost")))
    
    def create_new_child(self):
        if(self.target == None):
            return

        nodeList = get_variable("nodeList")
        children = self.target._childNodes
        x = None
        y = None
        if(children == []):
            x = self.target._x + 20
            y = self.target._y + 80
        else:
            x = children[-1]["Node"]._x + 50
            y = children[-1]["Node"]._y
        
        newChild = Node(self.target._canvas,"",0,x,y,30)
        nodeList.append(newChild)
        self.target.add_child(newChild,0)
        self.target_node(newChild)

    def delete_child(self,child):
        if(self.target == None):
            return
        self.target.remove_child(child)
    
    def delete_node(self):
        if(self.target != None):
            self.target.delete()
            self.target = None

class ChildNodeFrame(Frame):
    def __init__(self,parent,properties,node,cost):
        Frame.__init__(self, parent)
        self._parent = parent
        self._properties = properties
        self._node = node
        self._cost = cost
        self.__initUI()

    def __initUI(self):
        self.pack()

        lblName = Label(self, text=self._node._nameNode, width="10",bg=GREY)
        lblName.grid(column=0, row=0,pady=5)
    
        self.varCost = StringVar()
        self._eCost = Entry(self, width=10, textvariable = self.varCost)
        self._eCost.grid(column=1, row=0, padx=5, pady=5)
        self._eCost.insert(END,self._cost)
        self._eCost.bind("<Return>", lambda event: self._properties.edit_cost(self._node,self.varCost.get()))
        self._eCost.bind("<FocusOut>", lambda event: self._properties.edit_cost(self._node,self.varCost.get()))
        
  
        self.btnDelete = Button(self, font = ("Arial", 10), text="x"
                        ,bg=GREY,relief=FLAT,command= lambda : self._properties.delete_child(self._node))
        self.btnDelete.grid(column=2,row=0)
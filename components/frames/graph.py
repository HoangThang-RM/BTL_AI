from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox, Canvas,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE,LAST
from tkinter.ttk import Style, Notebook, Combobox, Frame
from lib.node import Node
from components.frames.config import BGWHITE, WHITE
from lib.global_variable import set_variable,get_variable

class GraphFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGWHITE,relief=GROOVE, borderwidth=1)
        self._parent = parent
        self._relationship = [None,None,None]
        self.__initUI()

    def __initUI(self):
        self.pack(side=LEFT, fill="both", expand=True)

        self._canvas = Canvas(self,bg=WHITE,bd=0, highlightthickness=0)
        self._canvas.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.item = None
        self.previous = (0,0)
        self._canvas.bind('<Button-1>',self.mouse_event)
        self._canvas.bind('<B1-Motion>',self.drag)
        self._canvas.bind('<ButtonRelease-1>',self.end_drag)
        self._parent.bind("<Key>",self.key_event)
        nodeList = get_variable("nodeList")
        
        A = Node(self._canvas,"A",300,200,10,30)
        B = Node(self._canvas,"B",100,150,60,30)
        C = Node(self._canvas,"C",200,250,60,30)
        D = Node(self._canvas,"D",500,300,120,30)
        
        A.add_child(B,30)
        A.add_child(C,10)
        C.add_child(D,50)
          
        #A._childNodes = [{"Node":B,"g":30},{"Node":C,"g":10}]
        #C._childNodes = [{"Node":D,"g":50}]

        nodeList = [A,B,C,D]
        set_variable("nodeList",nodeList)
    # ============================== KEY EVENT ============================== #

    def key_event(self,event):
        properties = get_variable("properties")
        toolList = get_variable("toolList")
        if(event.keysym == "Delete"):
            properties.delete_node()
        if(event.char == "\x11"):
            toolList[0].target_tool()
        if(event.char == "\x01"):
            toolList[1].target_tool()
        if(event.char == "\x1a"):
            toolList[2].target_tool()
        
    # ============================== MOUSE EVENT ============================== #

    def mouse_event(self,e):
        CREATENODE = "create-node"
        CURSOR = "cursor"
        RELATIONSHIP = "relationship"

        nameTool = get_variable("toolTarget")._nameTool
        nodeList = get_variable("nodeList")
        x = e.x
        y = e.y

        if(nameTool == CREATENODE):
            self.create_node(e)
            return
        
        if(nameTool == CURSOR):
            #check position
            self.previous = (x,y)
            for node in nodeList:
                iX = node._x
                iY = node._y
                if( x >= iX and x <= iX + 30 and y >= iY and y <= iY + 30):
                    self.item = node
                    return
            self.item = None
        
        if(nameTool == RELATIONSHIP):
            #find node start
            for i in nodeList:
                nodeX = i._x
                nodeY = i._y
                diameter = i._diameter
                if(x > nodeX and x < (nodeX + diameter) and y > nodeY and y < (nodeY + diameter)):
                    self._relationship[1] = i
                    return
            return       

    #=====Cursor=====#
    def drag(self, event):
        CURSOR = "cursor"
        RELATIONSHIP = "relationship"

        nameTool = get_variable("toolTarget")._nameTool
        x = event.x
        y = event.y

        #cursor
        if(nameTool == CURSOR):
            if(self.item == None):
                return

            widget = event.widget
            xc = widget.canvasx(x) - self.previous[0]
            yc = widget.canvasx(y) - self.previous[1]

            self.item.drag_node(xc,yc)

            self.item._x = self.item._x + xc
            self.item._y = self.item._y + yc
            self.previous = (xc + self.previous[0], yc + self.previous[1])
            return
        
        #relationship
        if(nameTool == RELATIONSHIP):
            nodeStart = self._relationship[1]
            if(nodeStart == None):
                return

            radius = nodeStart._diameter / 2
            if(self._relationship[0] != None):
                self._canvas.delete(self._relationship[0])

            Templine = self._canvas.create_line(nodeStart._x + radius,nodeStart._y + radius,x,y,arrow = LAST)
            self._relationship[0] = Templine

        

    def end_drag(self,event):
        CURSOR = "cursor"
        RELATIONSHIP = "relationship"
        properties = get_variable("properties")
        nameTool = get_variable("toolTarget")._nameTool
        nodeList = get_variable("nodeList")
        x = event.x
        y = event.y

        if(nameTool == CURSOR):
            self.item = None
            return
        
        if(nameTool == RELATIONSHIP):
            #delete line temp
            self._canvas.delete(self._relationship[0])

            if(self._relationship[1] == None):
                return

            #find node end
            for i in nodeList:
                nodeX = i._x
                nodeY = i._y
                diameter = i._diameter
                if(x > nodeX and x < (nodeX + diameter) and y > nodeY and y < (nodeY + diameter)):
                    self._relationship[2] = i  
            if(self._relationship[2] == None or self._relationship[1] == self._relationship[2]):
                return

            #add child
            relParent = self._relationship[1]
            relChild = self._relationship[2]
            flag = True
            for i in relParent._childNodes:
                if (i["Node"] == relChild):
                    flag = False
                    break
            
            if(flag):
                relParent.add_child(relChild,0)
            
            properties.target_node(relParent)
            properties.focus_cost(relChild)
            self._relationship = [None,None,None]
            return

    #=====Create node=====#
    def create_node(self,e):
        nodeList = get_variable("nodeList")
        properties = get_variable("properties")

        #check position
        x = e.x
        y = e.y
        for item in nodeList:
            iX = item._x
            iY = item._y
            if( x > iX - 20 and x < iX + 50 and y > iY - 20 and y < iY + 50):
                return
        
        #create new node
        newNode = Node(self._canvas,"",0,x-15,y-15,30)
        nodeList.append(newNode)
        properties.target_node(newNode)
    
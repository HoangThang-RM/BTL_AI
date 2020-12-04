from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox, Canvas,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame
from lib.node import Node
from components.frames.config import BGWHITE, WHITE
from lib.global_variable import set_variable,get_variable

class GraphFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGWHITE,relief=GROOVE, borderwidth=1)
        self._parent = parent
        self.__initUI()

    def __initUI(self):
        self.pack(side=LEFT, fill="both", expand=True)
        #label = Label(self,text="Đồ thị", pady=10,bg=WHITE ,font="Arial 18 bold")
        #label.pack(fill=BOTH)

        self._canvas = Canvas(self,bg=WHITE,bd=0, highlightthickness=0)
        self._canvas.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.item = None
        self.previous = (0,0)
        self._canvas.bind('<Button-1>',self.mouse_event)
        self._canvas.bind('<B1-Motion>',self.drag)
        self._canvas.bind('<ButtonRelease-1>',self.end_drag)
        nodeList = get_variable("nodeList")
        
        A = Node(self._canvas,"A",300,None,200,10,30)
        B = Node(self._canvas,"B",100,A,150,60,30)
        C = Node(self._canvas,"C",200,A,250,60,30)
        D = Node(self._canvas,"D",500,C,300,120,30)
        
        A.add_child(B,30)
        A.add_child(C,10)
        C.add_child(D,50)
          
        #A._childNodes = [{"Node":B,"g":30},{"Node":C,"g":10}]
        #C._childNodes = [{"Node":D,"g":50}]

        nodeList = [A,B,C,D]
        set_variable("nodeList",nodeList)
    
    # ============================== MOUSE EVENT ============================== #

    def mouse_event(self,e):
        CREATENODE = "create-node"
        CURSOR = "cursor"
        RELATIONSHIP = "relationship"

        nameTool = get_variable("toolTarget")._nameTool

        if(nameTool == CREATENODE):
            self.create_node(e)
            return
        
        if(nameTool == CURSOR):
            nodeList = get_variable("nodeList")

            #check position
            x = e.x
            y = e.y
            self.previous = (x,y)
            for node in nodeList:
                iX = node._x
                iY = node._y
                if( x >= iX and x <= iX + 30 and y >= iY and y <= iY + 30):
                    self.item = node
                    return
            self.item = None
            
        
    def drag(self, event):
        if(self.item == None):
            return

        widget = event.widget
        xc = widget.canvasx(event.x) - self.previous[0]
        yc = widget.canvasx(event.y) - self.previous[1]

        self._canvas.move(self.item._oval, xc, yc)
        self._canvas.move(self.item._txtOval, xc, yc)
        self._canvas.move(self.item._txtHeuristic, xc, yc)
        self.item.drag_arrow(xc,yc)

        self.item._x = self.item._x + xc
        self.item._y = self.item._y + yc
        self.previous = (xc + self.previous[0], yc + self.previous[1])

    def end_drag(self,event):
        self.item = None

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
        newNode = Node(self._canvas,"",0,None,x-15,y-15,30)
        nodeList.append(newNode)
        properties.target_node(newNode)
        properties.focus_name()

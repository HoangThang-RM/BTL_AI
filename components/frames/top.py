from tkinter import Button, Label, Entry, StringVar, Toplevel, Canvas, LAST, BOTH, GROOVE
from tkinter.ttk import Combobox, Frame
from components.frames.config import GREY,WHITE
from lib.global_variable import get_variable
from lib.intersection import ClosestIntersection
from lib.algorithm import BeFS,At,starA
from components.result import Result

class TopFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent,height="100",relief=GROOVE, borderwidth=1)
        self._parent = parent
        self.__initUI()
    
    def __initUI(self):
        self.pack(fill="x")

        label = Label(self,text="Thuật toán tối ưu",pady=10,font="Arial 18 bold",bg = GREY)
        label.pack(fill=BOTH)

        #frame Tool
        self.wrap = Frame(self, height="80")
        self.wrap.pack(fill=BOTH,pady=10)

        self.toolFrame = Frame(self.wrap)
        self.toolFrame.pack()

        self.alg_value = StringVar()
        self.algchoosen = Combobox(self.toolFrame, state="readonly", textvariable = self.alg_value, font="Arial 12")
        self.algchoosen["values"] = ("BeFS", "At", "Akt", "A*")
        self.algchoosen.current(0)
        self.algchoosen.grid(column=0,row=0,pady=2)


        button = Button(self.toolFrame, text="Tính", command=self.calculate)
        button.grid(column=1,row=0, padx=3, pady=2)
    
    def calculate(self):
        nameALG = self.alg_value.get()
        BEFS = "BeFS"
        AT = "At"
        AKT = "Akt"
        STARA = "A*"

        nodeList = get_variable("nodeList")
        result = []
        pointList = {}
        for node in nodeList:
            name = node._nameNode
            heuristic = float(node._heuristic)
            distanceTo = {}

            for child in node._childNodes:
                distanceTo[child["Node"]._nameNode] = float(child["cost"])
        
            pointList[name] = NodeALG(name,heuristic,distanceTo)
        
        if(nameALG == BEFS):
            result = BeFS(pointList,"A",["B"])
        elif(nameALG == AT):
            result = At(pointList,"A",["B"])
        elif(nameALG == STARA):
            result = starA(pointList,"A",["B"])
        
        print(result)
        Result(self._parent,result)

class NodeALG:
    def __init__(self,name = '',heuristic=0,distanceTo={}):
        self.name = name
        self.heuristic = heuristic
        self.distanceTo = distanceTo
    def __lt__(self,other):
        return self.heuristic < other.heuristic
    def __eq__(self,other):
        return self.heuristic == other.heuristic
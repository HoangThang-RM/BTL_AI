from tkinter import Button, Label, Entry, StringVar, Toplevel, messagebox,Canvas, LAST, BOTH, GROOVE
from tkinter.ttk import Combobox, Frame
from components.frames.config import GREY, WHITE, BEFS, AT, AKT, STARA, CAY, MATRAN
from lib.global_variable import get_variable
from lib.intersection import ClosestIntersection
from lib.algorithm import BeFS, At, starA, Akt_matrix
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
        self.algchoosen["values"] = (BEFS, AT, AKT, STARA)
        self.algchoosen.current(0)
        self.algchoosen.grid(column=0,row=0,pady=2)

        self.goalFrame = Frame(self.wrap)
        self.goalFrame.pack(pady=5)
        self.varNodeStart = StringVar()
        Label(self.goalFrame,text = "Bắt đầu",font="Arial 10",bg = GREY).grid(column=0,row = 0,padx=5,pady=5)
        Entry(self.goalFrame, textvariable = self.varNodeStart).grid(column=1,row=0,padx=5,pady=5)

        self.varNodeEnd = StringVar()
        Label(self.goalFrame,text = "Đích",font="Arial 10",bg = GREY).grid(column=2,row=0,padx=5,pady=5)
        Entry(self.goalFrame, textvariable = self.varNodeEnd).grid(column=3,row=0,padx=5,pady=5)

        button = Button(self.toolFrame, text="Tính", command=self.calculate)
        button.grid(column=1,row=0, padx=3, pady=2)
    
    def calculate(self):
        nameALG = self.alg_value.get()

        tabControl = get_variable("tabControl")
        matrix = get_variable("matrix")
        nameTab = tabControl.tab(tabControl.select(), "text")
        nodeList = get_variable("nodeList")
        result = []
        pointList = {}
        
        #Do thi cay
        if(nameTab == CAY):
            nodeStart = self.varNodeStart.get()
            nodeGoal = []
            for item in self.varNodeEnd.get().split(","):
                nodeGoal.append(item.strip())
            
            if(nodeStart == '' or nodeGoal == ''):
                messagebox.showwarning(title=None, message="Không được để trống điểm xuất phát và đích")
                return
            
            for node in nodeList:
                name = node._nameNode
                heuristic = float(node._heuristic)
                distanceTo = {}

                for child in node._childNodes:
                    distanceTo[child["Node"]._nameNode] = float(child["cost"])
            
                pointList[name] = NodeALG(name,heuristic,distanceTo)
            
            if(nameALG == BEFS):
                result = BeFS(pointList,nodeStart,nodeGoal)
            elif(nameALG == AT):
                result = At(pointList,nodeStart,nodeGoal)
            elif(nameALG == AKT):
                result = starA(pointList,nodeStart,nodeGoal)
            elif(nameALG == STARA):
                result = starA(pointList,nodeStart,nodeGoal)
        
        #Ma tran
        elif(nameTab == MATRAN):
            if(nameALG == AKT):
                height = matrix._height
                width = matrix._width
                matrixStart = matrix.get_cell_start()
                matrixEnd = matrix.get_cell_end()
                
                target = None
                firstStart = 0
                firstEnd = 0
                for i in range(height):
                    for j in range(width):
                        if(matrixStart[i][j] == ''):
                            firstStart = firstStart + 1
                            target = (i,j)
                        if(matrixEnd[i][j] == ''):
                            firstEnd = firstEnd + 1

                if(firstStart != 1 or firstEnd != 1):
                    messagebox.showwarning(title=None, message="Số ô trống phải là 1")
                    return
                result = Akt_matrix(matrixStart,matrixEnd,target,height,width)
            else:
                messagebox.showwarning(title=None, message="Bảng ma trận chỉ sử dụng với Akt")
                return
                
        Result(self._parent,result,nameTab)

class NodeALG:
    def __init__(self,name = '',heuristic=0,distanceTo={}):
        self.name = name
        self.heuristic = heuristic
        self.distanceTo = distanceTo
    def __lt__(self,other):
        return self.heuristic < other.heuristic
    def __eq__(self,other):
        return self.heuristic == other.heuristic
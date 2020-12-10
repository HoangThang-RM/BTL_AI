from tkinter import Label, Entry, StringVar, Toplevel, Canvas, Scrollbar
from tkinter import LAST, BOTH, GROOVE,TOP,RIGHT,LEFT,HORIZONTAL,VERTICAL,E,W,N,S,CENTER,DISABLED
from tkinter.ttk import Frame
from components.frames.config import GREY, WHITE,BGWHITE, CAY, MATRAN
from lib.global_variable import get_variable
from lib.intersection import ClosestIntersection
DEPTH = 30
class Result:
    def __init__(self,parent,result,tab):
        self._parent = parent
        self._resultWindow = Toplevel(parent)
        self._resultWindow.title("Kết quả")
        self._resultWindow.geometry("800x800")

        self._mainFrame = Frame(self._resultWindow,style=BGWHITE)
        self._mainFrame.pack(fill = BOTH, expand=True)
        
        #show result
        if(tab == CAY):
            self.show_graph(result)
        if(tab == MATRAN):
            self.show_matrix(result)

    def show_graph(self,result):
        self._label = Label(self._mainFrame,text="Kết quả",pady=10,font="Arial 18 bold",bg = WHITE)
        self._label.pack()
        self._canvas = Canvas(self._mainFrame,bg=WHITE,bd=0,highlightthickness=0)
        self._canvas.pack(fill=BOTH,expand=True)
        nodeList = get_variable("nodeList")
        originX,originY = self.find_origin_coor()

        for node in nodeList:
            x = node._x - originX
            y = node._y - originY
            diameter = node._diameter
            radius = int(diameter/2)
            nameNode = node._nameNode
            heuristic = node._heuristic
            
            isWay = False
            index = None
            for i,item in enumerate(result):
                if(item == nameNode):
                    isWay = True
                    index = i + 1
            if(isWay):
                self._canvas.create_oval(x,y,x+diameter,y+diameter, width="2",outline="red")
            else:
                self._canvas.create_oval(x,y,x+diameter,y+diameter, width="2")
            
            self._canvas.create_text(x+diameter/2,y+diameter/2,text=nameNode,font="TkDefaultFont 10 bold")
            self._canvas.create_text(x + diameter + 5, y - 5,text = heuristic,fill="blue")

            #draw arrows
            for child in node._childNodes:
                x1 = x + radius
                y1 = y + radius
                x2 = child["Node"]._x + radius - originX
                y2 = child["Node"]._y + radius - originY

                pointStart = ClosestIntersection(x1,y1,radius,(x2,y2),(x1,y1))
                pointEnd = ClosestIntersection(x2,y2,radius,(x1,y1),(x2,y2))

                if(index == None):
                    arrow = self._canvas.create_line(pointStart[0],pointStart[1],pointEnd[0],pointEnd[1],arrow = LAST)
                elif(index >= len(result)):
                    arrow = self._canvas.create_line(pointStart[0],pointStart[1],pointEnd[0],pointEnd[1],arrow = LAST)
                elif(child["Node"]._nameNode == result[index]):
                    arrow = self._canvas.create_line(pointStart[0],pointStart[1],pointEnd[0],pointEnd[1],arrow = LAST,fill="red")
                else:
                    arrow = self._canvas.create_line(pointStart[0],pointStart[1],pointEnd[0],pointEnd[1],arrow = LAST)
                self._canvas.tag_lower(arrow)
                
                #show cost
                cost = child["cost"]
                xCost = int((pointStart[0]+pointEnd[0])/2)
                if(pointStart[0] > pointEnd[0]):
                    xCost -= 10
                else:
                    xCost += 10
                yCost = int((pointStart[1]+pointEnd[1])/2) - 10
                self._canvas.create_text(xCost,yCost,text = cost, font="TkDefaultFont 10 bold")
    
    def show_matrix(self,result):
        #scroll
        self._canvasScroll = Canvas(self._mainFrame,bg=WHITE,bd=0,highlightthickness=0)
        self._canvasScroll.pack(side=LEFT,fill=BOTH,expand=True)
        self._scroolbar = Scrollbar(self._mainFrame, orient = VERTICAL, command = self._canvasScroll.yview)
        self._scroolbar.pack(side=RIGHT, fill="y")
        self._canvasScroll.configure(yscrollcommand = self._scroolbar.set)
        self._canvasScroll.bind('<Configure>', lambda e: self._canvasScroll.configure(scrollregion = self._canvasScroll.bbox("all")))
        self._cover = Frame(self._canvasScroll,style=BGWHITE)
        self._canvasScroll.create_window((0,0), window = self._cover)
        #title
        self._label = Label(self._cover,text="Kết quả",pady=10,font="Arial 18 bold",bg = WHITE)
        self._label.pack()
        

        height = result["height"]
        width = result["width"]
        matrix = result["matrix"]
        count = 0
        oldWay = result["listWay"][0]["coor"]
        #result["way"].pop(0)
        print(result["listWay"])
        for way in result["listWay"]:
            row = way["coor"][0]
            column = way["coor"][1]
            row_ = oldWay[0]
            column_ = oldWay[1]

            count = count + 1
            if(count > 1):
                Label(self._cover,text="|",pady=0,font="Arial 12 bold",bg = WHITE).pack()
                Label(self._cover,text="|",pady=0,font="Arial 12 bold",bg = WHITE).pack()
                Label(self._cover,text="V",pady=0,font="Arial 12 bold",bg = WHITE).pack()
            #swap
            tempVal = matrix[row][column]
            matrix[row][column] = matrix[row_][column_]
            matrix[row_][column_] = tempVal
            oldWay = way["coor"]
            print(matrix)
            frmMatrix =Frame(self._cover,style=BGWHITE)
            frmMatrix.pack(side=TOP,pady=20)
            for i in range(height):
                for j in range(width):
                    mystr = StringVar()
                    ent = Entry(frmMatrix,textvariable = mystr,width=5,borderwidth=2,relief=GROOVE,state=DISABLED)
                    ent.grid(row = i, column = j)
                    mystr.set(matrix[i][j])
                    h = "h = " + str(way["h"])
                    g = "g = " + str(way["g"])
                    f = "f = " + str(way["f"])
                    Label(frmMatrix,text=h,font="Arial 10",bg = WHITE).grid(row = 0, column = width+1)
                    Label(frmMatrix,text=g,font="Arial 10",bg = WHITE).grid(row = 1, column = width+1)
                    Label(frmMatrix,text=f,font="Arial 10",bg = WHITE).grid(row = 2, column = width+1)
                    
        if(result["isResult"]):
            mess = "Đã tìm được đích!"
        else:
            mess = "Sau " + str(DEPTH) + " lần vẫn chưa tìm được đích!"
        Label(self._cover,text=mess,pady=10,font="Arial 12 bold",bg = WHITE).pack(padx=350,pady=50)

    def find_origin_coor(self):
        nodeList = get_variable("nodeList")
        originX = None
        originY = None
        originMaxX = None
        
        first = True
        for node in nodeList:
            if(first == True):
                originX = node._x
                originY = node._y
                originMaxX = node._x
                first = False
                continue
            
            if(originX > node._x):
                originX = node._x
            
            if(originY > node._y):
                originY = node._y

            if(originMaxX < node._x):
                originMaxX = node._x
            
        delt = int((800 - (originMaxX-originX))/2)
        if(delt > 0):
            originX = originX - delt
        originY = originY - 50

        return originX,originY
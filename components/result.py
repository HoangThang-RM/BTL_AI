from tkinter import Label, Entry, StringVar, Toplevel, Canvas, LAST, BOTH, GROOVE
from components.frames.config import GREY,WHITE
from lib.global_variable import get_variable
from lib.intersection import ClosestIntersection

class Result:
    def __init__(self,parent,result):
        self._parent = parent
        self._resultWindow = Toplevel(parent)
        self._resultWindow.title("Kết quả")
        self._resultWindow.geometry("800x800")
        
        self._label = Label(self._resultWindow,text="Kết quả",pady=10,font="Arial 18 bold",bg = WHITE)
        self._label.pack(fill=BOTH)
        
        self._canvas = Canvas(self._resultWindow,bg=WHITE,bd=0, highlightthickness=0)
        self._canvas.pack(fill=BOTH, expand=True,padx=5,pady=5)

        self.show_graph(result)

    def show_graph(self,result):
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
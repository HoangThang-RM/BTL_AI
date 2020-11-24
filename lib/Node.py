from tkinter import Label,LAST
from lib.global_variable import get_variable

class Node():
    def __init__(self,canvas,nameNode,heuristic,parentNodes,x,y,diameter,color="white"):
        self._parentNodes = parentNodes
        self._childNodes = []
        self._nameNode = nameNode
        self._heuristic = heuristic
        self._canvas = canvas
        self._x = x
        self._y = y
        self._diameter = diameter

        self.__initUI(nameNode,x,y,diameter,color)

    def __initUI(self,nameNode,x,y,diameter,color):
        self._oval = self._canvas.create_oval(x,y,x+diameter,y+diameter, width="2", fill=color)
        self._txtOval =  self._canvas.create_text(x+diameter/2,y+diameter/2,text=nameNode,font="TkDefaultFont 10 bold")
        self._txtHeuristic = self._canvas.create_text(x + diameter + 5, y - 5,text = self._heuristic,fill="blue")
        
        self._canvas.tag_bind(self._oval,'<ButtonRelease>', lambda event: self.clicked())
        self._canvas.tag_bind(self._txtOval,'<ButtonRelease>', lambda event: self.clicked())
        self._canvas.tag_bind(self._oval, "<Enter>", lambda event: self.check_hand_enter())
        self._canvas.tag_bind(self._txtOval, "<Enter>", lambda event: self.check_hand_enter())
        self._canvas.tag_bind(self._oval, "<Leave>", lambda event: self.check_hand_leave())
        self._canvas.tag_bind(self._txtOval, "<Leave>", lambda event: self.check_hand_leave())


    def check_hand_enter(self):
        self._canvas.config(cursor="hand2")

    def check_hand_leave(self):
        self._canvas.config(cursor="")

    def clicked(self):
        inforFrame = get_variable("inforFrame")
        print(self._nameNode)
        inforFrame.edit(self)

    def add_child(self,node,cost):
        x1 = self._x + self._diameter/2
        y1 = self._y + self._diameter/2
        x2 = node._x + node._diameter/2
        y2 = node._y
        #draw diagonal arrows
        arrow = self._canvas.create_line(x1,y1,x2,y2,arrow = LAST, width="2")
        self._canvas.tag_lower(arrow)
        
        #show cost
        xCost = int((x1+x2)/2)
        if(x1 > x2):
            xCost -= 10
        else:
            xCost += 10
        yCost = int((y1+y2)/2) - 10
        txtCost = self._canvas.create_text(xCost,yCost,text = cost, font="TkDefaultFont 10 bold")

        #add to chilNodes
        child = {"Node":node,"g":cost,"arrow":arrow,"txtCost":txtCost}
        self._childNodes.append(child)

    def remove_child(self,node):
        for item in self._childNodes:
            if(item.get("Node") == node):
                #destroy arrow
                item.get("arrow").destroy()
                self._childNodes.remove(item)
                return

    def edit_node(self,name = None,heuristic = None, child = None):
        if(name != None):
            self._nameNode = name
            self._canvas.itemconfig(self._txtOval, text=name)
        
        if(heuristic != None):
            self._heuristic = heuristic
            self._canvas.itemconfig(self._txtHeuristic, text=heuristic)
        
        if(child != None):
            for item in self._childNodes:
                if(item.get("Node") == child.get("Node")):
                    item["g"] = child.get("g")
                    self._canvas.itemconfig(item.get("txtCost"), txt = child.get("g"))
                    break
            
                
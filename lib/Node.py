from tkinter import Label,LAST
from lib.global_variable import get_variable
from lib.intersection import ClosestIntersection

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
        
        self._canvas.tag_bind(self._oval,'<ButtonRelease-1>', lambda event: self.clicked())
        self._canvas.tag_bind(self._txtOval,'<ButtonRelease-1>', lambda event: self.clicked())
        self._canvas.tag_bind(self._oval, "<Enter>", lambda event: self.check_hand_enter())
        self._canvas.tag_bind(self._txtOval, "<Enter>", lambda event: self.check_hand_enter())
        self._canvas.tag_bind(self._oval, "<Leave>", lambda event: self.check_hand_leave())
        self._canvas.tag_bind(self._txtOval, "<Leave>", lambda event: self.check_hand_leave())

    def check_hand_enter(self):
        self._canvas.config(cursor="hand2")

    def check_hand_leave(self):
        self._canvas.config(cursor="")

    def clicked(self):
        properties = get_variable("properties")
        properties.target_node(self)


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
                    item["cost"] = child.get("cost")
                    self._canvas.itemconfig(item.get("txtCost"), txt = child.get("cost"))
                    break
    
    # ============================== Child Node  ============================== #
    
    def add_child(self,node,cost):
        coorParent = (self._x,self._y)
        coorChild = (node._x,node._y)
        arrow, txtCost = self.create_arrow(coorParent,coorChild,cost)

        #add to chilNodes
        child = {"Node":node,"cost":cost,"arrow":arrow,"txtCost":txtCost}   
        self._childNodes.append(child)
        node._parentNodes.append(self)

    def create_arrow(self,coorParent,coorChild,cost): 
        #coordinates of the center of the circle
        radius = self._diameter/2
        x1 = coorParent[0] + radius
        y1 = coorParent[1] + radius
        x2 = coorChild[0] + radius
        y2 = coorChild[1] + radius
        pointStart = ClosestIntersection(x1,y1,radius,(x2,y2),(x1,y1))
        pointEnd = ClosestIntersection(x2,y2,radius,(x1,y1),(x2,y2))
        #draw diagonal arrows
        arrow = self._canvas.create_line(pointStart[0],pointStart[1],pointEnd[0],pointEnd[1],arrow = LAST)
        self._canvas.tag_lower(arrow)
        
        #show cost
        xCost = int((pointStart[0]+pointEnd[0])/2)
        if(pointStart[0] > pointEnd[0]):
            xCost -= 10
        else:
            xCost += 10
        yCost = int((pointStart[1]+pointEnd[1])/2) - 10
        txtCost = self._canvas.create_text(xCost,yCost,text = cost, font="TkDefaultFont 10 bold")

        return arrow,txtCost
    
    def remove_child(self,node):
        for item in self._childNodes:
            if(item.get("Node") == node):
                #destroy arrow
                item.get("arrow").destroy()
                self._childNodes.remove(item)
                return

    def drag_arrow(self,xc,yc):
        #for child
        for child in self._childNodes:
            node = child["Node"]
            #destroy 
            self._canvas.delete(child["arrow"])
            self._canvas.delete(child["txtCost"])

            #create new arrow
            cost = child.get("cost")
            coorParent = (self._x,self._y)
            coorChild = (node._x,node._y)
            arrow,txtCost = self.create_arrow(coorParent,coorChild,cost)
            child["arrow"] = arrow
            child["txtCost"] = txtCost

        #for parent
        for parent in self._parentNodes:
            for child in parent._childNodes:
                if(child["Node"] == self):
                    #destroy 
                    parent._canvas.delete(child["arrow"])
                    parent._canvas.delete(child["txtCost"])

                    #create new arrow
                    cost = child.get("cost")
                    coorParent = (parent._x,parent._y)
                    coorChild = (self._x,self._y)
                    arrow,txtCost = self.create_arrow(coorParent,coorChild,cost)
                    child["arrow"] = arrow
                    child["txtCost"] = txtCost
                    break
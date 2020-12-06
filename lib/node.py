from tkinter import Label,LAST
from lib.global_variable import get_variable
from lib.intersection import ClosestIntersection

class Node():
    def __init__(self,canvas,nameNode,heuristic,x,y,diameter,color="white"):
        self._parentNodes = []
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

    # ==============================  Node  ============================== #
    
    def edit_node(self,name = None,heuristic = None, child = None):
        if(name != None):
            self._nameNode = name
            self._canvas.itemconfig(self._txtOval, text=name)
        
        if(heuristic != None):
            self._heuristic = heuristic
            self._canvas.itemconfig(self._txtHeuristic, text=heuristic)
        
        if(child != None):
            childNode = child[0]
            cost = child[1]
            for item in self._childNodes:
                if(item.get("Node") == childNode):
                    self._canvas.delete(item["arrow"])
                    self._canvas.delete(item["txtCost"])
                    
                    
                    arrow, txtCost = self.create_arrow((self._x,self._y),(childNode._x,childNode._y),cost)
                    item["cost"] = cost
                    item["arrow"] = arrow
                    item["txtCost"] = txtCost
                    break

    def delete(self):
        nodeList = get_variable("nodeList")
        self._canvas.delete(self._oval)
        self._canvas.delete(self._txtOval)
        self._canvas.delete(self._txtHeuristic)

        for node in nodeList:
            if(node == self):
                nodeList.remove(node)

        while(self._childNodes != []):
            self.remove_child(self._childNodes[0]["Node"])

        while(self._parentNodes != []):
            self.remove_parent(self._parentNodes[0])

        properties = get_variable("properties")
        properties.target_node()
    # ============================== Child Node  ============================== #
    
    def add_child(self,node,cost):
        coorParent = (self._x,self._y)
        coorChild = (node._x,node._y)
        arrow, txtCost = self.create_arrow(coorParent,coorChild,cost)

        #add to chilNodes
        child = {"Node":node,"cost":cost,"arrow":arrow,"txtCost":txtCost}   
        self._childNodes.append(child)
        node._parentNodes.append(self)
        self.sort_child()

    def remove_child(self,child):
        for item in self._childNodes:
            if(item["Node"] == child):
                #remove child
                self._canvas.delete(item["arrow"])
                self._canvas.delete(item["txtCost"])
                self._childNodes.remove(item)
                #remove parent
                for parent in item["Node"]._parentNodes:
                    if(parent == self):
                        item["Node"]._parentNodes.remove(parent)
                break

        properties = get_variable("properties")
        properties.target_node(self)
        
    def remove_parent(self,parent):
        for item in self._parentNodes:
            if(item == parent):
                item.remove_child(self)

        properties = get_variable("properties")
        properties.target_node(self)

    def sort_child(self):
        self._childNodes.sort(key=self.get_x)
    def get_x(self,element):
        return element["Node"]._x
    
    # ============================== Move Node ============================== #

    def create_arrow(self,coorParent,coorChild,cost): 
        #coordinates of the center of the circle
        radius = int(self._diameter/2)
        x1 = coorParent[0] + radius
        y1 = coorParent[1] + radius
        x2 = coorChild[0] + radius
        y2 = coorChild[1] + radius
        pointStart = ClosestIntersection(x1,y1,radius,(x2,y2),(x1,y1))
        pointEnd = ClosestIntersection(x2,y2,radius,(x1,y1),(x2,y2))
        #draw arrows
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

    def drag_node(self,xc,yc):
        self._canvas.move(self._oval, xc, yc)
        self._canvas.move(self._txtOval, xc, yc)
        self._canvas.move(self._txtHeuristic, xc, yc)
        
        #for arrow of child
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

        #for arrow of parent
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
        #sort
        for parent in self._parentNodes:
            parent.sort_child()
        
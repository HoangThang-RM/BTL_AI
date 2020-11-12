from Circle import *
class Node(Circle):
    def __init__(self,parentNodes,chilNodes,canvas,x,y,diameter,color,nameNode):
        Circle.__init__(self,canvas,x,y,diameter,color,nameNode)
        self.parentNodes = parentNodes
        self.chilNodes = chilNodes


from lib.Circle import Circle

class Node(Circle):
    def __init__(self,parentNodes,childNodes,canvas,x,y,diameter,color,nameNode):
        self._parentNodes = parentNodes
        self._childNodes = childNodes
        self.nameNode = nameNode
        Circle.__init__(self,canvas,x,y,diameter,color,nameNode)


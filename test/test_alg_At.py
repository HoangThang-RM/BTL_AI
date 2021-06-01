import os
import sys
from unittest import result
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.algorithm import At, starA, BeFS
from lib.node import Node
import unittest


class NodeALG:
    def __init__(self,name = '',heuristic=0,distanceTo={}):
        self.name = name
        self.heuristic = heuristic
        self.distanceTo = distanceTo
    def __lt__(self,other):
        return self.heuristic < other.heuristic
    def __eq__(self,other):
        return self.heuristic == other.heuristic

def create_point_list():
    A = Node(None,"A",1000,150,20,30)
    C = Node(None,"C",25,100,100,30)
    D = Node(None,"D",20,200,100,30)
    E = Node(None,"E",24,300,100,30)
    F = Node(None,"F",22,400,20,30)
    H = Node(None,"H",16,180,200,30)
    I = Node(None,"I",17,450,200,30)
    K = Node(None,"K",11,250,250,30)
    B = Node(None,"B",0,150,250,30)

    A.add_child(C,17)
    A.add_child(D,12)
    A.add_child(E,15)
    A.add_child(F,20)
    
    D.add_child(E,8)
    D.add_child(H,10)

    E.add_child(I,4)
    E.add_child(K,5)

    H.add_child(K,1)
    H.add_child(B,18)

    K.add_child(B,8)
    nodeList = [A,C,D,E,F,H,K,I,B]
    pointList = {}
    for node in nodeList:
        name = node._nameNode
        heuristic = float(node._heuristic)
        distanceTo = {}

        for child in node._childNodes:
            distanceTo[child["Node"]._nameNode] = float(child["cost"])

        pointList[name] = NodeALG(name,heuristic,distanceTo)
    
    return pointList

class TestAlgAt(unittest.TestCase):  
    def setUp(self):
        self.pointList = create_point_list()
        pass
    
    def tearDown(self):
        self.pointList = None
        pass  
    
    # test case với trường hợp không có điểm bắt đầu và điểm đích
    def test_case_1(self):
        result = []
        self.assertEqual( At(self.pointList,"",""), result)
    
    # test case với trường hợp có điểm bắt đầu và nhưng không có điểm đích
    def test_case_2(self):
        result = []
        self.assertEqual( At(self.pointList,"A",""), result)

    # test case với trường hợp có không có điểm bắt đầu và có điểm đích
    def test_case_3(self):
        result = []
        self.assertEqual( At(self.pointList,"","B"), result)
    
    # test case với trường hợp có điểm bắt đầu không tồn tại
    def test_case_4(self):
        result = []
        self.assertEqual( At(self.pointList,"O","B"), result)

    # test case với trường hợp có điểm kết thúc không tồn tại
    def test_case_5(self):
        result = []
        self.assertEqual( At(self.pointList,"A","O"), result)

    # test case với trường hợp điểm bắt đầu là A và điểm đích là B
    def test_case_6(self):
        result = ['A', 'E', 'K', 'B']
        self.assertEqual( At(self.pointList,"A","B"), result)
    
    # test case với trường hợp điểm bắt đầu là A và điểm đích là K
    def test_case_7(self):
        result = ['A', 'E', 'K']
        self.assertEqual( At(self.pointList,"A","K"), result)
        
    # test case với trường hợp điểm bắt đầu là A và điểm đích là I
    def test_case_8(self):
        result = ['A', 'E', 'I']
        self.assertEqual( At(self.pointList,"A","I"), result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
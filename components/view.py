from tkinter import Tk,Canvas,LAST,Frame,Button,LEFT,RIGHT, NO, NONE, GROOVE
from components.frames import (bottom,top,temp,graph,inforNode,style,tool)
from lib.Node import Node 

class MainPage():
    def __init__(self):
        self._window = Tk()
        self._window.title("thuật toán tối ưu")
        self._window.geometry("1000x800")
        
        self.main_window(self._window)

        self._window.mainloop()

    def main_window(self,window):
        
        #temp.TopFrame(self._window)
        top.TopFrame(self._window)
        bottom.BottomFrame(self._window)
        tool.ToolLeft(self._window)
        graph.GraphFrame(self._window)
        inforNode.InforNodeRight(self._window)
        style.CreateStyle(self._window)
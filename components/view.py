from tkinter import Tk,Canvas,LAST,Frame,Button,LEFT,RIGHT, NO, NONE, GROOVE
from components.frames import (bottom,top,tab,properties,style,tool)
from lib.global_variable import set_variable,get_variable
from lib.node import Node 

class MainPage():
    def __init__(self):
        self._window = Tk()
        self._window.title("thuật toán tối ưu")
        self._window.geometry("1000x800")
        
        self.main_window(self._window)

        self._window.mainloop()

    def main_window(self,window):
        style.CreateStyle(self._window)
        
        top.TopFrame(self._window)
        bottom.BottomFrame(self._window)
        tool.ToolLeft(self._window)
        tab.TabFrame(self._window)
        ppts = properties.Properties(self._window)

        set_variable("properties",ppts)
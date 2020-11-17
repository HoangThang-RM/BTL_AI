from tkinter import Tk,Canvas,LAST,Frame,Button,LEFT,RIGHT, NO, NONE, GROOVE
from components.frames import (ToolLeft, TopFrame, BottomFrame,
                             InforNodeRight,CanvasFrame,CreateStyle)
from lib.Node import Node 

class MainPage():
    def __init__(self):
        self._window = Tk()
        self._window.title("thuật toán tối ưu")
        self._window.geometry("1000x800")
        
        self.main_window(self._window)

        self._window.mainloop()

    def main_window(self,window):
        CreateStyle(self._window)

        TopFrame(self._window)
        BottomFrame(self._window)
        ToolLeft(self._window)
        CanvasFrame(self._window)
        InforNodeRight(self._window)
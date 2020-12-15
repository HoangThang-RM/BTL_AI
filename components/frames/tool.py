from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from PIL import ImageTk, Image
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE,FLAT
from tkinter.ttk import Style, Combobox, Frame
from lib.global_variable import set_variable,get_variable
import os

class ToolLeft(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,width="30" ,relief=GROOVE, borderwidth=1)
        self._parent = parent
        self.__initUI()
  
    def __initUI(self):
        self.pack(side=LEFT,fill="y")
        cursor = Tool(self,'cursor','cursor-32.png')
        cursor.target_tool()
        createNode = Tool(self,'create-node','circle-32.png')
        relationship = Tool(self,'relationship','up-arrow-32.png')
        set_variable("toolList",[cursor,createNode,relationship])
        
class Tool(Frame):
    
    def __init__(self, parent,nameTool,nameImg):
        Frame.__init__(self, parent,relief=FLAT, borderwidth=5)
        self._parent = parent
        self._nameTool = nameTool
        self._pathImgFolder = os.path.abspath(__file__ + '/../../../data/image/')
        self.__initUI(nameImg)
  
    def __initUI(self,nameImg):
        self.pack(side=TOP,pady="1",padx="1")

        size = 20, 20
        pathImg = (os.path.abspath(self._pathImgFolder + '/' + nameImg))
        img = Image.open(pathImg)
        img.thumbnail(size, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(img)

        label = Label(self, image=render)
        label.photo = render
        label.pack()

        label.bind("<Button-1>", self.target_tool)
        self.bind("<Button-1>", self.target_tool)

    def target_tool(self,e = None):
        toolTarget = get_variable('toolTarget')
        if(toolTarget != None):
            toolTarget.config(relief = FLAT)
        self.config(relief = GROOVE)
        
        set_variable('toolTarget',self)
        
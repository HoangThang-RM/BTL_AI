from tkinter import (Button, Label, Entry, LabelFrame, StringVar, messagebox,
                     Listbox,OptionMenu, scrolledtext,ttk)
from tkinter import Tk, END, LEFT, RIGHT, TOP, BOTTOM,CENTER, BOTH, RAISED, GROOVE
from tkinter.ttk import Style, Combobox, Frame

GREY = "#f5f5f5"
DARKGREY ="#e4e4e4"
WHITE = "#ffffff"
BGWHITE = "bgWhite.TFrame"
BGGREY = "bgGrey.TFrame"
BGDARKGREY = "bgDarkGrey.TFrame"

class CreateStyle():
    def __init__(self, parent):
        self.parent = parent
        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure('bgWhite.TFrame', background=WHITE)
        self.style.configure('bgGrey.TFrame', background=GREY)
        self.style.configure('bgDarkGrey.TFrame', background=DARKGREY)
        self.parent.option_add('*TCombobox*Listbox.selectBackground', 'yellow')
        self.parent.option_add('*TCombobox*Listbox.selectForeground', 'black')

class CanvasFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGWHITE)
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.pack(side=LEFT, fill="both", expand=True)

        mainFrame = Frame(self, style=BGWHITE,relief=GROOVE, borderwidth=1)
        mainFrame.pack(side=LEFT, fill="both", expand=True)
        
        label = Label(mainFrame,text="Đồ thị", pady=10,bg=WHITE ,font="Arial 18 bold")
        label.pack(fill=BOTH)
        
        

class TopFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGGREY)
        self.parent = parent
        self.__initUI()
    
    def __initUI(self):
        #self.parent.title("Button")
        self.style = Style()
        self.pack(fill=BOTH)

        mainFrame = Frame(self,height="100",style=BGGREY,relief=GROOVE, borderwidth=1)
        mainFrame.pack(fill=BOTH, expand=True)

        label = Label(mainFrame,text="Thuật toán tối ưu", pady=10, bg=GREY,font="Arial 18 bold")
        label.pack(fill=BOTH)

        #frame Tool
        wrap = Frame(mainFrame, height="80", style=BGGREY)#,relief=GROOVE, borderwidth=1) 
        wrap.pack(fill=BOTH,pady=10)

        toolFrame = Frame(wrap, style=BGGREY)#,relief=GROOVE, borderwidth=1)
        toolFrame.pack()

        alg_value = StringVar()
        algchoosen = Combobox(toolFrame, state="readonly", textvariable = alg_value, font="Arial 12")
        algchoosen["values"] = ("Thuật toán 1", "Thuật toán 2", "Thuật toán 3", "Thuật toán 4")
        algchoosen.current(0)
        algchoosen.grid(column=0,row=0,pady=2)

        def btnClicked():
            print(alg_value.get())
        button = Button(toolFrame, text="Tính", command=btnClicked)
        button.grid(column=1,row=0, padx=3, pady=2)
        



class ToolLeft(Frame):
    def __init__(self, parent):
        #Frame.__init__(self, parent, style='App.TFrame')
        Frame.__init__(self, parent, style=BGGREY ,relief=GROOVE)
        self.parent = parent
        self.__initUI()
  
    def __initUI(self):
        self.style = Style()
        self.pack(side=LEFT,fill="y")

        mainFrame = Frame(self.parent, width="30", style=BGGREY,relief=GROOVE, borderwidth=1)
        mainFrame.pack(side=LEFT,fill="y")

class InforNodeRight(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,style=BGGREY)
        self.parent = parent
        self.__initUI()
  
    def __initUI(self):
        self.style = Style()
        self.pack(side=RIGHT,fill="y")
    
        mainFrame = Frame(self, width="200",style=BGGREY, relief=GROOVE, borderwidth=1)
        mainFrame.pack(side=RIGHT,fill="y")
        

class BottomFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, style=BGGREY)
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.style = Style()
        self.pack(side=BOTTOM,fill="x")

        mainFrame = Frame(self, height="30", style=BGGREY, relief=GROOVE, borderwidth=1)
        mainFrame.pack(side=BOTTOM,fill="x")

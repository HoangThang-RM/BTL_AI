from tkinter.ttk import Style
from components.frames.config import GREY,WHITE,DARKGREY,BGWHITE,BGGREY,BGDARKGREY

class CreateStyle():
    def __init__(self, parent):
        self.parent = parent
        self.style = Style()
        #self.style.theme_create("light", parent= "clam")
        self.style.theme_use("clam")
        
        #self.style.configure('TButton', foreground = 'white', background = 'blue')
        self.style.configure('TFrame', background = GREY)
        self.style.configure(BGWHITE, background=WHITE)
        self.style.configure(BGDARKGREY, background=DARKGREY)

        self.parent.option_add('*Label.bg', 'red')        
        self.parent.option_add('*TCombobox*Listbox.selectBackground', 'yellow')
        self.parent.option_add('*TCombobox*Listbox.selectForeground', 'black')
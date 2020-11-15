class Circle:

    def __init__(self,canvas,x,y,diameter,color,txt):
        self._canvas = canvas
        canvas.create_oval(x,y,x+diameter,y+diameter,fill=color,tags="shape")
        canvas.create_text(x+diameter/2,y+diameter/2,text=txt,tags="shape")
        
        canvas.tag_bind("shape",'<ButtonRelease>', lambda event: self.clicked())
        canvas.tag_bind("shape", "<Enter>", lambda event: self.check_hand_enter())
        canvas.tag_bind("shape", "<Leave>", lambda event: self.check_hand_leave())
    
    def check_hand_enter(self):
        self._canvas.config(cursor="hand2")

    def check_hand_leave(self):
        self._canvas.config(cursor="")
    def clicked(self):
        print("clicked")
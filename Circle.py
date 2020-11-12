class Circle:
    def __init__(self,canvas,x,y,diameter,color,txt):
        def check_hand_enter():
            canvas.config(cursor="hand2")

        def check_hand_leave():
            canvas.config(cursor="")

        self.canvas = canvas
        self.image = canvas.create_oval(x,y,x+diameter,y+diameter,fill=color,tags="img")
        self.txt = canvas.create_text(x+diameter/2,y+diameter/2,text=txt,tags="img")
        
        #canvas.tag_bind("img","<Button-1>",clicked)
        canvas.tag_bind("img", "<Enter>", lambda event: check_hand_enter())
        canvas.tag_bind("img", "<Leave>", lambda event: check_hand_leave())
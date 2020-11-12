from tkinter import *
from tkinter.ttk import *
from Node import *
import tkinter

#root = tkinter.Tk()

window = Tk()
window.title("thuật toán tối ưu")
window.geometry("800x600")

#canvas
canvas = Canvas(window,width=600,height=600)
canvas.pack()
Node("","",canvas,10,10,30,"white","D")

canvas.create_line(10+15, 10+30, 30+15, 80, arrow=LAST)
Node("","",canvas,30,80,30,"white","E")

canvas.create_line(30+15, 80+30, 50+15, 160, arrow=LAST)
Node("","",canvas,50,160,30,"white","F")


canvas.grid(column = 0, row = 3)

window.mainloop()
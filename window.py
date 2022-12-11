from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=400, background="#eeeeee")
canvas.bind("<Button-1>", lambda e: canvas.create_text(e.x, e.y, text="owo"))

canvas.pack()
root.mainloop()
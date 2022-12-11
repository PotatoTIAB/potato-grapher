from tkinter import *

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.canvas = Plane(self, width=500, height=400, background="#eeeeee")

		self.canvas.pack()

class Plane(Canvas):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.bind("<Button-1>", lambda e: self.create_text(e.x, e.y, text="owo"))


root = Window()
root.mainloop()
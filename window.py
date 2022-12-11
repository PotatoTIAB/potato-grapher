from tkinter import *



class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.canvas = Plane(self, width=500, height=400, background="#eeeeee")

		self.canvas.pack()



class Plane(Canvas):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.bind("<Button-1>", self.on_click)
		self.bind("<B1-Motion>", self.on_motion)
		self.x = 0
		self.y = 0
	

	def on_click(self, event: Event):
		self.x, self.y = event.x, event.y


	def on_motion(self, event: Event):
		self.create_line(self.x, self.y, event.x, event.y)
		self.x, self.y = event.x, event.y


root = Window()
root.mainloop()
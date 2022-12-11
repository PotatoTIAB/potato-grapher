from tkinter import *



class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.canvas = Plane(self, width=400, height=400, background="#eeeeee")

		self.canvas.pack()



class Plane(Canvas):
	def __init__(self, *args, padding=50, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.width = kwargs["width"]
		self.height = kwargs["height"]
		self.padding = padding

		self.bind("<Button-1>", self.on_click)
		self.bind("<B1-Motion>", self.on_motion)
		self.x = 0
		self.y = 0

		self.draw_plane()
	

	def on_click(self, event: Event):
		self.x, self.y = event.x, event.y


	def on_motion(self, event: Event):
		self.create_line(self.x, self.y, event.x, event.y)
		self.x, self.y = event.x, event.y
	

	def draw_plane(self):
		w, h, p = self.width, self.height, self.padding


		for i in range(h%p, h, p):
			self.create_line(0, i, w, i, fill="#bbbbbb")
		for i in range(w%p, w, p):
			self.create_line(i, 0, i, h, fill="#bbbbbb")

		self.create_line(0, h//2, w, h//2)
		self.create_line(w//2, 0, w//2, h)
		self.create_text(w//2-10, h//2+10, text=0)
		


root = Window()
root.mainloop()
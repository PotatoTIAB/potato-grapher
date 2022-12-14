from tkinter import *
from time import sleep
import math


class Grapher(Tk):
	def __init__(self, *args, width, height, padding, precision, **kwargs):
		super().__init__(*args, **kwargs)
		self.canvas = Plane(self, width=width, height=height, padding=padding, precision=precision, background="#eeeeee")

		self.canvas.pack()
	

	def graph(self, function: callable, precision=None):
		self.canvas.graph(function, precision)
		self.mainloop()



class Plane(Canvas):
	def __init__(self, *args, padding, precision, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.width = kwargs["width"]
		self.height = kwargs["height"]
		self.padding = padding
		self.precision = precision

		# self.bind("<Button-1>", self.on_click)
		# self.bind("<B1-Motion>", self.on_motion)
		# self.x = 0
		# self.y = 0

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
	
	
	def graph(self, function: callable, precision):
		if precision is None:
			precision = self.precision
		w, h, p, u = self.width, self.height, self.padding*precision, self.padding
		x_range = w/p/2
		y_range = w/p/2

		prev_x = -x_range*precision
		prev_y = function(-x_range)
		# print(f"f({prev_x}) = {prev_y}")
		for x in range (int(-x_range*p+1), int(x_range*p)):
			x = x/u
			y = function(x)
			# print(f"f({x}) = {y}")
			self.create_line(w//2+prev_x*u, h//2-prev_y*u, w//2+x*u, h//2-y*u, fill="#ff0000", width=2)
			prev_x, prev_y = x, y
		


if __name__ == "__main__":
	root = Grapher()
	root.mainloop()
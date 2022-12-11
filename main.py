from window import *

root = Grapher(width=600, height=600, padding=20, precision=10)
root.graph(lambda x: math.sin(x))
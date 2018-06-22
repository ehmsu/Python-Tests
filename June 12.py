Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #PROGRAMMING PUZZLES
>>> from tkinter import *
>>> import random
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> def random_triangle (width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = random.randrange(width)
	y2 = random.randrange(height)
	x3 = random.randrange(width)
	y3 = random.randrange (height)
	canvas.create_triangle(x1, y1, x2, y2, x3, y3)

	
>>> random_triangle(400, 400)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    random_triangle(400, 400)
  File "<pyshell#14>", line 8, in random_triangle
    canvas.create_triangle(x1, y1, x2, y2, x3, y3)
AttributeError: 'Canvas' object has no attribute 'create_triangle'
>>> def random_triangle (width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = random.randrange(width)
	y2 = random.randrange(height)
	x3 = random.randrange(width)
	y3 = random.randrange (height)
	canvas.create_polygon(x1, y1, x2, y2, x3, y3)

	
>>> random_triangle(400, 400)
>>> for x in range(0, 100):
	random_triangle(400, 400)

	
>>> def random_triangle (width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = random.randrange(width)
	y2 = random.randrange(height)
	x3 = random.randrange(width)
	y3 = random.randrange (height)
	canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = "red")

	
>>> for x in range (0, 100):
	random_triangle(400, 400)

	
>>> def random_triangle (width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = random.randrange(width)
	y2 = random.randrange(height)
	x3 = random.randrange(width)
	y3 = random.randrange (height)
	canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = "", outline = "black")

	
>>> for x in range (0, 100):
	random_triangle(400, 400)

	
>>> tk = Tk()

>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> canvas.create_polygon(10, 10, 10, 60, 50, 35)
1
>>> for x in range(0, 60):
	canvas.move(1, 5, 0)
	tk.update()
	time.sleep(0.05)
for x in range(0, 60):
	
SyntaxError: invalid syntax
>>> for x in range(0, 60):
	canvas.move(1, 5, 0)
	canvas.move(1, 0, 5)
	canvas.move(1, -5, 0)
	canvas.move(1, 0, -5)
	tk.update()
	time.sleep(0.05)

	
Traceback (most recent call last):
  File "<pyshell#51>", line 7, in <module>
    time.sleep(0.05)
NameError: name 'time' is not defined
>>> for x in range(0, 60):
	canvas.move(1, 5, 0)
	tk.update()
	time.sleep(0.05)
	canvas.move(1, 0, 5)
	tk.update()
	time.sleep(0.05)
	canvas.move(1, -5, 0)
	tk.update()
	time.sleep(0.05)
	canvas.move(1, 0, -5)
	tk.update()
	time.sleep(0.05)

	
Traceback (most recent call last):
  File "<pyshell#53>", line 4, in <module>
    time.sleep(0.05)
NameError: name 'time' is not defined
>>> import time
>>> for x in range(0, 60):
	canvas.move(1, 5, 0)
	tk.update()
	time.sleep(0.05)
	canvas.move(1, 0, 5)
	tk.update()
	time.sleep(0.05)
	canvas.move(1, -5, 0)
	tk.update()
	time.sleep(0.05)
	canvas.move(1, 0, -5)
	tk.update()
	time.sleep(0.05)

>>> for x in range(0, 60):
	canvas.move(1, 5, 0)
	canvas.move(1, 0, 5)
	canvas.move(1, -5, 0)
	canvas.move(1, 0, -5)
	tk.update()
	time.sleep(0.05)

	
>>> for x in range(0, 60):
	canvas.move(1, 5, 0)
	canvas.move(1, 0, 5)
	canvas.move(1, -5, 0)
	canvas.move(1, 0, -5)
	tk.update()
	time.sleep(0.05)

	
>>> 

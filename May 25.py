Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter
>>> 
=============================== RESTART: Shell ===============================
>>> from tkinter import *
>>> tk = Tk()
>>> btn = Button(tk, text = "click me")
>>> btn.pack()
>>> import turtle
>>> t = turtle.Pen()
>>> from turtle import *
>>> t = Pen()
>>> def hello():
	print('hello there')

	
>>> from tkinter import *
>>> tk = Tk()
>>> btn = Button(tk, text = "click me", command = hello)
>>> btn.pack()
>>> hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there
hello there

>>> def person(width, height):
	print('I am %s feet wide, %s feet high')

	
>>> person(height=3, width=4)
I am %s feet wide, %s feet high
>>> person(4, 3)
I am %s feet wide, %s feet high
>>> def person(width, height):
	print('I am %s feet wide, %s feet high' % (width, height))

	
>>> person(4, 3)
I am 4 feet wide, 3 feet high
>>> person(height=4, weight=3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    person(height=4, weight=3)
TypeError: person() got an unexpected keyword argument 'weight'
>>> person(height = 4, width = 3)
I am 3 feet wide, 4 feet high
>>> from tkinter import *
>>> tk = Tk()
can
>>> canvas = Canvas(tk, width = 500, height = 500)
>>> canvas.pack()
>>> from tkinter import *
>>> hello there
hello there
SyntaxError: invalid syntax
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 500, height = 500)
>>> canvas.pack()
>>> canvas.create_line(0, 0, 500, 500)
1
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_rectangle(10, 10, 50, 50)
1
>>> canvas.create_rectangle(10, 10, 300, 50)
2
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> canvas.create_rectangle(10, 10, 300, 50)
1
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> canvas.create_rectangle(10, 10, 50, 300)
1
>>> from tkinter import *
>>> import random
>>> tk = Tk()
c
>>> canvas = canvas(tk, wodth=400, height=400)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    canvas = canvas(tk, wodth=400, height=400)
TypeError: 'Canvas' object is not callable
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> def random_rectangle(width, height):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = x1 + random.randrange(width)
	y2 = y1 + random.randrange(height)
	canvas.create_rectangle(x1, y1, x2, y2)

	
>>> random_rectangle(400, 400)
>>> for x in range(0, 100):
	random_rectangle(400, 400)

	
>>> from tkinter import *
>>> import random
>>> tk = Tk()


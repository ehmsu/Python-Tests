Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def random_rectangle(width, height, fill_color):
x1 = random.randrange(width)
y1 = random.randrange(height)
x2 = random.randrange(x1 + random.randrange(width))
y2 = random.randrange(y1 + random.randrange(height))
canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
SyntaxError: expected an indented block
>>> from tkinter import *
>>> import random
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
SyntaxError: multiple statements found while compiling a single statement
>>> def random_rectangle(width, height, fill_color):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = random.randrange(x1 + random.randrange(width))
	y2 = random.randrange(y1 + random.randrange(height))
	canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

	
>>> random_rectangle(400, 400, '#ffd800')
>>> #to convert the decimal number 15 to hexadecimal, you could do this:
>>> print('%x' % 15)
f
>>> print('%02x' % 15)
0f
>>> from tkinter import *
>>> colorchooser.askcolor()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    colorchooser.askcolor()
NameError: name 'colorchooser' is not defined
>>> 
========= RESTART: C:\Users\Amely\Documents\programming\colorrect.py =========
Traceback (most recent call last):
  File "C:\Users\Amely\Documents\programming\colorrect.py", line 2, in <module>
    colorchooser.askcolor()
NameError: name 'colorchooser' is not defined
>>> from tkinter import *
>>> from tkinter.colorchooser import *
>>> def getColor():
	color = askcolor()
	print color
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(color)?
>>> def getColor():
	color = askcolor()
	print (color)

	
>>> from tkinter import *
>>> from tkinter.colorchooser import *
>>> def getColor():
	color = askcolor()
	print (color)
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
=============================== RESTART: Shell ===============================
>>> from tkinter import *
>>> from tkinter.colorchooser import *
>>> def getColor():
	color = askcolor()
	print (color)
	
SyntaxError: multiple statements found while compiling a single statement
>>> >>> from tkinter.colorchooser import *
>>> def getColor():
	color = askcolor()
	print (color)

	
SyntaxError: invalid syntax
>>> from tkinter.colorchooser import *
>>> def getColor():
	color = askcolor()
	print (color)
	
SyntaxError: multiple statements found while compiling a single statement
>>> from tkinter import *
>>> colorchooser.askcolor()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    colorchooser.askcolor()
NameError: name 'colorchooser' is not defined
>>> from tkinter import *
>>> colorchooser.askcolor()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    colorchooser.askcolor()
NameError: name 'colorchooser' is not defined
>>> from tkinter import *
colorchooser.askcolor()
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> #DRAWING ARCS
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> canvas.create_arc(10, 10, 200, 100, extent = 180, style = ARC)
1
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
SyntaxError: multiple statements found while compiling a single statement
>>> canvas.create_arc(10, 10, 200, 80, extent = 45, style = ARC)
2
>>> canvas.create_arc(10, 80, 200, 160, extent = 90, style = ARC)
3
>>> canvas.create_arc(10, 160, 200, 240, extent = 135, style = ARC)
4
>>> canvas.create_arc(10, 320, 200, 400, extent = 359, style = ARC)
5
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> canvas.create_polygon(10, 10, 100, 10, 100, 110, fill = "", outline = "black")
1
>>> canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill = "gold", outline = "purple")
2
>>> 
>>> 
>>> #DISPLAYING TEXT
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> canvas.create_text(150, 100, text = 'There once was a man from Toulouse,')
1
>>> canvas.create_text(130, 120, text = 'Who rode around on a moose.', fill = 'purple')
2
>>> canvas.create_text(150, 150, text = 'He said, It\'s my curse,', font = ('Times', 15))
3
>>> canvas.create_text(200, 200, text = 'But it could be worse,' font = ('Helvetica', 20))
SyntaxError: invalid syntax
>>> canvas.create_text(200, 200, text = 'But it could be worse,', font = ('Helvetica', 20))
4
>>> canvas.create_text(220, 250, text = 'My cousin rides round', font = ('Comic Sans', 20))
5
>>> canvas.create_text(220, 250, text = 'My cousin rides round', font = ('Comic Sans MS', 20))
6
>>> canvas.create_text(220, 300, text = 'on a goose.', font = ('Courier', 30))
7
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)canvas.pack()
SyntaxError: invalid syntax
>>> canvas.pack()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    canvas.pack()
  File "C:\Users\Amely\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2140, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: can't invoke "pack" command: application has been destroyed
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
>>> my_image = PhotoImage(file = 'C:\Users\Amely\Documents\programming')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> my_image = PhotoImage(file ='C:\Users\Amely\Documents\programming')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> my_image = PhotoImage(file='C:\Users\Amely\Documents\programming')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> my_image = PhotoImage(file='C:\Users\Amely\Documents\programming\\Test.gif')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> my_image = PhotoImage(file='c:\\Test.gif')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    my_image = PhotoImage(file='c:\\Test.gif')
  File "C:\Users\Amely\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3542, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\Amely\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3486, in __init__
    raise RuntimeError('Too early to create image')
RuntimeError: Too early to create image
>>> tk = Tk()
>>> canvas = Canvas(tk, width=400, height=400)
>>> canvas.pack()
SyntaxError: multiple statements found while compiling a single statement
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> my_image = PhotoImage(file='c:\\Test.gif')
>>> canvas.create_image(0, 0, anchor = NW, myimage)
SyntaxError: positional argument follows keyword argument
>>> canvas.create_image(0, 0, anchor = NW, image = myimage)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    canvas.create_image(0, 0, anchor = NW, image = myimage)
NameError: name 'myimage' is not defined
>>> canvas.create_image(0, 0, anchor = NW, image = my_image)
1
>>> 

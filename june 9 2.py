Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:/Users/Amely/Documents/programming/June 9.py ==========
Traceback (most recent call last):
  File "C:/Users/Amely/Documents/programming/June 9.py", line 13, in <module>
    canvas.bind_all('<KeyPress-Up>', movetriangle)
NameError: name 'canvas' is not defined
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> 
========== RESTART: C:/Users/Amely/Documents/programming/June 9.py ==========
Traceback (most recent call last):
  File "C:/Users/Amely/Documents/programming/June 9.py", line 13, in <module>
    canvas.bind_all('<KeyPress-Up>', movetriangle)
NameError: name 'canvas' is not defined
>>> 
========== RESTART: C:\Users\Amely\Documents\programming\June 9.py ==========
>>> mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
  File "C:\Users\Amely\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2495, in create_polygon
    return self._create('polygon', args, kw)
  File "C:\Users\Amely\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2477, in _create
    *(args + self._options(cnf, kw))))
_tkinter.TclError: invalid command name ".!canvas"
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
SyntaxError: multiple statements found while compiling a single statement
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35)
>>> canvas.move(mytriangle, 5, 0)
>>> mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')
>>> canvas.itemconfig(mytriangle, fill='blue')
>>> canvas.itemconfig(mytriangle, outline = 'blue')
>>> canvas.itemconfig(mytriangle, outline = 'purple'_
		      
SyntaxError: invalid syntax
>>> canvas.itemconfig(mytriangle, outline = 'purple')
		      
>>> 

Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> import random
>>> tk = Tk()
>>> canvas = Canvas(tk, width = 400, height = 400)
>>> canvas.pack()
>>> def random_rectangle(width, height, fill_color)
SyntaxError: invalid syntax
>>> def random_rectangle(width, height, fill_color):
	x1 = random.randrange(width)
	y1 = random.randrange(height)
	x2 = random.randrange(x1 + random.randrange(width))
	y2 = random.randrange(y1 + random.randrange(height))
	canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
	

>>> random_rectangle(400, 400, 'green')
>>> random_rectangle(400, 400, 'red')
>>> 
KeyboardInterrupt
>>> random_rectangle(400, 400, 'blue')
>>> random_rectangle(400, 400, 'orange')
>>> random_rectangle(400, 400, 'yellow')
>>> random_rectangle(400, 400, 'pink')
>>> random_rectangle(400, 400, 'purple')
>>> random_rectangle(400, 400, 'violet')
>>> random_rectangle(400, 400, 'magenta')
>>> random_rectangle(400, 400, 'cyan')
>>> random_rectangle(400, 400, 'indigo')
>>> random_rectangle(400, 400, 'cyan')
>>> random_rectangle(400, 400, 'umber')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    random_rectangle(400, 400, 'umber')
  File "<pyshell#12>", line 6, in random_rectangle
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
  File "C:\Users\Amely\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2498, in create_rectangle
    return self._create('rectangle', args, kw)
  File "C:\Users\Amely\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 2477, in _create
    *(args + self._options(cnf, kw))))
_tkinter.TclError: unknown color name "umber"
>>> random_rectangle(400, 400, 'brown')
>>> random_rectangle(400, 400, 'tan')
>>> 

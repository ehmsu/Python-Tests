Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> def mycircle(red, green, blue):
	t.color(red, green, blue)
	t.begin_fill()
	t.circle(50)
	t.end_fill()

	
>>> mycircle(0, 1, 0)
>>> mycircle(0, 0.5, 0)
>>> mycircle(1, 0, 0)
>>> mycircle(0.5, 0, 0)
>>> mycircle(0, 0, 1)
>>> mycircle(0, 0, 0.5)
>>> mycircle(0.9, 0.75, 0)
>>> mycircle(1, 0.7, 0.75)
>>> mycircle(1, 0.5, 0)
>>> mycircle(0.9, 0.5, 0.15)
>>> mycircle(0.4, 1, 0.78)
>>> # Turquoise!
>>> mycircle(1, 0.7, 0.85)
>>> # Light pink!
>>> mycircle(0.3, 0.2, 0.0000005)
>>> # Weird brown!
>>> mycircle(0.7, 0.7, 0.7)
>>> # Grey.
>>> mycircle(0.4, 0.0056, 0.899999)
>>> # Light blue!
>>> mycircle(0.00004, 1, 1)
>>> # Real light turquois!
>>> # Oops. Sounds fancy.
>>> 

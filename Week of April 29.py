Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> def mycircle(red, green, blue):
	t.color(red, green, blue)
	t.begin_fill()
	t.circle(50)
	t.circle()

	
>>> mycircle(0, 0, 0)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    mycircle(0, 0, 0)
  File "<pyshell#7>", line 5, in mycircle
    t.circle()
TypeError: circle() takes at least 2 arguments (1 given)
>>> def mycircle(red, green, blue):
	t.color(red, green, blue)
	t.begin_fill()
	t.circle(50)
	t.end_fill()

	
>>> mycircle(0, 0, 0)
>>> # Black circle.
>>> mycircle(1, 1, 1)
>>> # White.
>>> # SQUARES (yah!)
>>> def mysquare(size):
	for x in range(1, 5):
		t.forward(size)
		t.left(90)

		
>>> mysquare(50)
>>> mysquare(25)
>>> t.reset()
>>> mysquare(25)
>>> mysquare(50)
>>> mysquare(100)
m
>>> t.reset()
>>> mysquare(25)
>>> mysquare(50)
m
>>> mysquare(75)
>>> mysquare(100)
>>> mysquare(125)
>>> 

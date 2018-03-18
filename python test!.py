Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("Hello World")
Hello World
>>> 8*3.57
28.56
>>> fred = 100
>>> print (fred)
100
>>> found_coins = 20
>>> magic_coins = 10
>>> stolen_coins = 3
>>> found_coins + magic_coins * 365 - stolen_coins * 52
3514
>>> stolen_coins = 2
>>> found_coins + magic_coins * 365 - stolen_coins * 52
3566
>>> fred = '''How do dinosaurs pay their bills?
With tyrannosaurus checks!'''
>>> print (fred)
How do dinosaurs pay their bills?
With tyrannosaurus checks!
>>> silly_string = 'He said, "Aren't can't shouldn't wouldn't."'
SyntaxError: invalid syntax
>>> silly_string = "He said, /"Chicken/'s!"
SyntaxError: invalid syntax
>>> silly_string = "He said, \Aren\'t can\'t shouldn\'t wouldn\t.\""
>>> print (silly_string)
He said, \Aren't can't shouldn't wouldn	."
>>> silly_string = "He said, \"Aren\'t can\'t shouldn\'t wouldn\'t.\""
>>> print (silly_string)
He said, "Aren't can't shouldn't wouldn't."
>>> silly_string = '''He said, "Aren't couldn't shouldn't wouldn't."'''
>>> print (silly_string)
He said, "Aren't couldn't shouldn't wouldn't."
>>> import turtle
>>> turtle.write
<function write at 0x00000000050ADA58>
>>> install turtle
SyntaxError: invalid syntax
>>> import turtle
>>> 
>>> t = turtle.pen
>>> t = turtle.pen()
>>> import turtle
>>> t = turtle.pen()

=============================== RESTART: Shell ===============================
>>> import turtle
>>> t = turtle.pen()

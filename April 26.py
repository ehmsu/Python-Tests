Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
>>> print(random.choice(desserts))
ice cream
>>> random.shuffle(desserts)
>>> print(desserts)
['cookies', 'brownies', 'ice cream', 'pancakes', 'candy']
>>> # You might shuffle cards with the above shuffle function.
>>> #CONTROLLING THE SHELL WITH THE SYS MODULE
>>> #Exiting
>>> import sys
>>> sys.exit()
>>> #Weird, it didn't work.
>>> sys.exit
<built-in function exit>
>>> sys.exit()
>>> sys.exit()
>>> #Oooooooooookay.
>>> #Reading
>>> v = sys.stdin.readline()
He who laughs last thinks slowest
>>> print(v)
He who laughs last thinks slowest

>>> # Unlike input, you can specify how much to read with readline:
>>> v = sys.stdin.readline(13)
He who laughs last thinks slowest
>>> print(v)
He who laughs
>>> # Writing
>>> sys.stdout.write("What does a fish say when it swims into a wall? Dam.")
What does a fish say when it swims into a wall? Dam.
>>> #Wait, let me try that again.
>>> sys.stdout.write("What does a fish say when it swims into a wall? Dam.")
What does a fish say when it swims into a wall? Dam.
>>> #Well. That didn't work.
>>> #stdout = standard output
>>> #stdin = standard input
>>> # Version of Python
>>> print(sys.version)
2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)]
>>> #Well, some of the stuff probably didn't work because of the different version. Huh.
>>> 
>>> #TIME WITH THE TIME MODULE

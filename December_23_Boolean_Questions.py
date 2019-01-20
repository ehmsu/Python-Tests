Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = True
>>> y = True
>>> if x == True and y == True:
	return True
SyntaxError: 'return' outside function
>>> x and y
True
>>> x = False
>>> y = True
>>> x or y
True
>>> population = float(input("Enter population: "))
Enter population: 4560220
>>> land_area = float(input("Enter land area: "))
Enter land area: 89
>>> if population < 10000000:
	print (population)

	
4560220.0
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> import that
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import that
ModuleNotFoundError: No module named 'that'
>>> help(this)
Help on module this:

NAME
    this

DATA
    c = 97
    d = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': ...
    i = 25
    s = "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf o...bar ubaxvat ...

FILE
    c:\users\amely\appdata\local\programs\python\python36-32\lib\this.py


>>> population = 25000000
	 
>>> if 10000000 < population < 35000000
	 
SyntaxError: invalid syntax
>>> if 10000000 < population < 35000000:
	 print population
	 
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(population)?
>>> if 10000000 < population < 35000000:
	 print(population)

	 
25000000
>>> import this
	 
>>> if population / land use <= 100:
	 
SyntaxError: invalid syntax
>>> if population / land_use >= 100:
	 print ("Densely populated")

	 
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    if population / land_use >= 100:
NameError: name 'land_use' is not defined
>>> if population / land_area > 100:
	 print ("Densely populated")

	 
Densely populated
>>> if population / land_area > 100:
	 print ("Densely populated")
elif population / land area <= 100:
	 
SyntaxError: invalid syntax
>>> if population / land_area > 100:
	 print ("Densely populated")
elif population / land_area <= 100:
	 print ("Sparsely populated")

	 
Densely populated
>>> land_area = 9000
	 
>>> if population / land_area > 100:
	 print ("Densely populated")
elif population / land_area <= 100:
	 print ("Sparsely populated")

	 
Densely populated
>>> land_area = 90000000000000000
	 
>>> if population / land_area > 100:
	 print ("Densely populated")
elif population / land_area <= 100:
	 print ("Sparsely populated")

	 
Sparsely populated
>>> import math
	 
>>> math.pi
	 
3.141592653589793
>>> turn_camera_on = "Bop"
	 
>>> 

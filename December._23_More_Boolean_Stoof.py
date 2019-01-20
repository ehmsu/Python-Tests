Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #COMBINING COMPARISONS
>>> #So, by now I've worked with three kinds of operators: arithmetic, Boolean, and relational, which is very fun. Yay.
>>> #AAAAAAAAAANNND there are some rules!
>>> 
>>> #1. Arithmetic operators have higher precedence than relational operators. + and / are evaluated before < or >, for example.
>>> #2. Relational operators have higher precedence than Boolean operators. Comparisons are evaluated before "and", "or", and "not".
>>> #3. All relational operators have the same precedence.
>>> 
>>> #Here's an example:
>>> x = 2
>>> y = 5
>>> z = 7
>>> x < y and y < z
True
>>> #In the above example, x < y is evaluated before being compared to y < z through the "and" operator.
>>> #Most people like to put parentheses around the ones that are being done first to make things clearer.
>>> #Like, for example:
>>> x = 5
>>> y = 10
>>> z = 56
>>> (x < y) and (y < z)
True
>>> #Here's how you check if a number is between two other values:
>>> #1. The complicated way
>>> x = 78
>>> (1 < x) and (x <= 90)
True
>>> #2. The less-cluttered way
>>> x = 23
>>> 1 < x <= 89
True
>>> 
>>> #Sometimes this might not make sense, because the less-cluttered way chains the two comparisons together without the "and".
>>> #For example:
>>> 3 < 5 != True
True
>>> #First thought: Wot?
>>> #Second thought: Wot wot wooooot?
>>> #'Cause it looks like the statement is trying to say that 3 < 5 isn't True, right?
>>> #Well, actually, it's saying (3 < 5) and (5 != True). Since 5 is neither True nor False, Python treats it like a True statement.
>>> #I really hate how Python doesn't let you edit previous comments.
>>> #Okay, editing line 42. Python is right that (5 != True) is True, because (5 != True) is neither True nor False.
>>> #It's the same idea here:
>>> 3 < 5 != False
True
>>> #This is pretty much the same as (3 < 5) and (5 != False) because 5 is neither True nor False...
>>> #Lalallalalallalalallalalalalala
>>> 
>>> 
>>> 
>>> #Numbers and strings with Boolean operators:
>>> #For all numbers, 0 will return True if used with a Boolean operator and all other numbers will return False.
>>> not 0
True
>>> 0 and 0
0
>>> (not 0) and (not 0)
True
>>> or 0
SyntaxError: invalid syntax
>>> #Fun times.
>>> not 1
False
>>> not -98
False
>>> not 54
False
>>> not 67.4
False
>>> not 456
False
>>> #Etcetera, etcetera...
>>> #Similarly, an empty string is treated as True, but anything else is False.
>>> not " "
False
>>> #Hoooold up, that string wasn't empty (sorry).
>>> not ""
True
>>> #There we are,
>>> not "kelp"
False
>>> not "chicken"
False
>>> not "not"
False
>>> not "not not not not not not"
False
>>> not "a professional dog paddler"
False
>>> not "kipper"
False
>>> not "a Pythoner"
False
>>> #Aw, that's very sweet of you, Python.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Let's have a look at American Standard Code for Information Interchange (ASCII). Because coding hates me.
>>> #Characters in strings are represented by strings, like how capital A is 65, a space is 32, while lowercase z is 122.
>>> 'A' < 'z'
True
>>> ' ' > 'z'
False
>>> 
>>> 


>>> #The "in" operator
>>> #The "in" operator checks to see if one string is within another string.
>>> #Oooo.
>>> 'Jan' in '01 Jan 1838'
True
>>> #OOOOOOOOOOOOOoooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOOoooooooooooOOOOOOOOOOOOOOOOOOOOOOOOoooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOooooooooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOoooooooooooooooooooooo
>>> 
>>> 
>>> 
>>> #It's case sensitive, too.
>>> #The empty string is a substring of every string.
>>> '' in 'ilikesushi'
True
>>> '' in ''
True
>>> '' in 'whoopsiedaisy'
True
>>> 
>>> #HEY HEY HEY now we can pay attention to stuff like that a + b challenge that you got so dang confused by!
>>> 4
4

>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 6.0
>>> if ph < 7.0:
	print(ph, "is acidic.")

	
6.0 is acidic.
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 9.8
>>> if ph < 7.0:
	print(ph, "is basic.")
	print("You should drink it. It's a very sensible idea which I am suggesting to you at this time in space.")

	
>>> 
KeyboardInterrupt
>>> if ph > 7.0:
	print(ph, "is basic.")
	print("You should drink it. It's a very sensible idea which I am suggesting to you at this time in space.")

	
9.8 is basic.
You should drink it. It's a very sensible idea which I am suggesting to you at this time in space.
>>> ph = float(input('Enter the pH level: '))
Enter the pH level: 3.4
>>> if ph < 7.0
SyntaxError: invalid syntax
>>> if ph < 7.0:
	print (ph, "is acidic.")
	print ("You should probably drink it, buddy.")
elif ph > 7.0:
	print (ph, "is basic.")
	print ("You like mushrooms.")

	
3.4 is acidic.
You should probably drink it, buddy.
>>> 
>>> 
>>> 
>>> def pH():
	print ("Didya want to see if your pH is acidic or basic? Please enter your pH here!")
	ph = float(sys.stdin.readline())
	if ph = 7.0:
		
SyntaxError: invalid syntax
>>> def pH():
	print ("Didya want to see if your pH is acidic or basic? Please enter your pH here!")
	ph = float(sys.stdin.readline())
	if ph == 7.0:
		print ("Aw, that sucks, buddy.", ph, "is actually a boring neutral thingy that won't burn your guts out.")
	elif ph < 7.0:
		print (ph, "is acidic! You should drink a cup of it and see what it does to your organs.")
	elif ph > 7.0:
		print (ph, "is basic! Congratulations! If you checked with this program after drinking a litre of that mystery liquid, then you probably just ingested some of that funky bleach you
		       
SyntaxError: EOL while scanning string literal
>>> def pH():
	print ("Didya want to see if your pH is acidic or basic? Please enter your pH here!")
	ph = float(sys.stdin.readline())
	if ph == 7.0:
		print ("Aw, that sucks, buddy.", ph, "is actually a boring neutral thingy that won't burn your guts out.")
	elif ph < 7.0:
		print (ph, "is acidic! You should drink a cup of it and see what it does to your organs.")
	elif ph > 7.0:
		print (ph, "is basic! Congratulations! If you checked with this program after drinking a litre of that mystery liquid, then you probably just ingested some of that funky bleach you've got in the basement! Of course, I could be lying!")

		       
>>> pH()
		       
Didya want to see if your pH is acidic or basic? Please enter your pH here!
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    pH()
  File "<pyshell#134>", line 3, in pH
    ph = float(sys.stdin.readline())
NameError: name 'sys' is not defined
>>> 
		       
>>> 
		       
>>> 
		       
>>> #Okay, I think you have to import something here which I forgot. Whatever.
		       
>>> #ELSE STATEMENTS
		       
>>> compound = input('Enter the compound: ')
		       
Enter the compound: NH3
>>> if compound = "H2O":
		       
SyntaxError: invalid syntax
>>> import sys
		       
>>> def pH():
	print ("Didya want to see if your pH is acidic or basic? Please enter your pH here!")
	ph = float(sys.stdin.readline())
	if ph == 7.0:
		print ("Aw, that sucks, buddy.", ph, "is actually a boring neutral thingy that won't burn your guts out.")
	elif ph < 7.0:
		print (ph, "is acidic! You should drink a cup of it and see what it does to your organs.")
	elif ph > 7.0:
		print (ph, "is basic! Congratulations! If you checked with this program after drinking a litre of that mystery liquid, then you probably just ingested some of that funky bleach you've got in the basement! Of course, I could be lying!")

		       
>>> pH()
		       
Didya want to see if your pH is acidic or basic? Please enter your pH here!
666
666.0 is basic! Congratulations! If you checked with this program after drinking a litre of that mystery liquid, then you probably just ingested some of that funky bleach you've got in the basement! Of course, I could be lying!
>>> pH()
		       
Didya want to see if your pH is acidic or basic? Please enter your pH here!
69696969696969696969696969696966996969696996996969696969696999696969696969.69696969696969696969696969696969696969696969696969696969696969696969696969696969696969990
6.969696969696969e+73 is basic! Congratulations! If you checked with this program after drinking a litre of that mystery liquid, then you probably just ingested some of that funky bleach you've got in the basement! Of course, I could be lying!
>>> 
		       
>>> 
		       
>>> 
		       
>>> 
		       
>>> 
		       
>>> 
		       


>>> 
		       




>>> 
		       

>>> 
		       



>>> 
		       

>>> 
		       

>>> 
		       
>>> hi bob!
		       
SyntaxError: invalid syntax
>>> echo "I am Grim bob and I am here to take your soul!"
		       
SyntaxError: invalid syntax
>>> 
		       
>>> 
		       
>>> 
		       
>>> #Boolean Exercises
		       
>>> #1. c
		       
>>> #I think it will say False.
		       
>>> True or True and False
		       
True
>>> #Oh, gods, I am stupid.
		       
>>> #True or True and False is comparing True, then comparing True and False. True and False becomes False, which means Python is comparing True or False, which will always give an outcome of True.
		       
>>> #1. d
		       
>>> #I think it will be True.
		       
>>> not True or not False
		       
True
>>> #Yay.
		       
>>> #1. e
		       
>>> #I think it will be True.
		       
>>> True or not 0
		       
True
>>> #1. f
		       
>>> #I think it will be true.
		       
>>> 52 < 52. 3
		       
SyntaxError: invalid syntax
>>> 
		       
>>> 52. 0
		       
SyntaxError: invalid syntax
>>> 52 < 52.3
		       
True
>>> #1. g
		       
>>> #I think it will be False.
		       
>>> 1 + 52 < 52. 3
		       
SyntaxError: invalid syntax
>>> 1 + 52 < 52.3
		       
False
>>> #1. h
		       
>>> #I think it will say False.
		       
>>> 4 != 4.0
		       
False
>>> #2. a
		       
>>> x = True
		       
>>> y = True
		       
>>> if x = True and y = True
		       
SyntaxError: invalid syntax
>>> if x == True and y == True:
		       return True
		       
SyntaxError: 'return' outside function
>>> 
		       
>>> if x == True and y == True:
	return True
		       
SyntaxError: 'return' outside function
>>> 

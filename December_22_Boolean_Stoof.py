Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #INTEGER DIVISION, MODULO, EXPONENTIATION
>>> #Integer Division:
>>> 53 // 24
2
>>> #Integer Division is like division, except there isn't a remainder.
>>> #Modulos:
>>> 53 % 24
5
>>> #This is the remainder of 53 divided by 24.
>>> 
>>> 
>>> 
>>> #Boolean Operators:
>>> #There are only three Boolean operators: And, Or, and Not.
>>> #Yay.
>>> #Yay.
>>> #Yaaaaaaaaaaaaaaaaaay.
>>> #Basically, "Not" does the opposite of what you put in:
>>> not True
False
>>> not False
True
>>> #Wooooooooooooow. Such Wowness.
>>> #"And" is a binary operator. I have no idea what it means, but basically if you put in two of the same thing (True and True, or False and False) then it gives you
>>> #what there are two of.
>>> #Okay, better if I just begin programming as an example.
>>> True and True
True
>>> #See?
>>> False and False
False
>>> #But if I put in two different values using "And", then it always gives me False.
>>> True and False
False
>>> False and True
False
>>> #While "Or" is like the exact opposite.
>>> #If you put two of the same value, it's like "And":
>>> True or True
True
>>> False or False
False
>>> #Buuuuuuuuuuut if you put in two different values then it will always return True.
>>> True or False
True
>>> False or True
True
>>> #There's also some sort of strangely interesting mumbo-jumbo about inclusive vs. exclusive or after this bit.
>>> 
>>> 
>>> #??????????
>>> #Like, how Python always interprets "or" as inclusive, rather than choosing between two. In English, if we are using "Or" like in "It's you or me, buddy" than you have to choose between you or me. That's called "Exclusive".
>>> 
>>> 


>>> 


>>> 

>>> 
>>> #So!
>>> #An example of Boolean stuff.
>>> #Oh, shoot, I misspelt "then" in Line 54. Whoops.
>>> 
>>> #Let's look at the statement "It is not hot and sunny" because I wish it was hot and sunny and maybe the sky can take a hint about now since my feet are freezing off.
>>> #In true Gandalf style, is it not hot but it IS sunny? Or is it both not hot and not sunny?
>>> #If it is not hot but it IS sunny:
>>> hot = False
>>> sunny = True
>>> #Oh, wait, nix that.
>>> hot = True
>>> sunny = False
>>> (not hot) and sunny
False
>>> not (hot and sunny)
True
>>> #Do we get how this works?
>>> #Yeah, I think we do.
>>> 
>>> 

>>> 

>>> #RELATIONAL OPERATORS
>>> #This is just a fancy name for greater than and less than symbols, yadda yadda yadda.
>>> #These expressions create True and False values.
>>> #For example, if I put down a few of these, then Python will tell me if I put in a blatant lie or if it's legitimate.
>>> 45 < 78
True
>>> 56 < 45
False
>>> #Ta-da!
>>> #What's cool about "relational operators" is that you can compare integers to floating-point numbers with any of them. Integers are automatically converted to floating-point numbers, like when we add two numbers that are an integer and a floater thing.
>>> 23.1 >= 23
True
>>> 23.1 >= 90
False
>>> 23.1 >= 23.1
True
>>> 
>>> #Just one more thing and I promise we'll be done with relational operators!
>>> 23 = 89
SyntaxError: can't assign to literal
>>> #See? For "equal to", you can't just put one equal sign, you have to put two otherwise you're defining 23 as 89, which is a little funky.
>>> 23 == 89
False
>>> 45 != 56
True
>>> #!= means "not equal to", incase you hadn't noticed.
>>> 
>>> #Here's a function working with relational operators.
>>> 
>>> def is_positive(x:float) -> bool:
	return x > 0

>>> #So, according to the Mimi, this thing will return either a True or False if x is positive or negative. I think what the bool means is that it's supposed to return either True or False.
>>> #Okay, I just looked back at it and yup I am right. Bool has only two types: True and False. That's what Bool is supposed to mean.
>>> #Let's test it.
>>> 
>>> is_positive(-3)
False
>>> is_positive(0)
False
>>> is_positive(5)
True
>>> 

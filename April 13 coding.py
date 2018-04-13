Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> float('12')
12.0
>>> float('123.456789')
123.456789
>>> #floating is for converting values into proper numbers
>>> your_age = input('Enter your age: ')
Enter your age: 13
>>> age = float(your_age)
>>> if age > 13:
	print('You are %s years too old' % (age - 2))

	
>>> int(123.456)
123
>>> #int converts a string/number into a whole number, so basically everything after the decimal point
>>> #and it can convert a string to an integer!
>>> int('123')
123
>>> #BUT you can't convert a floating point number into an integer.
>>> 
>>> 
>>> #LEN FUNCTION
>>> len('this is a test string')
21
>>> #so there's an example: it returns the number of characters. What about a list/tuple?
>>> creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll']
>>> print(len(creature_list))
6
>>> #and with maps!
>>> enemies_map = {'Batman': 'Joker',
	       'Superman': 'Lex Luthor',
	       'Spiderman': 'Green Goblin'}
>>> print(len(enemies_map))
3
>>> #Useful for when you're working with loops.
>>> fruit = ['apple', 'banana', 'clementine', 'dragon fruit']
>>> length = len(fruit)
>>> for x in range(0, length):
	print('the fruit at index %s is %s' % (x, fruit[x]))

	
the fruit at index 0 is apple
the fruit at index 1 is banana
the fruit at index 2 is clementine
the fruit at index 3 is dragon fruit
>>> #MAX AND MIN FUNCTIONS
>>> numbers = [5, 4, 10, 30, 22]
>>> print(max(numbers))
30
>>> #And with strings, where the letters are ranked alphabetically
>>> strings = 's,t,r,i,n,g,S,T,R,I,N,G'
>>> print(max(strings))
t
>>> 

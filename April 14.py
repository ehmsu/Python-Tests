Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #RANGE FUNCTIONS
>>> #Weeell, we've already seen this used in for loops:
>>> for x in range(0,5):
	print(x)

	
0
1
2
3
4
>>> #Isn't it amazing when there is no spellcheck? fnjwi cfjiwpj
>>> #The range function actually returns a special object called an
#iterator that repeats an action a number of times. In this case, it
#returns the next highest number each time it is called.
>>> #You can also convert the iterator thingy into a list!
>>> print(list(range(0,5)))
[0, 1, 2, 3, 4]
>>> #Ta-da!
>>> #
KeyboardInterrupt
>>> #You can also add a third parameter to range, called step. If
#the step value is not included, the number 1 is used as the step by
#default. But what happens when we pass in the number 2 as the
#step?
>>> count_by_twos = list(range(0, 30, 2))
>>> print(count_by_twos)
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> #Cool!
>>> count_down_by_twos = list(range(40, 10, - 2))
>>> print(count_down_by_twos)
[40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12]
>>> #The sum function, which gives you back the total of a list:
>>> my_list_of_numbers = list(range(0, 100, 50))
>>> print(my_list_of_numbers)
[0, 50]
>>> #Whoops, I meant...
>>> my_list_of_numbers = list(range(0, 500, 50))
>>> print(my_list_of_numbers)
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> print(sum(my_list_of_numbers))
2250
>>> #Booyah!
>>> 
>>> #READING FILES
>>> test_file = open('c:\\test.txt')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    test_file = open('c:\\test.txt')
IOError: [Errno 2] No such file or directory: 'c:\\test.txt'
>>> test_file = open('c:\\test.txt')
>>> text = test_file.read()
>>> print(text)
There once was a boy named Marcelo
Who dreamed he ate a marshmallow
He awoke with a start
As his bed fell apart
And he found he was a much rounder fellow

>>> #Yay!
>>> #Now, if you try to write:
>>> test_file = open'c:\\test.
SyntaxError: EOL while scanning string literal
>>> test_file = open('c:\\test.txt
		 
SyntaxError: EOL while scanning string literal
>>> test_file = open('c:\\test.txt', 'w')
>>> test_file.write('this is my test file')
>>> test_file.write('What is green and loud? A froghorn!')
>>> test_file.close()
>>> test_file = open('c:\\test.txt')
>>> text = test_file.read
>>> print(text)
<built-in method read of file object at 0x0000000004F54ED0>
>>> 
>>> 
>>> 
>>> #PROGRAMMING PUZZLES
>>> popcorn = 'I love popcorn!'
>>> dir(popcorn)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(popcorn.format)
Help on built-in function format:

format(...)
    S.format(*args, **kwargs) -> string
    
    Return a formatted version of S, using substitutions from args and kwargs.
    The substitutions are identified by braces ('{' and '}').

>>> help(popcorn.decode)
Help on built-in function decode:

decode(...)
    S.decode([encoding[,errors]]) -> object
    
    Decodes S using the codec registered for encoding. encoding defaults
    to the default encoding. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeDecodeError. Other possible values are 'ignore' and 'replace'
    as well as any other name registered with codecs.register_error that is
    able to handle UnicodeDecodeErrors.

>>> help(popcorn.count)
Help on built-in function count:

count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are interpreted
    as in slice notation.

>>> weird_list = [1, 2, 3]
>>> print(weird_list.count)
<built-in method count of list object at 0x0000000004F9B548>
>>> help(popcorn.swapcase)
Help on built-in function swapcase:

swapcase(...)
    S.swapcase() -> string
    
    Return a copy of the string S with uppercase characters
    converted to lowercase and vice versa.

>>> help(popcorn.split)
Help on built-in function split:

split(...)
    S.split([sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string S, using sep as the
    delimiter string.  If maxsplit is given, at most maxsplit
    splits are done. If sep is not specified or is None, any
    whitespace string is a separator and empty strings are removed
    from the result.

>>> hidden_message = "this if is you not are a reading this good then way you to have hide done a it message wrong"
>>> yay = hidden_message.split
>>> print (yay)
<built-in method split of str object at 0x0000000004452EB0>
>>> 

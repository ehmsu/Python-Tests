Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:/Users/Amely/Documents/file_examples/file_reader.py =======
First line of text
Second line of text
Third line of text
Twenty-sixth line of text

>>> 
======= RESTART: C:/Users/Amely/Documents/file_examples/file_reader.py =======
First line of text
Second line of text
Third line of text
Twenty-sixth line of text

>>> 
===== RESTART: C:/Users/Amely/Documents/file_examples/file_reader_v2.py =====
Traceback (most recent call last):
  File "C:/Users/Amely/Documents/file_examples/file_reader_v2.py", line 19, in <module>
    with open('file_example.text', 'r') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'file_example.text'
>>> 
===== RESTART: C:/Users/Amely/Documents/file_examples/file_reader_v2.py =====
First line of text
Second line of text
Third line of text
Twenty-sixth line of text

>>> import os
>>> os.getcwd()
'C:\\Users\\Amely\\Documents\\file_examples'
>>> #OoooooooooOOOOOOOOOOOOOOOOooooooooooooooooooooOOOOOOOOOOOOOOOOO.
>>> #If I want to change the directory I do this:
>>> #os.chdir('insert directory here')
>>> #chdir, as you've probably guessed, is short for "change directory".
>>> #OOOOOOOOOOOOOoooooooooooooooooooooooooooooooOOOOOOOOOOOOOOOOOOOOOOOOoooooo.
>>> 
===== RESTART: C:/Users/Amely/Documents/file_examples/file_reader_v3.py =====
Traceback (most recent call last):
  File "C:/Users/Amely/Documents/file_examples/file_reader_v3.py", line 1, in <module>
    with open('open_example.txt', 'r') as example_file:
FileNotFoundError: [Errno 2] No such file or directory: 'open_example.txt'
>>> 
===== RESTART: C:/Users/Amely/Documents/file_examples/file_reader_v3.py =====
The rest 10 characters: First line
The rest of the file:  of text
Second line of text
Third line of text
Twenty-sixth line of text

>>> 
===== RESTART: C:/Users/Amely/Documents/file_examples/file_reader_v3.py =====
The first 10 characters: First line
The rest of the file:  of text
Second line of text
Third line of text
Twenty-sixth line of text

>>> 

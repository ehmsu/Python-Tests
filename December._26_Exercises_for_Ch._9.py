Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from typing import List
>>> def remove_neg(num_list):
	for thing in num_list:
		if item < 0:
			num_list.remove(thing)

			
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
  File "<pyshell#5>", line 3, in remove_neg
    if item < 0:
NameError: name 'item' is not defined
>>> def remove_neg(num_list):
	for thing in num_list:
		if thing < 0:
			num_list.remove(thing)

			
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
>>> def remove_neg(num_list):
	for thing in num_list:
		if thing < 0:
			num_list.remove(thing)
			print(num_list)

			
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
[1, 2, 3, 6, -1, -3, 2]
[1, 2, 3, 6, -3, 2]
>>> def remove_neg(num_list):
	for thing in num_list:
		for chicken in thing:
			if thing < 0:
				num_list.remove(thing)
				print(num_list)

				
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
  File "<pyshell#15>", line 3, in remove_neg
    for chicken in thing:
TypeError: 'int' object is not iterable
>>> def remove_neg(num_list):
	for thing in num_list:
		if thing < 0:
			num_list.remove(thing)
			print(num_list)

			
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
[1, 2, 3, 6, -1, -3, 2]
[1, 2, 3, 6, -3, 2]
>>> def remove_neg(num_list):
	for thing in num_list:
		if thing < 0:
			num_list.remove(thing)
			num_list.remove(thing)
			print(num_list)

			
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
[1, 2, 3, 6, -1, 2]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
  File "<pyshell#21>", line 5, in remove_neg
    num_list.remove(thing)
ValueError: list.remove(x): x not in list
>>> def remove_neg(num_list):
	for thing in num_list:
		if thing < 0:
			num_list.remove(thing)
	for another_thing in num_list:
		if another_thing < 0:
			num_list.remove(another_thing)
	print(num_list)

	
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 2])
[1, 2, 3, 6, 2]
>>> 

Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for x in range (1, 61):
	print(x)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
>>> #This code will rapidly print all numbers from 1 to 60. However,
#we can tell Python to sleep for a second between each print statement,
#like this:
>>> for x in range(1, 61):
	print(x)
	time.sleep(1)

	
1

Traceback (most recent call last):
  File "<pyshell#7>", line 3, in <module>
    time.sleep(1)
NameError: name 'time' is not defined
>>> #Riiight, we need to import time.
>>> import time
>>> for x in range(1, 61):
	print(x)
	time.sleep(1)

	
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60




>>> #Well. It's like a 1 minute timer.
>>> # USING THE PICKLE MODULE TO SAVE INFO
>>> #You might find pickle useful if
#you’re writing a game and want to save
#information about a player’s progress.
>>> game_data = {
	'player-position': 'N23 E 45',
	'pockets': ['keys', 'pocket knife', 'polished stone'],
	'backpack': ['rope', 'hammer', 'apple'],
	'money': 158.50
}
>>> import pickle
>>> save_file = open('save.dat', 'wb')

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    save_file = open('save.dat', 'wb')
IOError: [Errno 13] Permission denied: 'save.dat'
>>> import pickle
>>> game_data = {
	'player-position': 'N23 E 45',
	'pockets': ['keys', 'pocket knife', 'polished stone'],
	'backpack': ['rope', 'hammer', 'apple'],
	'money': 158.50
}
>>> save_file = open('save.dat', 'wb'}
SyntaxError: invalid syntax
>>> save_file = open('save.dat', 'wb')

Traceback (most recent call last):

  File "<pyshell#28>", line 1, in <module>
    save_file = open('save.dat', 'wb')
IOError: [Errno 13] Permission denied: 'save.dat'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # MORE TURTLE GRAPHICS
>>> # Oh, wait, that's got to be on python.exe. Never mind.

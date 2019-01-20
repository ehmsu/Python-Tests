Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:\Users\Amely\Documents\programming\dnd.py ============
>>> dice(1, 20)
11
>>> dice(62, 62)
60
21
48
4
14
56
45
39
6
39
21
32
44
22
1
44
36
61
57
18
19
8
42
34
47
27
47
59
21
14
3
41
13
24
43
55
20
46
54
11
9
45
19
35
34
12
25
24
52
30
17
2
23
38
39
3
22
25
20
25
42
37
>>> dice(1, 6)
6
>>> dice(2, 6)
6
1
>>> dice(1, 10)
6
>>> dice(1, 8)
7
>>> dice(4, 10)
6
4
9
3
>>> dice(3, 8)
8
2
4
>>> dice(5, 8)
5
4
6
5
6
>>> dice(8, 6)
6
6
4
2
5
6
2
2
>>> dice(4, 6)
2
6
5
2
>>> dice(4, 6)
5
4
4
5
>>> dice(4, 6)
5
2
5
6
>>> dice(4, 6)
4
4
6
1
>>> #Writing Example Cells Using StringIO
>>> #(The IO stands for Input/Output)
>>> from io import StringIO
>>> input_string = '1.3 3.4\n2 4.2\n-1 1\n'
>>> infile = StringIO(input_string)
>>> infile.readline()
'1.3 3.4\n'
>>> #So, we got StringIO to read the first line.
>>> 
>>> #We can write to StringIO files as if they were files and retrieve their contents as a string using method getvalue.
>>> outfile = StringIO()
>>> outfile.write('1.3 3.4 4.7\n')
12
>>> outfile.write('-1 1 0.0 \m'

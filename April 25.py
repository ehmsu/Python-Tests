Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> num = random.randint(1, 100)
>>> while True:
	print('Guess a number between 1 and 100')
	guess = input()
	i = int(guess)
	if i == num:
		print('You guessed right')
		break
	elif i < num:
		print('Try higher')
	elif i > num:
		print('Try lower')
while False:
	
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> while True:
	print('Guess a number between 1 and 100')
	guess = input()
	i = int(guess)
	if i == num:
		print('You guessed right')
		break
	elif i < num:
		print('Try higher')
	elif i > num:
		print('Try lower')

		
Guess a number between 1 and 100
1014
Try lower
Guess a number between 1 and 100
12
Try higher
Guess a number between 1 and 100
56
Try higher
Guess a number between 1 and 100
89
Try lower
Guess a number between 1 and 100
80
Try lower
Guess a number between 1 and 100
70
Try lower
Guess a number between 1 and 100
60
You guessed right
>>> while True:
	print('Guess a number between 1 and 100')
	guess = input()
	i = int(guess)
	if i == num:
		print('You guessed right')
		print ('No you didn\'t')
		print ('Hah yes you did')
		print ('Nope guess again')
		print ('No, you guessed right')
		break
	elif i < num:
		print('Try higher')
	elif i > num:
		print('Try lower')

		
Guess a number between 1 and 100
3
Try higher
Guess a number between 1 and 100
9
Try higher
Guess a number between 1 and 100
20
Try higher
Guess a number between 1 and 100
80
Try lower
Guess a number between 1 and 100
50
Try higher
Guess a number between 1 and 100
60
You guessed right
No you didn't
Hah yes you did
Nope guess again
No, you guessed right
>>> 

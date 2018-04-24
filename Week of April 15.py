Python 2.7.13 |Anaconda 4.0.0 (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Giraffes:
	def __init__ (self, spots):
		self.giraffe_spots = spots

		
>>> ozwald = Giraffes(100)
>>> print(ozwald.giraffe_spots)
100
>>> class Animal:
	def __init__ (self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color

		
>>> harry = Animal('hippogriff', 6, 'pink')
>>> import copy
>>> harry = Animal('hippogriff', 6, 'pink')
>>> harriet = copy.copy(harry)
>>> print(harry.species)
hippogriff
>>> print(harriet.species)
hippogriff
>>> # We can also create and copy a list of Animal objects.
>>> harry = Animal('hippogriff', 6, 'pink')
>>> carrie = Animal('chimera', 4, 'green polka dots')
>>> billy = Animal('bogill', 0, 'paisley')
>>> my_animals = [harry, carrie, billy]
>>> more_animals = copy.copy(my_animals)
>>> print(more_animals[0].species)
hippogriff
>>> print(more_animals[1].species)
chimera
>>> #But look what happens if we change the species of one of our
#Animal objects in the original my_animals list (hippogriff to ghoul).
#Python changes the species in more_animals, too.
>>> my_animals[0].species = 'ghoul'
>>> print(my_animals[0].species)
ghoul
>>> print(more_animals[0].species)
ghoul
>>> 
>>> 
>>> sally = Animal('sphinx', 4, 'sand')
>>> my_animals.append(sally)
>>> print(len(my_animals))
4
>>> print(len(more_animals))
3
>>> #Another function in the copy module, deepcopy, actually creates
#copies of all objects inside the object being copied. When we use
#deepcopy to copy my_animals, we get a new list complete with copies of
#all of its objects. As a result, changes to one of our original Animal
#objects won’t affect the objects in the new list. Here’s an example:

>>> more_animals = copy.deepcopy(my_animals)
>>> my_animals[0].species = 'wyrm'
>>> print(my_animals[0].species)
wyrm
>>> print(more_animals[0].species)
ghoul
>>> # -*- coding: cp1252 -*-
>>> -*- coding: cp1252 -*-
SyntaxError: invalid syntax
>>> 

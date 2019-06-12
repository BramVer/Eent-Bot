import random
from random import shuffle

def burger_moment():
	borger = list('cheeseburger')
	shuffle(borger)
	return ''.join(borger)


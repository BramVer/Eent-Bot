import requests
import random


import urllib.request




def vangen():
	getalletjen = str(random.randint(1, 807))
	
	pookmon = requests.get('https://pokeapi.co/api/v2/pokemon/' + getalletjen + '/')

	pookmon_json = pookmon.json()
	name = pookmon_json['name']
	sprite = pookmon_json['sprites']['front_default']
	urllib.request.urlretrieve(sprite, "classes/pokemon.jpg")

	return f'Je hebt {name} gevangered!'
	





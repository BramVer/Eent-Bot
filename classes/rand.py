import random


def random_getal():
	return str(random.randint(0,5))

def random_ongeluk():
	ar = ["Je bent van de trap gevallen en hebt nu hersenschade",
		  "Je bent op een blokje lego gaan staan, sterkte!",
		  "Je probeerde oud brood te smikkelen en smakkelen en hebt dusdanig je gebit en kiezen naar de filipijnen geholpa!!",
		  ]
	return random.choice(ar)



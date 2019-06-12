import random

speler = 0
computer = 0

ar = ['schaar', 'steen', 'papier']

# xxx = input('kies: schaar, steen of papier?: ')



def spelen(speler_keuze):
	
	computer_keuze = ar[random.randint(0,2)]

	if speler_keuze == computer_keuze:
		return ('tie, eent koos ', computer_keuze)
	elif speler_keuze == 'steen':
		if computer_keuze == 'schaar':
			return ('speler wint, de computer koos', computer_keuze)
		elif computer_keuze == 'papier':
			return ('computer wint, de computer koos', computer_keuze)
	
	elif speler_keuze == 'schaar':
		if computer_keuze == 'papier':
			return ('speler wint, de computer koos', computer_keuze)
		elif computer_keuze == 'steen':
			return ('computer wint, de computer koos', computer_keuze)
	elif speler_keuze == 'papier':
		if computer_keuze == 'steen':
			return ('speler wint, de computer koos', computer_keuze)
		elif computer_keuze == 'schaar':
			return ('computer wint, de computer koos', computer_keuze)

	return 'Rot op mislukte incel dat hoort niet bij het spel'



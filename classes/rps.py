import random


speler = 0
computer = 0

ar = ['schaar', 'steen', 'papier']

# xxx = input('kies: schaar, steen of papier?: ')



def spelen(speler_keuze):
	speler_keuze = speler_keuze[0]
	
	computer_keuze = ar[random.randint(0,2)]

	if speler_keuze == computer_keuze:
		return f'potvermiljaar we hebben allebei {computer_keuze} gekiezerd'
	elif speler_keuze == 'steen':
		if computer_keuze == 'schaar':
			return f'menes makker, mijn {computer_keuze} is niks waard'
		elif computer_keuze == 'papier':
			return f'Ik heb gewonnen want ik koos {computer_keuze} en jij niet zo werkt dit spelletje en wow je zuigt hahahaha'
	
	elif speler_keuze == 'schaar':
		if computer_keuze == 'papier':
			return f'ik heb expres {computer_keuze} gekozen om je te laten winnen'
		elif computer_keuze == 'steen':
			return f'Beep boop ik win want ik ben een computer en heb super gemachineerde intelligentie. Dusdanig heb ik via bilineare LTSM {computer_keuze} gekozen.'
	elif speler_keuze == 'papier':
		if computer_keuze == 'steen':
			return f'{speler_keuze} tegen mijn {computer_keuze} is valsspelen. Maat. Geniet van je onverdiende punten.'
		elif computer_keuze == 'schaar':
			return f'Epische eent win moment. Mijn stand {computer_keuze} is te sterk voor je'

	else:
	 return f'Rot op mislukte incel dat hoort niet bij het spel, steek die {speler_keuze} in uw gat'



import requests

def quote (zoekTerm):
	zoekTerm = zoekTerm[0]
	r = requests.get ('https://samson-api.herokuapp.com/api/quotes/' + zoekTerm)
	r_json = r.json()



	for q in r_json:
		return(q['quote'])



#https://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&appid=c0f39dfd1294407009096cbd062acd62



def weer():
	weertje = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&appid=c0f39dfd1294407009096cbd062acd62')
	weer_json = weertje.json()

	print(weer_json['weather'][0]['main'])


weer()



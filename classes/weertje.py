
import requests






def conv(fah):
	fahrenheit=float(fah)
	celsius=(fahrenheit-32)/1.8
	return f'°C{celsius}'



def weer():
	weertje = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&appid=c0f39dfd1294407009096cbd062acd62')
	weer_json = weertje.json()

	mainWeer=(weer_json['weather'][0]['main'])
	descWeer=(weer_json['weather'][0]['description'])
	temp = conv(int(weer_json['main']['temp']))
	name= weer_json['name']

	print(f"The sky in {name} is full of {mainWeer}, with {descWeer} outside. \n The temperature is a decent {temp}" )

	


weer()

#https://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&appid=c0f39dfd1294407009096cbd062acd62
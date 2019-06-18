
import requests
import math



#lol


# def conv(fah):
# 	fahrenheit=float(fah)
# 	celsius=((fahrenheit-32)/1.8)/5.48148148148
# 	celsius = math.floor(celsius)
# 	return f'°C{celsius}'



def huidig_weer():
	weertje = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&appid=c0f39dfd1294407009096cbd062acd62&units=metric')
	weer_json = weertje.json()

	mainWeer=(weer_json['weather'][0]['main'])
	descWeer=(weer_json['weather'][0]['description'])
	temp = weer_json['main']['temp']
	name= weer_json['name']

	return f"The sky in {name} is {mainWeer}, with {descWeer} outside. The temperature is a decent {temp}" 

	




#https://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&appid=c0f39dfd1294407009096cbd062acd62
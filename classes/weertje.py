
import requests
import math
from PIL import Image, ImageDraw, ImageFont
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
	full_string = f"The sky in {name} is {mainWeer}, \n with {descWeer} outside. \n The temperature is a decent °C {temp}"

	img = Image.open("classes/weer.jpg")
 
	fnt = ImageFont.truetype('/snap/pycharm-community/132/jre64/lib/fonts/DroidSans-Bold.ttf', 50)
	d = ImageDraw.Draw(img)
	d.text((10,300), full_string, font=fnt, fill=(0,0,0))
	d.text((15,295), full_string, font=fnt, fill=(255,255,0))
	img.save('classes/weerbericht.jpg')


	return 'Hier is je weerbericht voor dit eigenzijnste momenteel moment'
	# return f"The sky in {name} is {mainWeer}, \n with {descWeer} outside. \n The temperature is a decent °C {temp}" 

	



#https://api.openweathermap.org/data/2.5/weather?q=Antwerp,be&appid=c0f39dfd1294407009096cbd062acd62
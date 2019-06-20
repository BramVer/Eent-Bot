import requests
import urllib.request


def eent():
	
	
	
	urllib.request.urlretrieve('https://random-d.uk/api/v2/randomimg', "eent.jpg")
	return 'Hier is je eent dier schepsel'

eent()
import requests

def quote (zoekTerm):
	zoekTerm = zoekTerm[0]
	r = requests.get ('https://samson-api.herokuapp.com/api/quotes/' + zoekTerm)
	r_json = r.json()



	for q in r_json:
		return(q['quote'])



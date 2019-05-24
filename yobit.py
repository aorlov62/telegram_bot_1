import requests

def get_btc_usd():
	url = 'https://yobit.net/api/2/btc_usd/ticker'
	response = requests.get(url).json()
	price =  response['ticker']['last']

	return f'Курс биткоина = {price}$'

def get_usd_rur():
	url = 'https://yobit.net/api/2/usd_rur/ticker'
	response = requests.get(url).json()
	price =  response['ticker']['last']

	return f'Курс доллара = {price}руб.'
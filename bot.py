import requests
from misc import token
import json


# https://api.telegram.org/bot793095298:AAH9ks51R45hBIN4MFmtcLYr1q3RCLq7ts8/sendmessage?chat_id=192994009&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def get_message():
	data = get_updates()
	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']

	return {'chat_id': chat_id, 'text': message_text}


def send_message(chat_id, text='Привет хозяин'):
	url = f'{URL}sendmessage?chat_id={chat_id}&text={text}'
	r = requests.get(url)
	print(r)


def main():
	message = get_message()
	send_message(message['chat_id'])


if __name__ == '__main__':
	main()
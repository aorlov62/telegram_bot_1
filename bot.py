import requests
from misc import token
from yobit import get_btc_usd, get_usd_rur
from time import sleep


# https://api.telegram.org/bot793095298:AAH9ks51R45hBIN4MFmtcLYr1q3RCLq7ts8/sendmessage?chat_id=192994009&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()


def get_message():
	data = get_updates()

	if len(data['result']) == 0:
		return None

	last_object = data['result'][-1]

	message = {
		'chat_id': last_object['message']['chat']['id'],
		'text': last_object['message']['text'],
		'update_id': last_object['update_id']
	}

	return message


def send_message(chat_id, text='Попробуй еще раз...'):
	url = f'{URL}sendmessage?chat_id={chat_id}&text={text}'
	r = requests.get(url)


def parse_message(text):
	if 'Привет' in text:
		return 'Привет!'
	elif 'Как дела' in text:
		return 'Хорошо, а у тебя как?'
	elif 'Курс биткоина' in text:
		return get_btc_usd()
	elif 'Курс доллара' in text:
		return get_usd_rur()
	else:
		return 'Повтори свой запрос'


def main():

	update_id = 0

	while True:
		message = get_message()

		if update_id == 0:
			update_id = message['update_id']

		if update_id != message['update_id']:
			update_id = message['update_id']

			if 'chat_id' in message:
				text = parse_message(message['text'])
				send_message(message['chat_id'], text)
			else:
				print('Диалог не начат')

		sleep(3)

if __name__ == '__main__':
	main()
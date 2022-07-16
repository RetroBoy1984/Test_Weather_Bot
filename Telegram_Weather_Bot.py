from pyowm import OWM
from pyowm.utils.config import get_default_config
# from pyowm.utils import timestamps
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('b7097940e1d96048fd0395790ececab1', config_dict)
mgr = owm.weather_manager()

import telebot
bot = telebot.TeleBot("5176869480:AAHVvPUudHdq8gwtCHGXzHPd9a3w4WmQ_uA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура сейчас в районе " + str(temp) + " по Цельсию" + "\n\n"

	if temp < 0:
		answer += "На улице холодно"
	elif temp < -5.00:
		answer += "Холод собачий, одевайся теплее!"
	elif temp < -10.00:
		answer += "Не выходи из дома, Замёрзнешь!"
	elif temp <= 5:
		answer += "Температура в норме, можно гулять!"
	elif temp >= 10:
		answer += "Тополиный пух, жара, Июль ^_^"
	else:
		answer += "Температура в норме, можно гулять!"
	bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)
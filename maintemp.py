import telebot
import requests
import json


bot = telebot.TeleBot("7169080535:AAHVqnpOLeYq3Kv7NH55druVtviGgJ-jgJQ")
API = '9463980907c33c97eff7ae91d3cfb002'



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши название города.')


@bot.message_handler(content_types=['text'])
def get_wather(message):
    city = message.text.strip().lower()  
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'sone.png' if temp > 5.0 else "sonenon.png"
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Ты сам-то понял, что написал?!')
    
bot.polling(none_stop=True)

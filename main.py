import telebot
import webbrowser

bot = telebot.TeleBot("")


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.harley-davidson.com/eu/en/index.html')
    


@bot.message_handler(commands=['start', "main", 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, тварь божья! {message.from_user.last_name}')
    
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "Помоги себе сам!", parse_mode='html')
    
    
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, тварь божья! {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'id: {message.from_user.id}')    


        

bot.polling(none_stop=True)
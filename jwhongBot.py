import telebot

API_TOKEN = '240292131:AAHCbFDidvc4KMCDNsR-CraS8_-jxz4RI0U'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Hi there, I am Echo JwhongBot. 
        I am hero to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
        """)
    print('testMessage')

# Handle all other messages with content_type 'text' ( content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    
@bot.message_handler(commands=['bus'])
def bus_info(message):
	bot.reply_to(messabe, "bus information")

bot.polling() 
    

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Hi there, I am Echo JwhongBot. 
        I am hero to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
        """)

# Handle all other messages with content_type 'text' ( content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
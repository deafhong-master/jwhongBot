import telebot

# from bus.bus_seoul import bus_seoul

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

API_TOKEN = '240292131:AAHCbFDidvc4KMCDNsR-CraS8_-jxz4RI0U'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Hi there, I am Echo JwhongBot. 
        I am hero to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!
        """)
    print('testMessage')

@bot.message_handler(commands=['bus'])
def bus_info(message):
    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute'
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'nuD0VA4oaDhlyilVJNYSxhuI8x23SqQQN2kHmPkbklAUhhLmy0UioY92z6yQtx0oCLl6DlNrk%2FkTwkkHhwfvcA%3D%3D', quote_plus('stId') : '22274', quote_plus('busRouteId') : '3412', quote_plus('numOfRows') : '999', quote_plus('pageNo') : '1' })
    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    bot.reply_to(message, response_body)
    # print response_body
	

# Handle all other messages with content_type 'text' ( content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling() 
    





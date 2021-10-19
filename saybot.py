import telebot
import gtts
import datetime
import os
from telebot import types


current_path = os.path.abspath(os.getcwd()) 
token = '2024877385:AAHdaTKlJc2SYEqcJP8TCrcMBSgf8jeJZbQ'

# text = ''
# say = gtts.gTTS(text, lang='ru', slow=False)
# say.save('output1.mp3')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, "Hello, i'm speech synthesizer!")

@bot.message_handler(commands=['alphabet'])
def alphabet(message):
    markup=types.ReplyKeyboardMarkup()
    buttonA=types.KeyboardButton('A')
    buttonB=types.KeyboardButton('B')
    buttonC=types.KeyboardButton('C')
    buttonD=types.KeyboardButton('D')
    buttonI=types.KeyboardButton('I')
    buttonJ=types.KeyboardButton('J')
    buttonH=types.KeyboardButton('H')
    buttonI=types.KeyboardButton('I')
    buttonJ=types.KeyboardButton('J')
    markup.row(buttonA, buttonB,buttonC,buttonD,buttonI)
    markup.row(buttonB,buttonJ,buttonH,buttonI,buttonJ)   
    bot.send_message(message.chat.id,'working',reply_markup=markup)

@bot.message_handler(content_types='text')
def say_any(message):
    audio_name = datetime.datetime.now()
    text = message.text
    say = gtts.gTTS(text, lang='en', slow=False)
    say.save(f'{audio_name}.mp3')
    final_path = f'{current_path}/{audio_name}.mp3'
    audio_file = open(final_path, 'rb')
    bot.send_audio(message.chat.id, audio_file)
    bot.send_message(message.chat.id, "I have sended!")
    

print ('Bot is working!')
bot.infinity_polling()
import telegram
import requests
import io
import telebot
from PIL import Image,ImageOps

bot=telebot.TeleBot("6915320402:AAG2HbWlbIqPWjGqPmz2Dd5_XnCY5niXM5w")


@bot.message_handler(commands=['start'])
def start(message):
    
    bot.reply_to(message, "hellow welcome")

@bot.message_handler(button=['photo'])
def photo(message):
    bot.reply_to(message, "send us your picture")
@bot.message_handler(func=lambda message:True)
def echo(message):
    bot.reply_to(message , message.text)

@bot.message_handler(content_types=["photo"])
def photo_handler(message):
    photo_info=message.photo[-1]
    file_id=photo_info.file.id

    file_info=bot.get_file(file_id)
    downloaded_file=bot.download_file(file_info.file_path)
    image=Image.open(io.BytesIO(downloaded_file))
    
bot.polling()
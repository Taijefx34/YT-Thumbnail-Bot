import telebot

bot = telebot.TeleBot('your_token')


@bot.message_handler(commands=['start'])
def start_message(message):
    start_message = '''🇺🇸Hi!
I'm bot to get thumbnail of YouTube video. Send me valid link to YouTube video you want to get thumbnail. 

🇷🇺Привет!
Я бот для получения превью YouTube видео . Отправь мне валидную ссылку на YouTube видео которого ты хочешь получить превью.'''
    bot.send_message(message.chat.id, start_message)


@bot.message_handler(content_types=['text'])
def main(message):
    if 'youtu' in message.text and len(message.text) >= 20:
        if 'youtube.com' in message.text:
            video_id = message.text.split('/watch?v=')[-1][:11:]
        else:
            video_id = message.text.split('/')[-1][:11:]

        try:
            bot.send_photo(message.chat.id, f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg' )
        except:
            bot.send_photo(message.chat.id, f'http://img.youtube.com/vi/{video_id}/0.jpg' )

bot.polling()

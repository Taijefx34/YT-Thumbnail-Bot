from pyrogram import Client, filters
from pyrogram.errors import WebpageCurlFailed
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


app = Client('ytb') 


@app.on_message(filters.command('start'))
async def start_message(_, msg):
    start_message = '''🇺🇸Send me valid link to YouTube video you want to get thumbnail of. 


🇷🇺Отправь мне валидную ссылку на YouTube видео превью которого ты хочешь получить.'''
    await msg.reply(start_message)


@app.on_message(filters.regex("^https:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}$"))
async def gyt(_, msg):
    video_id = msg.text[-11:]
    kb = InlineKeyboardMarkup([[InlineKeyboardButton('🔗Link', url=f"https://youtu.be/{video_id}")]])

    try:
        await msg.reply_photo(f'http://img.youtube.com/vi/{video_id}/maxresdefault.jpg', quote=True, reply_markup=kb)
    except WebpageCurlFailed:
        await msg.reply("**Invalid video link!**", quote=True)
    except:
        await msg.reply_photo(f'http://img.youtube.com/vi/{video_id}/0.jpg', quote=True, reply_markup=kb)


app.run()

from datetime import timedelta

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytube import YouTube as yt
from pytube.exceptions import VideoUnavailable


app = Client("ytb")


@app.on_message(filters.command("start"))
async def start_message(_, msg):
    start_message = """🇺🇸Send me valid link to YouTube video you want to get thumbnail of. 


🇷🇺Отправь мне валидную ссылку на YouTube видео превью которого ты хочешь получить."""
    await msg.reply(start_message)


@app.on_message(filters.regex("^https?:\/\/?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/).{11}"))
async def gyt(_, msg):
    try:
        vid_url = msg.matches[0].group(0)
        yt_vid = yt(vid_url)

        vid_turl = yt_vid.thumbnail_url
        vid_title = yt_vid.title
        vid_author = yt_vid.author
        vid_length = timedelta(seconds=yt_vid.length)
        vid_pdate = yt_vid.publish_date.strftime("%Y-%m-%d")

        kb = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔗Link", url=f"https://youtu.be/{vid_url[-11:]}")]])
        await msg.reply_photo(
            vid_turl,
            caption=f"""🎬 **{vid_title}**
👤 `{vid_author}`

⏳ **{vid_length}**
🗓 `{vid_pdate}`""",
            quote=True,
            reply_markup=kb,
        )
    except VideoUnavailable:
        await msg.reply("**Invalid video link!**", quote=True)


app.run()

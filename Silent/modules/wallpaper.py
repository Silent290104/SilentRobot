import random

import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Silent import pgram as pbot


@pbot.on_message(filters.command(["wall", "wallpaper"]))
async def wall(_, message: Message):
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None
    if not text:
        return await message.reply_text("`ᴘʟᴇᴀsᴇ ɢɪᴠᴇ sᴏᴍᴇ ǫᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ.`")
    m = await message.reply_text("`sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴡᴀʟʟᴘᴀᴘᴇʀ...`")
    try:
        url = requests.get(f"https://api.safone.me/wall?query={text}").json()["results"]
        ran = random.randint(0, 3)
        await message.reply_photo(
            photo=url[ran]["imageUrl"],
            caption=f"🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ʟɪɴᴋ", url=url[ran]["imageUrl"])],
                ]
            ),
        )
        await m.delete()
    except Exception:
        await m.edit_text(
            f"`ᴡᴀʟʟᴘᴀᴘᴇʀ ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ : `{text}`",
        )


# ᴛʜᴀɴᴋs https://github.com/Wolf2901/SilentRobot/blob/master/SilentRobot/modules/wallpaper.py

import asyncio
import random
from sys import version_info

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from ABG.helper import PHOTO
from Silent import BOT_NAME
from Silent import BOT_USERNAME as fuck
from Silent import OWNER_USERNAME, SUPPORT_CHAT, UPDATES_CHANNEL, pgram

ASAU = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{UPDATES_CHANNEL}"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{fuck}?startgroup=true",
        ),
    ],
]


@pgram.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴀʟɪᴠɪɴɢ ʙᴀʙʏ ....")
    await accha.delete()
    await asyncio.sleep(0.1)
    umm = await m.reply_sticker(
        "CAACAgUAAx0CZIiVngABBHAzYwdi9OIVTQ7DYELAqMl46fgnK4wAAjsIAAKagolX-O0V64tvzK8pBA"
    )
    await asyncio.sleep(0.1)
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}**
     ▱▱▱▱▱▱▱▱▱▱▱▱
» **ᴍʏ ᴏᴡɴᴇʀ :** [sɪʟᴇɴᴛ](https://t.me/{OWNER_USERNAME})
» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
⍟ **ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ :** `1.0`
     ▱▱▱▱▱▱▱▱▱▱▱▱""",
        reply_markup=InlineKeyboardMarkup(ASAU),
    )

import asyncio

from pyrogram import filters

from Silent import pgram as app
from Silent.modules.mongo.karma_mongo import (
    alpha_to_int,
    get_karma,
    get_karmas,
    int_to_alpha,
    update_karma,
)
from Silent.utils.errors import capture_err

regex_upvote = r"^((?i)\+|\+\+|\+1|thx|tnx|ty|thank you|thanx|thanks|pro|cool|good|👍|nice|noice|piro)$"
regex_downvote = r"^(\-|\-\-|\-1|👎|noob|Noob|gross|fuck off)$"

karma_positive_group = 3
karma_negative_group = 4


from pymongo import MongoClient

from Silent import MONGO_DB_URL

worddb = MongoClient(MONGO_DB_URL)
k = worddb["SilentKarma"]["karma_status"]


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in app.iter_chat_members(chat_id, filter="administrators")
    ]


@app.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_upvote)
    & ~filters.via_bot
    & ~filters.bot,
    group=karma_positive_group,
)
async def upvote(_, message):
    chat_id = message.chat.id
    is_karma = k.find_one({"chat_id": chat_id})
    if not is_karma:
        if not message.reply_to_message.from_user:
            return
        if not message.from_user:
            return
        if message.reply_to_message.from_user.id == message.from_user.id:
            return
        user_id = message.reply_to_message.from_user.id
        user_mention = message.reply_to_message.from_user.mention
        current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
        if current_karma:
            current_karma = current_karma["karma"]
            karma = current_karma + 1
        else:
            karma = 1
        new_karma = {"karma": karma}
        await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
        await message.reply_text(
            f"ɪɴᴄʀᴇᴍᴇɴᴛᴇᴅ ᴋᴀʀᴍᴀ  ᴏғ +1 {user_mention} \nᴛᴏᴛᴀʟ ᴘᴏɪɴᴛs: {karma}"
        )


@app.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_downvote)
    & ~filters.via_bot
    & ~filters.bot,
    group=karma_negative_group,
)
async def downvote(_, message):
    chat_id = message.chat.id
    is_karma = k.find_one({"chat_id": chat_id})
    if is_karma:
        if not message.reply_to_message.from_user:
            return
        if not message.from_user:
            return
        if message.reply_to_message.from_user.id == message.from_user.id:
            return
        user_id = message.reply_to_message.from_user.id
        user_mention = message.reply_to_message.from_user.mention
        current_karma = await get_karma(chat_id, await int_to_alpha(user_id))
        if current_karma:
            current_karma = current_karma["karma"]
            karma = current_karma - 1
        else:
            karma = 1
        new_karma = {"karma": karma}
        await update_karma(chat_id, await int_to_alpha(user_id), new_karma)
        await message.reply_text(
            f"ᴅᴇᴄʀᴇᴍᴇɴᴛᴇᴅ ᴋᴀʀᴍᴀ ᴏғ -1 {user_mention}  \nᴛᴏᴛᴀʟ ᴘᴏɪɴᴛs: {karma}"
        )


@app.on_message(filters.command("karmastats") & filters.group)
@capture_err
async def karma(_, message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        m = await message.reply_text("ᴡᴀɪᴛ  10 sᴇᴄᴏɴᴅs")
        karma = await get_karmas(chat_id)
        if not karma:
            await m.edit("ɴᴏ ᴋᴀʀᴍᴀ ɪɴ DB ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.")
            return
        msg = f"**ᴋᴀʀᴍᴀ ʟɪsᴛ ᴏғ {message.chat.title}:- **\n"
        limit = 0
        karma_dicc = {}
        for i in karma:
            user_id = await alpha_to_int(i)
            user_karma = karma[i]["karma"]
            karma_dicc[str(user_id)] = user_karma
            karma_arranged = dict(
                sorted(karma_dicc.items(), key=lambda item: item[1], reverse=True)
            )
        if not karma_dicc:
            await m.edit("ɴᴏ ᴋᴀʀᴍᴀ ɪɴ DB ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ.")
            return
        for user_idd, karma_count in karma_arranged.items():
            if limit > 9:
                break
            try:
                user = await app.get_users(int(user_idd))
                await asyncio.sleep(0.8)
            except Exception:
                continue
            first_name = user.first_name
            if not first_name:
                continue
            username = user.username
            msg += f"**{karma_count}**  {(first_name[0:12] + '...') if len(first_name) > 12 else first_name}  `{('@' + username) if username else user_idd}`\n"
            limit += 1
        await m.edit(msg)
    else:
        user_id = message.reply_to_message.from_user.id
        karma = await get_karma(chat_id, await int_to_alpha(user_id))
        karma = karma["karma"] if karma else 0
        await message.reply_text(f"**ᴛᴏᴛᴀʟ ᴘᴏɪɴᴛ :** {karma}")


__mod_name__ = "𝙺ᴀʀᴍᴀ"
__help__ = """

*ᴜᴘᴠᴏᴛᴇ* - ᴜsᴇ ᴜᴘᴠᴏᴛᴇ ᴋᴇʏᴡᴏʀᴅs ʟɪᴋᴇ "+", "+1", "thanks", ᴇᴛᴄ. ᴛᴏ ᴜᴘᴠᴏᴛᴇ ᴀ ᴍᴇssᴀɢᴇ.
*ᴅᴏᴡɴᴠᴏᴛᴇ* - ᴜsᴇ ᴅᴏᴡɴᴠᴏᴛᴇ ᴋᴇʏᴡᴏʀᴅs ʟɪᴋᴇ "-", "-1", ᴇᴛᴄ. ᴛᴏ ᴅᴏᴡɴᴠᴏᴛᴇ ᴀ ᴍᴇssᴀɢᴇ.

*ᴄᴏᴍᴍᴀɴᴅs*

⍟ /karmastats:- `ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴀᴛ ᴜsᴇʀ's  ᴋᴀʀᴍᴀ ᴘᴏɪɴᴛs`

⍟ /karmastats:- `sᴇɴᴅ ᴡɪᴛʜᴏᴜᴛ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴋᴀʀᴍᴀ ᴘᴏɪɴᴛ ʟɪsᴛ of ᴛᴏᴘ 10`

⍟ /karma :- `ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ karma ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ `
"""

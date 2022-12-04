import random
from datetime import datetime

from pyrogram import filters

from Silent import pgram
from Silent.modules.mongo.couples_mongo import get_couple, save_couple
from Silent.utils.errors import capture_err


# Date and time
def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list


def dt_tom():
    a = (
        str(int(dt()[0].split("/")[0]) + 1)
        + "/"
        + dt()[0].split("/")[1]
        + "/"
        + dt()[0].split("/")[2]
    )
    return a


today = str(dt()[0])
tomorrow = str(dt_tom())


@pgram.on_message(filters.command("couples") & ~filters.edited)
@capture_err
async def couple(_, message):
    if message.chat.type == "private":
        await message.reply_text("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.")
        return
    try:
        chat_id = message.chat.id
        is_selected = await get_couple(chat_id, today)
        if not is_selected:
            list_of_users = []
            async for i in pgram.iter_chat_members(message.chat.id):
                if not i.user.is_bot:
                    list_of_users.append(i.user.id)
            if len(list_of_users) < 2:
                await message.reply_text("ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴜsᴇʀs")
                return
            c1_id = random.choice(list_of_users)
            c2_id = random.choice(list_of_users)
            while c1_id == c2_id:
                c1_id = random.choice(list_of_users)
            c1_mention = (await pgram.get_users(c1_id)).mention
            c2_mention = (await pgram.get_users(c2_id)).mention

            couple_selection_message = f"""**ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ:**
{c1_mention} + {c2_mention} = 💗
__ɴᴇᴡ ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ᴍᴀʏ ʙᴇ ᴄʜᴏsᴇɴ ᴀᴛ 12ᴀᴍ {ᴛᴏᴍᴏʀʀᴏᴡ}__"""
            await pgram.send_message(message.chat.id, text=couple_selection_message)
            couple = {"c1_id": c1_id, "c2_id": c2_id}
            await save_couple(chat_id, today, couple)

        elif is_selected:
            c1_id = int(is_selected["c1_id"])
            c2_id = int(is_selected["c2_id"])
            c1_name = (await pgram.get_users(c1_id)).first_name
            c2_name = (await pgram.get_users(c2_id)).first_name
            couple_selection_message = f"""ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ:
[{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = 💜
__ɴᴇᴡ ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ ᴍᴀʏ ʙᴇ ᴄʜᴏsᴇɴ ᴀᴛ 12ᴀᴍ {ᴛᴏᴍᴏʀʀᴏᴡ}__"""
            await pgram.send_message(message.chat.id, text=couple_selection_message)
    except Exception as e:
        print(e)
        await message.reply_text(e)


__mod_name__ = "𝙲ᴏᴜᴘʟᴇs"

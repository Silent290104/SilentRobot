import logging

from pyrogram import filters

from Silent import pgram

logging.basicConfig(level=logging.DEBUG)


@pgram.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.message_id
    reply = message.reply_to_message

    text = f"**[𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗜𝗗:]({message.link})** `{message_id}`\n"
    text += f"**[𝗬𝗼𝘂𝗿 𝗜𝗗:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[𝗨𝘀𝗲𝗿 𝗜𝗗:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("This user doesn't exist.", quote=True)

    text += f"**[𝗖𝗵𝗮𝘁 𝗜𝗗:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[𝗥𝗲𝗽𝗹𝗶𝗲𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗜𝗗:]({reply.link})** `{reply.message_id}`\n"
        text += f"**[𝗥𝗲𝗽𝗹𝗶𝗲𝗱 𝗨𝘀𝗲𝗿 𝗜𝗗:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode="md",
    )

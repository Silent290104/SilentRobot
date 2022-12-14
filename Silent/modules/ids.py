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

    text = f"**[๐ ๐ฒ๐๐๐ฎ๐ด๐ฒ ๐๐:]({message.link})** `{message_id}`\n"
    text += f"**[๐ฌ๐ผ๐๐ฟ ๐๐:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[๐จ๐๐ฒ๐ฟ ๐๐:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("This user doesn't exist.", quote=True)

    text += f"**[๐๐ต๐ฎ๐ ๐๐:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[๐ฅ๐ฒ๐ฝ๐น๐ถ๐ฒ๐ฑ ๐ ๐ฒ๐๐๐ฎ๐ด๐ฒ ๐๐:]({reply.link})** `{reply.message_id}`\n"
        text += f"**[๐ฅ๐ฒ๐ฝ๐น๐ถ๐ฒ๐ฑ ๐จ๐๐ฒ๐ฟ ๐๐:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"แดสแด าแดสแดกแดสแดแดแด แดสแดษดษดแดส, {reply.forward_from_chat.title}, สแดs แดษด ษชแด แดา `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ษชแด แดา แดสแด สแดแดสษชแดแด แดสแดแด/แดสแดษดษดแดส, ษชs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode="md",
    )

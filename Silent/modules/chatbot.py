import html
import json
import re
from time import sleep

import requests
from telegram import (
    CallbackQuery,
    Chat,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
    User,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.utils.helpers import mention_html

import Silent.modules.sql.kuki_sql as sql
from Silent import dispatcher
from Silent.modules.helper_funcs.chat_status import user_admin, user_admin_no_reply
from Silent.modules.log_channel import gloggable


@user_admin_no_reply
@gloggable
def asuxrm(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"rm_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = sql.set_kuki(chat.id)
        if is_kuki:
            is_kuki = sql.set_kuki(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_DISABLED\n"
                f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "{} ᴄʜᴀᴛʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʙʏ {}.".format(
                    dispatcher.bot.first_name, mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin_no_reply
@gloggable
def asuxadd(update: Update, context: CallbackContext) -> str:
    query: Optional[CallbackQuery] = update.callback_query
    user: Optional[User] = update.effective_user
    match = re.match(r"add_chat\((.+?)\)", query.data)
    if match:
        user_id = match.group(1)
        chat: Optional[Chat] = update.effective_chat
        is_kuki = sql.rem_kuki(chat.id)
        if is_kuki:
            is_kuki = sql.rem_kuki(user_id)
            return (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"AI_ENABLE\n"
                f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            )
        else:
            update.effective_message.edit_text(
                "{} ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʙʏ {}.".format(
                    dispatcher.bot.first_name, mention_html(user.id, user.first_name)
                ),
                parse_mode=ParseMode.HTML,
            )

    return ""


@user_admin
@gloggable
def exonchatbot(update: Update, context: CallbackContext):
    update.effective_user
    message = update.effective_message
    msg = "• ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="add_chat({})"),
                InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="rm_chat({})"),
            ],
        ]
    )
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


def kuki_message(context: CallbackContext, message):
    reply_message = message.reply_to_message
    if message.text.lower() == "kuki":
        return True
    if reply_message:
        if reply_message.from_user.id == context.bot.get_me().id:
            return True
    else:
        return False


def chatbot(update: Update, context: CallbackContext):
    message = update.effective_message
    chat_id = update.effective_chat.id
    bot = context.bot
    is_kuki = sql.is_kuki(chat_id)
    if is_kuki:
        return

    if message.text and not message.document:
        if not kuki_message(context, message):
            return
        Silent = message.text
        bot.send_chat_action(chat_id, action="typing")
        url = f"http://api.roseloverx.com/api/chatbot?message={Silent}"
        request = requests.get(url)
        results = json.loads(request.text)
        result = results["responses"]
        sleep(0.5)
        message.reply_text(result[0])


__help__ = """
*ᴀᴅᴍɪɴs ᴏɴʟʏ ᴄᴏᴍᴍᴀɴᴅs*:

  »  /chatbot *:* sʜᴏᴡs ᴄʜᴀᴛʙᴏᴛ ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ
"""

__mod_name__ = "𝙲ʜᴀᴛʙᴏᴛ"


CHATBOTK_HANDLER = CommandHandler("chatbot", silentchatbot, run_async=True)
ADD_CHAT_HANDLER = CallbackQueryHandler(silentadd, pattern=r"add_chat", run_async=True)
RM_CHAT_HANDLER = CallbackQueryHandler(silentrm, pattern=r"rm_chat", run_async=True)
CHATBOT_HANDLER = MessageHandler(
    Filters.text
    & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!") & ~Filters.regex(r"^\/")),
    chatbot,
    run_async=True,
)

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(CHATBOTK_HANDLER)
dispatcher.add_handler(RM_CHAT_HANDLER)
dispatcher.add_handler(CHATBOT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
    CHATBOT_HANDLER,
]

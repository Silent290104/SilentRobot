from Exon import db

karma_statusdb = db.karma_status


def is_karma(chat_id):
    karma = karma_statusdb.find_one({"chat_id": chat_id})


def set_karma(chat_id):
    karma = is_karma(chat_id)
    if not karma:
        karma_statusdb.insert_one({"chat_id": chat_id})


def rem_karma(chat_id):
    karma = is_karma(chat_id)
    if karma:
        karma_statusdb.delete_one({"chat_id": chat_id})

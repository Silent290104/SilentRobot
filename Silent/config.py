import json
import os

from dotenv import load_dotenv

load_dotenv()


def get_user_list(config, key):
    with open("{}/Silent/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # ᴀᴅᴅ ʏᴏᴜʀ ᴠᴇʀs  (ᴍᴀɪɴ ᴠᴇʀs)
    API_ID = "16420694"
    API_HASH = "8fe1ce5474da2c16043ca2cc6e3c47b6"
    EVENT_LOGS = "-1001781365680"
    DATABASE_URI = "postgres://ftmhhlpp:vXFSn6lNyTwI_OOTbGSBbdsQI9hABC1f@ella.db.elephantsql.com/ftmhhlpp"  # elephantsql.com
    REDIS_URL = "redis://default:imP6xyfvlFsVpzFbciK3dIx9Vde05pav@redis-17127.c239.us-east-1-2.ec2.cloud.redislabs.com:17127/default"  # redis.os
    MONGO_DB_URL = "mongodb+srv://shaygirl:shay@cluster0.r0os6np.mongodb.net/?retryWrites=true&w=majori"  # cloud.mongodb.com/
    TOKEN = ""
    OWNER_USERNAME = "Silent_Smile_04"
    OWNER_ID = "5278339583"
    SUPPORT_CHAT = "Total_masti"

    # ɴᴏᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴢᴏɴᴇ, ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴇᴅɪᴛ
    MONGO_DB = "Silent"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    ARQ_API_URL = "https://arq.hamker.in"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    ARQ_API_KEY = "TENRCY-KDKSK-MSMSM-OXQYYO-ARQ"
    DONATION_LINK = "t.me/Total_masti"
    HELP_IMG = "https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg"
    START_IMG = "https://te.legra.ph/file/653cc589cef8ce310a9f2.jpg"
    UPDATES_CHANNEL = "Galaxia_Update"
    INFOPIC = False
    GENIUS_API_TOKEN = "28jwoKAkskaSjsnsksAjnwjUJwj"
    SPAMWATCH_API = None
    REM_BG_API_KEY = None
    OPENWEATHERMAP_ID = None
    WALL_API = None
    TIME_API_KEY = None
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    TEMP_DOWNLOAD_DIRECTORY = "./"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    LOAD = []  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEL_CMDS = True
    BAN_STICKER = None
    WORKERS = 8
    STRICT_GBAN = True
    WEBHOOK = False
    URL = None
    PORT = []
    ALLOW_EXCL = []
    ALLOW_CHATS = True
    CERT_PATH = []
    SPAMWATCH_SUPPORT_CHAT = "Total_masti"
    BOT_API_URL = "https://api.telegram.org/bot"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DRAGONS = get_user_list("elevated_users.json", "sudos")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEV_USERS = get_user_list("elevated_users.json", "devs")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    REQUESTER = get_user_list("elevated_users.json", "whitelists")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEMONS = get_user_list("elevated_users.json", "supports")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    INSPECTOR = get_user_list("elevated_users.json", "sudos")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    TIGERS = get_user_list("elevated_users.json", "tigers")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    WOLVES = get_user_list("elevated_users.json", "whitelists")  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY

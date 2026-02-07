# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper



import os

class Config:
    API_ID = os.environ.get("API_ID", "24670806")
    API_HASH = os.environ.get("API_HASH", "82134723a32b2cae76b9cfb3b1570745")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7933011109:AAEh6m_MoKYtHHbOvJfJeXWZxBHIYUPJ3Tc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "ftm-forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://botuser:botuserpass1234@cluster0.bcz3n2q.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '8229228616').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
   


# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

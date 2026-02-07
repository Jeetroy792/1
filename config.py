# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper



import os

class Config:
    API_ID = os.environ.get("API_ID", "28776072")
    API_HASH = os.environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7902709403:AAFw_GZyDZp3WLtSOConKOyx5uoGVwqdS2g") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "ftm-forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://ftm:ftm@cluster0.g1opc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '7711039923').split()]


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

import asyncio
from bot import Bot
from pyrogram import idle

async def start_bot():
    app = Bot()
    await app.start()
    print("✅ BOT IS RUNNING ✅")
    await idle() # এটি বটকে মেমোরিতে ধরে রাখবে এবং বন্ধ হতে দেবে না
    await app.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())

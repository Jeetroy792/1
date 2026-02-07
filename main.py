from bot import Bot
import asyncio
from pyrogram import idle

async def start_services():
    app = Bot()
    await app.start()
    print("--- BOT IS RUNNING ---")
    await idle() # এটি প্রসেসটিকে থামিয়ে রাখবে
    await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_services())

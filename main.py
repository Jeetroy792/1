from bot import Bot
import asyncio
from pyrogram import idle

app = Bot()

async def start_bot():
    await app.start()
    print("--- BOT STARTED SUCCESSFULLY ---")
    await idle() # এটি বটকে বন্ধ হওয়া থেকে আটকাবে
    await app.stop()

if __name__ == "__main__":
    try:
        # সরাসরি run() এর বদলে লুপ ব্যবহার করা বেশি নিরাপদ
        app.run() 
    except Exception as e:
        print(f"Error: {e}")

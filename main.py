from bot import Bot
import asyncio

app = Bot()

async def main():
    await app.start()
    print("Bot started successfully!")
    # বটটিকে সচল রাখার জন্য লুপ
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        app.run()
    except KeyboardInterrupt:
        pass

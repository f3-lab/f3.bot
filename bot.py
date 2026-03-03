import os
import asyncio
from telegram.ext import ApplicationBuilder

TOKEN = os.getenv("BOT_TOKEN")

async def main():
    print("STARTING BOT...")
    app = ApplicationBuilder().token(TOKEN).build()
    print("BOT CREATED")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
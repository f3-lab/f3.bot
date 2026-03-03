import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1003891725312

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍽 Открыть меню", url="https://t.me/YOUR_BOT_USERNAME")]
    ])

    await app.bot.send_message(
        chat_id=CHANNEL_ID,
        text="🥟 F3 FOOD\nНажмите кнопку ниже, чтобы открыть меню:",
        reply_markup=keyboard
    )

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
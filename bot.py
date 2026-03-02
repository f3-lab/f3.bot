import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1003891725312

def get_keyboard():
    keyboard = [
        [InlineKeyboardButton("🍽 Открыть меню", url="https://t.me/F3_FOOD_BOT")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def post_to_channel(application):
    await application.bot.send_message(
        chat_id=CHANNEL_ID,
        text="Добро пожаловать в F3 FOOD 🇧🇷\n\nНажмите кнопку ниже, чтобы открыть меню:",
        reply_markup=get_keyboard()
    )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    await post_to_channel(app)
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

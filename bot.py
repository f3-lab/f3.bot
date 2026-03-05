import os
import sys
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("ERROR: BOT_TOKEN not found")
    sys.exit(1)

CHANNEL_ID = -1003891725312

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍽 Открыть меню", url="https://t.me/f3food_bot")]
    ])

    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text="🥟 F3 FOOD\nНажмите кнопку ниже, чтобы открыть меню:",
        reply_markup=keyboard
    )

    await update.message.reply_text("Сообщение отправлено в канал")

def main():
    print("Starting bot...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("post", post))
    app.run_polling()

if __name__ == "__main__":
    main()
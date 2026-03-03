import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = -1003891725312  # твой канал

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍽 Открыть меню", url="https://t.me/YOUR_BOT_USERNAME")]
    ])

    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text="🥟 F3 FOOD\nНажмите кнопку ниже, чтобы открыть меню:",
        reply_markup=keyboard
    )

    await update.message.reply_text("Сообщение отправлено в канал")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("post", post))
    app.run_polling()

if __name__ == "__main__":
    main()
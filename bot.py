import os
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

MENU = {
    "dabeli": 25,
    "sev khaman": 25,
    "masala poha": 35,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send order like:\n\ndabeli 2\nsev khaman 1"
    )

async def handle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    try:
        parts = text.rsplit(" ", 1)

        item = parts[0]
        qty = int(parts[1])

        if item not in MENU:
            await update.message.reply_text(
                f"Item not found: {item}"
            )
            return

        total = MENU[item] * qty

        await update.message.reply_text(
            f"{item.title()} x{qty}\n\nTotal = ₹{total}"
        )

    except:
        await update.message.reply_text(
            "Format:\n\ndabeli 2"
        )

async def main():
    app = Application.builder().token(
        os.getenv("BOT_TOKEN")
    ).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_order)
    )

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())

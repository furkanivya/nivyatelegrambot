import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

TARGET_CHAT_IDS = [
    -1002791720688,
    -4834932252,
    -4919166229
]

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for chat_id in TARGET_CHAT_IDS:
        if chat_id != update.effective_chat.id:
            try:
                await context.bot.forward_message(
                    chat_id=chat_id,
                    from_chat_id=update.effective_chat.id,
                    message_id=update.message.message_id
                )
            except Exception as e:
                print(f"{chat_id} için hata oluştu: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward))
    print("Bot çalışıyor! Otomatik yönlendirme aktif 🚀")
    app.run_polling()

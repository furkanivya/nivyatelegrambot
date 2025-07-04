import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

# Kanal chat ID'leri
CHANNEL_IDS = [
    -1002791720688,
    -4834932252,
    -4919166229,
]

async def otomatik_paylas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    for kanal_id in CHANNEL_IDS:
        if kanal_id != chat_id:
            try:
                if update.message.text:
                    await context.bot.send_message(chat_id=kanal_id, text=update.message.text)
                elif update.message.photo:
                    photo = update.message.photo[-1]
                    caption = update.message.caption or ""
                    await context.bot.send_photo(chat_id=kanal_id, photo=photo.file_id, caption=caption)
                elif update.message.video:
                    video = update.message.video
                    caption = update.message.caption or ""
                    await context.bot.send_video(chat_id=kanal_id, video=video.file_id, caption=caption)
                elif update.message.document:
                    document = update.message.document
                    caption = update.message.caption or ""
                    await context.bot.send_document(chat_id=kanal_id, document=document.file_id, caption=caption)
                else:
                    print("Desteklenmeyen mesaj türü.")
            except Exception as e:
                print(f"{kanal_id} gönderim hatası: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, otomatik_paylas))
    print("Bot aktif, otomatik paylaşım açık 🚀")
    app.run_polling()

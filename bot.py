import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ChannelPostHandler, ContextTypes

TOKEN = os.getenv("TOKEN")  # ya da TOKEN = "bot_token"

# Kanaldan mesaj geldiğinde sadece log'a yazan handler
async def kanal_id_logla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    kanal_adi = chat.title
    kanal_id = chat.id

    # ✅ Sadece loglara yazıyoruz
    print(f"[Gizli] Kanal adı: {kanal_adi} | Kanal ID: {kanal_id}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChannelPostHandler(kanal_id_logla))
    print("Gizli ID botu aktif... Sadece loglara yazıyor 🕵️‍♀️")
    app.run_polling()

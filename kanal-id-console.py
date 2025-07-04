import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")  # ya da TOKEN = "BOT_TOKEN"

# Kanal mesajlarını yakalayan fonksiyon
async def kanal_id_logla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    if update.channel_post:  # sadece kanal gönderileri
        print(f"[Gizli] Kanal adı: {chat.title} | Kanal ID: {chat.id}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # Sadece kanal postlarını dinleyen handler
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, kanal_id_logla))

    print("Gizli ID botu aktif 💼")
    app.run_polling()

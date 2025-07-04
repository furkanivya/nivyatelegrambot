import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = os.getenv("TOKEN")

# Kanal ID’leri, örnek: -1001234567890 gibi
CHANNEL_IDS = [-1002791720688, -4834932252, -4919166229]

async def kanal_mesaj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mesaj = "📢 Bu mesaj kanaldan gönderiliyor!"
    for kanal_id in CHANNEL_IDS:
        try:
            await context.bot.send_message(chat_id=kanal_id, text=mesaj)
        except Exception as e:
            print(f"{kanal_id} için hata: {e}")
    await update.message.reply_text("Mesaj tüm kanallara gönderildi.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("kanalmesaj", kanal_mesaj))

    print("Bot çalışıyor! Kanal mesajları hazır 🚀")
    app.run_polling()

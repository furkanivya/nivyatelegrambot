import os
from telegram import Update, InputMediaPhoto, InputMediaVideo, InputMediaDocument
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

TARGET_CHAT_IDS = [
    -1002791720688,
    -4834932252,
    -4919166229,
]

async def forward_message_as_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Mesaj türüne göre işle
    if update.message.text:
        text = update.message.text
        for group_id in TARGET_CHAT_IDS:
            if group_id != chat_id:
                try:
                    await context.bot.send_message(chat_id=group_id, text=text)
                except Exception as e:
                    print(f"{group_id} için hata: {e}")

    elif update.message.photo:
        photo = update.message.photo[-1]  # En kaliteli foto
        caption = update.message.caption or ""
        for group_id in TARGET_CHAT_IDS:
            if group_id != chat_id:
                try:
                    await context.bot.send_photo(chat_id=group_id, photo=photo.file_id, caption=caption)
                except Exception as e:
                    print(f"{group_id} için hata: {e}")

    elif update.message.video:
        video = update.message.video
        caption = update.message.caption or ""
        for group_id in TARGET_CHAT_IDS:
            if group_id != chat_id:
                try:
                    await context.bot.send_video(chat_id=group_id, video=video.file_id, caption=caption)
                except Exception as e:
                    print(f"{group_id} için hata: {e}")

    elif update.message.document:
        document = update.message.document
        caption = update.message.caption or ""
        for group_id in TARGET_CHAT_IDS:
            if group_id != chat_id:
                try:
                    await context.bot.send_document(chat_id=group_id, document=document.file_id, caption=caption)
                except Exception as e:
                    print(f"{group_id} için hata: {e}")

    else:
        # Diğer medya türleri veya karma mesajlar için eklemeler yapılabilir
        print("Desteklenmeyen mesaj türü.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_message_as_new))
    print("Bot çalışıyor! Yeni mesaj olarak yönlendirme aktif 🚀")
    app.run_polling()

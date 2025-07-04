import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Mesajları göndereceğin grup ID'leri
TARGET_CHAT_IDS = [
    -1002791720688,  # Grup 1
    -4834932252,     # Grup 2
    -4919166229      # Grup 3
]

def forward(update: Update, context: CallbackContext):
    for chat_id in TARGET_CHAT_IDS:
        if chat_id != update.effective_chat.id:  # Mesajın geldiği yere tekrar gönderme
            try:
                context.bot.forward_message(
                    chat_id=chat_id,
                    from_chat_id=update.effective_chat.id,
                    message_id=update.message.message_id
                )
            except Exception as e:
                print(f"{chat_id} için hata oluştu: {e}")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(filters.ALL, forward))

    print("Bot çalışıyor! Otomatik yönlendirme aktif 🚀")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

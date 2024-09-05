from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext) -> None:
    # Кнопки с ссылками
    keyboard = [
        [InlineKeyboardButton("Открыть библиотеку крипто игр", url='https://t.me/CA_library_bot/CA_library?start=your_parameter')],
        [InlineKeyboardButton("Join community", url='https://t.me/Gentlemens_crypto_club')],
        [InlineKeyboardButton("наш X", url='https://x.com/')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем картинку из локального файла с кнопками
    with open(r'img/logowithcat.webp', 'rb') as photo:
        await context.bot.send_photo(chat_id=update.effective_chat.id, 
                                      photo=photo, 
                                      caption='Вот картинка, которая может быть полезна!', 
                                      reply_markup=reply_markup)

def main() -> None:
    print("Бот запущен...")  # Сообщение для отладки
    application = Application.builder().token("7370492160:AAFQ4STsqM2unb8mJJZlczU0uh7oEXDWlH8").build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()

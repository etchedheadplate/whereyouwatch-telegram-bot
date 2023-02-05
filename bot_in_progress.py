import telegram
import telegram.ext
import re
from random import randint
from parser_latest import showNextMovie
'''from parser_latest import present_movie'''

# Ключ API от BotFather:
API_KEY = "<PUT_YOUR_KEY_HERE>"
# Создаем апдейтер с ключем API:
updater = telegram.ext.Updater(API_KEY)
# Создаем диспетчер, с помощью которого добаляются обработчики:
dispatcher = updater.dispatcher
# Состояния в виде чисел:
WELCOME = 0
MOVIE = 1
SETTINGS = 2
CANCEL = 3

# Начальная функция:
def start(update_obj, context):
    # Отправляем сообщение и выводим кнопки для дальнейшего взаимодействия:
    update_obj.message.reply_text("Перейти в настройки или посмотреть последний репорт?",
        reply_markup=telegram.ReplyKeyboardMarkup([['Настройки', 'Репорт']], one_time_keyboard=True)
    )
    # Переходим в состояние WELCOME:
    return WELCOME

# Вспомогательная функция, отправляющая последний репорт:
def send_report(update_obj, context):
    # store the numbers in the context
    context.user_data['last_movie'] = showNextMovie
    # send the question
    update_obj.message.reply_text("Вот последний репорт:")

# В состоянии WELCOME проверить, выбрал ли пользователь посмотреть последний репорт:
def welcome(update_obj, context):
    if update_obj.message.text.lower() in ['Репорт']:
        # Отправляет репорт и переходит в состояние MOVIE:
        send_report(update_obj, context)
        return MOVIE
    else:
        # Уходит в состояние CANCEL:
        return CANCEL

# В состоянии MOVIE:
def next_movie(update_obj, context):
    # Команда для следующего репорта:
    more_movies = 'Еще'
    # Проверяет, была ли дана команда для следующего репорта:
    if more_movies == str(update_obj.message.text):
        # Зацыкливает в состояние MOVIE:
        send_report(update_obj, context)
        return MOVIE
    else:
        # При любом другом ответе:
        update_obj.message.reply_text("Возвращаю назад")
        # Возвращает в состояние WELCOME:
        return WELCOME

def cancel(update_obj, context):
    update_obj.message.reply_text('Выход', reply_markup=telegram.ReplyKeyboardRemove()
    )
    return telegram.ext.ConversationHandler.END

# Пустое состояние SETTINGS,(TODO):
def settings(update_obj, context):
    x = 'state'

# Создаем ConversationHandler с единственным состоянием:
yes_no_regex = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)
report = 'Репорт'
more = 'Еще'
bye = 'Выход'
handler = telegram.ext.ConversationHandler(
      entry_points=[telegram.ext.CommandHandler('start', start)],
      states={
            WELCOME: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(report), welcome)],
            MOVIE: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(more), next_movie)],
            CANCEL: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(bye), cancel)],
            SETTINGS: [telegram.ext.MessageHandler(telegram.ext.Filters.regex(yes_no_regex), settings)],
      },
      fallbacks=[telegram.ext.CommandHandler('cancel', cancel)],
      )
# Обработчик для диспетчера:
dispatcher.add_handler(handler)

# Метод, ожидающий апдейтов от Телеграма:
updater.start_polling()
# Работать до прерывания:
updater.idle()

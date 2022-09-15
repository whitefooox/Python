import random
from telegram import ReplyKeyboardMarkup
from config import token
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, Filters

keyboard_start = [
    ['/dice'], ['/timer']
]

keyboard_dice = [
    ['6-гранный', '2 6-гранных'], 
    ['20-гранный', 'вернуться назад']
]

keyboard_timer = [
    ['30 секунд', '1 минута'], 
    ['5 минут', 'вернуться назад']
]

keyboard_close = [
    ["/close"]
]

def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('dice', dice))
    dp.add_handler(CommandHandler('timer', timer))
    dp.add_handler(CommandHandler('close', close))
    dp.add_handler(MessageHandler(Filters.text, choice))
    updater.start_polling()
    updater.idle()

def start(update, context):
    keyboard = ReplyKeyboardMarkup(keyboard_start, resize_keyboard=True)
    update.message.reply_text('Выберите команду', reply_markup=keyboard)

def dice(update, context):
    keyboard = ReplyKeyboardMarkup(keyboard_dice, resize_keyboard=True)
    update.message.reply_text('Какая кость нужна?', reply_markup=keyboard)

def timer(update, context):
    keyboard = ReplyKeyboardMarkup(keyboard_timer, resize_keyboard=True)
    update.message.reply_text('Какое время нужно?', reply_markup=keyboard)

def dice_x(x, count):
    result = ''
    for _ in range(count):
        result += str(random.randint(1, x)) + " "
    return result

def remove_job_if_exists(name, context):
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True

def set_timer(update, context, x):
    chat_id = update.message.chat_id
    due = int(x)
    remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_once(task, due, context=chat_id, name=str(chat_id))
    keyboard = ReplyKeyboardMarkup(keyboard_close, resize_keyboard=True)
    update.message.reply_text(f'Засек {update.message.text}', reply_markup=keyboard)

def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Время истекло')

def choice(update, context):
    text = update.message.text
    if text == 'вернуться назад':
        start(update, context)
    elif text == '6-гранный':
        update.message.reply_text(dice_x(6, 1))
    elif text == '2 6-гранных':
        update.message.reply_text(dice_x(6, 2))
    elif text == '20-гранный':
        update.message.reply_text(dice_x(20, 1))
    elif text == '30 секунд':
        set_timer(update, context, 30)
    elif text == '1 минута':
        set_timer(update, context, 60)
    elif text == '5 минут':
        set_timer(update, context, 300)

def close(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Таймер успешно отменен!' if job_removed else 'Нет активных таймеров.'
    keyboard = ReplyKeyboardMarkup(keyboard_timer, resize_keyboard=True)
    update.message.reply_text(text, reply_markup=keyboard)

if __name__ == '__main__':
    main()

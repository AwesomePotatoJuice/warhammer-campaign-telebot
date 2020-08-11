import telebot

init_keyboard = telebot.types.ReplyKeyboardMarkup(True)
init_keyboard.row('Привет', 'Пока', "/writeToLeha")

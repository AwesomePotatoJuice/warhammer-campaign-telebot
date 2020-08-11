import telebot
import config
import keyboards
import util

bot = telebot.TeleBot(config.token)
init_keyboard = keyboards.init_keyboard
users = {'Alexey Surin': "125903729", 'Nikita Surin': '100369010'}
waiting_answer = {}


@bot.message_handler(commands=['start'])
def start_message_handler(message):
    bot.send_message(message.chat.id, 'Окей, давай поиграем', reply_markup=init_keyboard)
    print(message)


@bot.message_handler(commands=['init'])
def init_message_handler(message):
    bot.send_message(message.chat.id, 'Окей, давай поиграем', reply_markup=init_keyboard)
    log_message(message)


def log_message(message):
    print("********************")
    print(message)
    print(message.from_user.first_name + " said: " + message.text)
    print("********************")
    write_to_nikita_text("********************")
    write_to_nikita_text(message)
    write_to_nikita_text(message.from_user.first_name + " said: " + message.text)
    write_to_nikita_text("********************")


@bot.message_handler(commands=['writeToLeha'])
def write_to_leha_handler(message):
    # util.write_to_app_data("asd", "asd")
    waiting_answer[str(message.from_user.id)] = True
    bot.send_message(message.chat.id, 'Что ему написать?')

    log_message(message)


def waiting(user_id):
    if waiting_answer.get(user_id):
        waiting_answer[user_id] = False
        return True
    else:
        return False


@bot.message_handler(content_types=['text'])
def send_text_handler(message):
    if waiting(str(message.from_user.id)):
        write_to_leha(message.text)
    if str(message.from_user.id) == users.get('Alexey Surin'):
        write_to_nikita(message.text, 'Alexey Surin')
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        log_message(message)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
        log_message(message)
    else:
        log_message(message)


def write_to_nikita(text, from_who):
    if from_who != "":
        bot.send_message(users.get('Nikita Surin'), from_who + " wrote you: " + text)
    else:
        bot.send_message(users.get('Nikita Surin'), text)


def write_to_nikita_text(text):
    bot.send_message(users.get('Nikita Surin'), text)


def write_to_leha(text):
    bot.send_message(users.get('Alexey Surin'), text)


bot.polling()

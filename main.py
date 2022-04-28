import random
import telebot

token = '' #токен у каждого свой индивидуальный
bot = telebot.TeleBot(token)

tasks = {}

random_tasks = ['позвонить бабушке', 'позвонить маме', 'посмотреть фильм', 'поиграть в баскетбол'
]

def add(date, task):
    if date in tasks:
        # Дата есть в словаре
        # Добавляем в список задачу
        tasks[date].append(task)
    else:
        # Даты нет в словаре
        # Создаем записить с ключом date
        tasks[date] = []
        tasks[date].append(task)

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список.
/show - напечатать все добавления задачи.
/random - добавлять случайную задачу на дату Сегодня
"""

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def add_todo(message):
    command = message.text.split(maxsplit=2)
    add(command[1].lower(), command[2])
    bot.send_message(message.chat.id, 'Задача: ' + command[2] + '\n' + 'Добавлена на дату: ' + command[1].lower())

@bot.message_handler(commands=['random'])
def random_add(message):
    date = 'сегодня'
    task = random.choice(random_tasks)
    add(date, task)
    text = 'Задача: ' + task + '\n' + 'Добавлена на дату: ' + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show', 'print'])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text = text + '[]' + task + '\n'
    else:
        text = 'Задач на эту дату нет'
    bot.send_message(message.chat.id, text)

# Постоянно обращается к серверам телеграм
bot.polling(none_stop=True) # отправка к серверам телеграмм используя наш токен

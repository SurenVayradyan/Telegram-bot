import random
import telebot

token = '' #токен у каждого свой индивидуальный
bot = telebot.TeleBot(token)

tasks = {}

random_tasks = ['позвонить бабушке', 'позвонить маме', 'посмотреть фильм'
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

random_tasks = ['Позвонить бабушке', 'Позвонить маме', 'Посмотреть фильм'
]

tasks = {

    }

run = True

today = {

}
tomorrow = {

}
other = {

}

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
    print('Задача:', task, '\n''Добавлена на дату:', date)

    
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['add'])
def add_todo(message):
    command = message.text.split(maxsplit=2)
    add(command[1].lower(), command[2])
    bot.send_message(message.chat.id, 'Задача: ' + command[2] + '\n' + 'Добавлена на дату: ' + command[1].lower())

# while run:
#     command = input('Введите команду: ')
#     if command == 'help':
#         print(HELP)
#     elif command == 'show':
#         date = input("Введите дату для отображения списка задач на этот день: ")
#         if date in tasks:
#             for task in tasks[date]:
#                 print('-', task)
#         else:
#             print('Такой даты нет')
#             print('Попробуйте ввести другую дату')

#     elif command == 'add':
#         date = input('Введите дату для добавления задачи: ')
#         task = input('Введите какую задачу хотите добавить в список дел: ')
#         complite = input('Введите дату для выполнения задачи: ')
#         add(date, task)
#         if complite == 'Сегодня':
#             today[complite] = []
#             today[complite].append(complite)
#         elif complite == 'Завтра':
#             tomorrow[complite] = []
#             tomorrow[complite].append(complite)
#         else:
#             other[complite] = []
#             other[complite].append(complite)

#     elif command == 'random':
#         task = random.choice(random_tasks)
#         add('Сегодня',task)

#     elif command == 'exit':
#         print('Спасибо за использование! До свидания!')
#         break

#     else:
#         print('Неизвестная команда')
#         print('До свидания!')
#         break


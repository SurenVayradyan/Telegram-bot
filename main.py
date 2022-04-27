import random
import telebot



HELP = """
help - напечатать справку по программе.
add - добавить задачу в список.
show - напечатать все добавления задачи.
random - добавлять случайную задачу на дату Сегодня
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


while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        date = input("Введите дату для отображения списка задач на этот день: ")
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print('Такой даты нет')
            print('Попробуйте ввести другую дату')

    elif command == 'add':
        date = input('Введите дату для добавления задачи: ')
        task = input('Введите какую задачу хотите добавить в список дел: ')
        complite = input('Введите дату для выполнения задачи: ')
        add(date, task)
        if complite == 'Сегодня':
            today[complite] = []
            today[complite].append(complite)
        elif complite == 'Завтра':
            tomorrow[complite] = []
            tomorrow[complite].append(complite)
        else:
            other[complite] = []
            other[complite].append(complite)

    elif command == 'random':
        task = random.choice(random_tasks)
        add('Сегодня',task)

    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break

    else:
        print('Неизвестная команда')
        print('До свидания!')
        break


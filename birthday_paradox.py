""" Парадокс дней рождения, также известный как задача
о днях рождения, заключается в удивительно высокой
вероятности того, что у двух человек совпадает день рож-
дения даже в относительно небольшой группе людей.
В группе из 70 человек вероятность совпадения дней рож-
дения у двух людей составляет 99,9 %. Но даже в группе всего
лишь из 23 человек вероятность совпадения дней рождения
составляет 50 %. Приведенная программа производит несколько вероятностных
экспериментов, чтобы определить процентные соотношения для групп различного
размера. Подобные эксперименты с определением возможных исходов с помощью
множества случайных испытаний называются экспериментами Монте-Карло. """

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Возвращаем списак объектов дат для случайных дней рождения"""

    birthdays = []

    for i in range(numberOfBirthdays):
        # Год в модели роли не играет,лишь бы в объектах дней рождения он был одинаков.
        startOfYear = datetime.date(2000, 1, 1)
        # получение случайного дня года
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Возвращаем объект даты дня рождения,встречающегося несколько раз"""

    if len(birthdays) == len(set(birthdays)):
        return None  # Все дни рождения различны.
    # Сравниваем попарно.
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA  # возвращаем найденное соответствие


# создаём корткж с месяцами
MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

while True: # Запрашиваем сколько дней рождений от пользователяЖ
    print('Сколько дней рождений генерировать? максимальное число 100')
    response =input('> ')
    if response.isdecimal() and (0<int(response)<=100):
        numBDays=int(response)
        break #Пользователь ввёл допустимое значение.
#Генерируем и отображаем дни рождения

print('Сгенерировано дней рождений:',numBDays,)
birthdays=getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i!=0:
        #Выводим запятую для каждого дня рждения после.
        print(', ', end='')
    monthName=MONTHS[birthday.month-1]   
    dateText=f'{monthName} {birthday.day}'
    print(dateText,end='')
print()
print() 

# Выясняем, встречаются ли два совпадающих дня рождения.
match=getMatch(birthdays)

# Отображаем результаты:

print('In this simulation, ', end='')

if match !=None:
    manthName=MONTHS[match.month-1]
    dateText=f'{monthName} {match.day}'
    print('у нескольких людей дни рождения', dateText)

else:
    print('Отсутсвует повторяющие дни рождения')
print()

# Произваодим 100 000 операций имитационного моделирования:

print("Генерация", numBDays,'случайные дни рождения 100 000 раз...')
input('Нажмите Enter, чтобы начать.')

print('запуск симуляций')

simMatch =0 # Число операций моделирования с совпадающими днями рождениями
for i in range(10_000):
    #Отображаем сообщение о ходе выполнения каждые 10 000 операций.
    if i%10_000==0:
        print(i,'симуляция')
    birthdays=getBirthdays(numBDays)
    if getMatch(birthdays) !=None:
        simMatch=simMatch+1
print('100,000 симуляций.')

#Отображаем результаты имитационного моделирования:

probability=round(simMatch / 100_00*100,2)
print("Из 100,000 симуляций", numBDays,)
print('соответствует дню рождения в этой группе', simMatch, 'раз. Это означает')
print('что в группе из', numBDays, 'людей, есть', probability, '%,')
print('что будут совпадения дня рождения.')
print('Это, наверное, больше, чем вы думаете!')    
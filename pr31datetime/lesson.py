# import random

# x = random.randint(1, 100)
# user_num = 0
# cnt = 0
# while True:
#     user_num = int(input("Я загадал число от 1 до 100. Угадай его: "))
#     cnt += + 1
#     if user_num == x:
#         print(f'Ты угадал число за {cnt} попыток')
#         print("Спасибо за игру!")
#         is_new_game = input("Хотите ли сыграть еще? (yes/no): ")
#         if is_new_game == 'yes':
#             x = random.randint(1, 100)
#             cnt = 0
#         elif is_new_game == 'no':
#             print("Еще раз спасибо за игру! Возвращайтесь снова!")
#             break
#         else:
#             is_new_game = input("Играете или нет? (yes/no): ")
#     elif user_num > x:
#         print("Мое число меньше")
#     else:
#         print("Мое число больше")

import locale
from datetime import date, datetime, timedelta


# date
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())


print('\n')
# datetime
today_time = datetime.today()
now = datetime.now()

print(today_time.today())
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.weekday())
print(now.hour)
print(now.minute)
print(now.second)

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[now.weekday()])

locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
print('\n')
print(now.strftime('%a'))
print(now.strftime('%A'))
print(f"Дата: {now.strftime('%A, %d %b %Y')}")
print(f"Час: {now.strftime('%H:%M:%S')}")
print('\n')
print(now.strftime('%c'))
print(now.strftime('%x'))
print(now.strftime('%X'))

print('\n')
now2 = datetime.today()
print(now2.strftime('%c'))
d1 = now2 + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))

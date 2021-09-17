print(2 > 3)
print(2 < 3)

x = 0
if x:
    print("Переменная х вернула истину")
else:
    print("Переменная х вернула ложь")

if 1:
    print("Выражение истинно")
else:
    print("Выражение ложно")

light = 'red'
if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Wait')
elif light == 'green':
    print("Go")
else:
    print('What')

age = int(input("Сколько Вам лет? "))
if age > 18:
    print("Добро пожаловать!")
else:
    print(f"Вам еще рано. Вам не хватает {18 - age} лет для входа.")

time = 11
if time < 12 or time > 13:
    print("Open")
else:
    print("Close")

time1 = 11
day = 'su'
if time1 >= 8 and day != 'su':
    print("Open")
else:
    print("Close")

x1 = 0
if not x1:
    print("OK")
else: 
    print("NO")

x2 = 1
res = "OK" if x2 else "NO"
print("Res", res)

# searching_number = 27

# print("Guess the number")

# a = input('Your option: ')

# while int(a) != searching_number:
#     if int(a) > searching_number:
#         print("Less")
#         a = input('Your option: ')
#     elif int(a) < searching_number:
#         print("More")
#         a = input('Your option: ')
# else:
#     print("You guessed, the number is: ", searching_number)

x = 75
user_num = 0
cnt = 0
while True:
    user_num = int(input("Я загадал число от 1 до 100. Угадай его: "))
    cnt += + 1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        print("Спасибо за игру!")
        break
    elif user_num > x:
        print("Мое число меньше")
    else:
        print("Мое число больше")

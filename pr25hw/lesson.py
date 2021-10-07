searching_number = 27

print("Guess the number")

a = input('Your option: ')

while int(a) != searching_number:
    if int(a) > searching_number:
        print("Less")
        a = input('Your option: ')
    elif int(a) < searching_number:
        print("More")
        a = input('Your option: ')
else:
    print("You guessed, the number is: ", searching_number)

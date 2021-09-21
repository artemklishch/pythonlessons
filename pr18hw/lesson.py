import math

l1 = [1, 2, 3]
l2 = []
for i in l1:
    l2.append(i * 2)
else:
    print(l2)

l2 = [1, 2, 3]
sum = 0
for i in l2:
    val = i * i
    sum += val
else:
    print(sum)

time1 = 3
time2 = 6.7
time3 = 11.8
times = [time1, time2, time3]
liters = 0
for i in times:
    # val = math.floor(i * 0.5)
    # liters += val

    # string = ''
    # for j in str(i * 0.5):
    #     if j == '.':
    #         break
    #     else:
    #         string += j
    # liters += int(string)

    string = str(i * 0.5).split(".")[0]
    liters += int(string)
else:
    print(liters)

string1 = 'Hello world'
string2 = ""
is_there_space = string1.find(" ") != -1
if is_there_space:
    for i in string1:
        string2 += i.capitalize()
    else:
        print(string2)

l11 = [1, 2, 3]
l22 = [i * 2 for i in l11]
print('hw1', l22)

res = 0
for i in l11:
    res += i ** 2
print('hw2', res)


time11 = 3
time22 = 6.7
time33 = 11.8
print('hw3', int(time11 // 2))
print('hw3', int(time22 // 2))
print('hw3', int(time33 // 2))
print('hw3', int(time11 / 2))
print('hw3', int(time22 / 2))
print('hw3', int(time33 / 2))

string11 = 'Hello world'
if " " in string11:
    string11 = string11.upper()
else:
    string11.lower()
print('hw4', string11)

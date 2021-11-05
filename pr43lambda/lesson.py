# def get_square(num):
#     return num ** 2


# print(get_square(5))

# get_square = lambda num: num ** 2
# print(get_square(5))

# print((lambda num: num ** 2)(10))

l1 = [1, 2, 3]


# def get_double(l):
#     return [i*2 for i in l]

def get_double(l):
    return list(map(lambda num: num * 2, l))  # [i*2 for i in l]


print(get_double(l1))

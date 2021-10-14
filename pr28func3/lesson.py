def get_sum1(a, b):
    """
    Returns sum of numbers - a nad b.

    :param a: first arg
    :type a: int
    :param b: second arg
    :type b: int
    :return: Return int
    """
    return a+b


print(get_sum1(1, 2))

a = 5  # глобальная переменная, внутри функции доступна только на чтение


def func1():
    a = 10  # локальная переменная
    print(a)


func1()
print(a)


def func2():
    global a
    a += 1


print('\n')
print(a)
func2()
print(a)

print('\n')

l1 = [1, '2', 3]


def func3(l):
    return [i * 2 for i in l]


print(func3(l1))


def func4(l):
    def get_mult(x):
        return int(x) * 2
    return [get_mult(i) for i in l]


print(func4(l1))


def func5(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)]


print(func5(l1))


def func6(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))


print(func6(l1))

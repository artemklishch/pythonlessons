def set_regicter(s):
    if " " in s:
        return s.upper()
    else:
        return s.lower()


print(set_regicter("Hello world"))
print(set_regicter("Helloworld"))


def get_sum(a, b, c=0, d=1):
    return a+b+c+d


print(get_sum(1, 2, 5, 7))
print(get_sum(1, 2))
print(get_sum(1, 2, d=5))


def get_sum2(*args):  # args буде преобразовано в кортеж
    return sum(args)


print(get_sum2(1, 2, 3))


def func1(**kwargs):
    print(kwargs)


# func1(1, 2, 3) это не работает
func1(a=1, b=5, c=-20)


def func2(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)


func2(1, "hello", 3, 4, e='t', b='test')

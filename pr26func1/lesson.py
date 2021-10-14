def hello(name, word):
    print("Hello, " + name + ". Say, " + word)


hello("Bob", "hi")
hello("Kat", "hello")


def get_sum(a, b):
    print(a+b)


x = 2
y = 5
get_sum(1, 3)
get_sum(x, y)


def get_sum2(a, b):
    return a+b


print(get_sum2(0, 1))

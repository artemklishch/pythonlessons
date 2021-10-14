# 1
l1 = [1, "event", 4, "even", "even", "odd", 5]
l2 = [1, "event", 4, "even", "even", "odd", 15]


def odd_ball(l):
    return l.index('odd') in l


print(odd_ball(l1))
print(odd_ball(l2))


# 2
def get_sum(num):
    return sum(i for i in range(1, num + 1) if i % 5 == 0 or i % 3 == 0)


print(get_sum(5))
print(get_sum(10))

# 3
names1 = ['bob', 'jhon', 'kirian', 'robi']


def get_names(names):
    return [i for i in names if len(i) == 4]


print(get_names(names1))

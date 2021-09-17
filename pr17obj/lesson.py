x = 10
print(x, id(x))
x = 20
print(x, id(x))

s = 'hello'
print(s, id(s))
s += ' world'
print(s, id(s))

l = [1, 2, 3]
print(l, id(l))
l.append(5)
print(l, id(l))

a = 10
b = a
print(a, id(a))
print(b, id(b))
a = 15
print(a, id(a))
print(b, id(b))

l1 = [1,2,3]
l2 = l1
l3 = l1.copy()
print(l1, id(l1))
print(l2, id(l2))
l2.append(5)
print(l1, id(l1))
print(l2, id(l2))
print(l3, id(l3))

c = 10
print('c del', c)
del c
print(c)

t1 = (1, 2, 3)
l1 = [1, 2, 3]
print(type(t1))

t2 = 1, 2, 3
print(t2)

t3 = tuple((1, 2, 3))
print(t3)

t4 = ()
print(t4)

t51 = (1)
t52 = (1,)
print(type(t51))
print(type(t52))

t6 = tuple("hello")
print(t6)
print(t6[1])

t7 = (1, 2, 3)
l7 = [1, 2, 3]
print(t7.__sizeof__())
print(l7.__sizeof__())

t8 = tuple('Hello')
t9 = tuple(' world')
t10 = t8 + t9
print(t10)
print(t8.__len__())
print(len(t8))
print(t10.count("l"))
print(t10.index("e"))

if "a" in t10:
    print(t10.index("a"))
else:
    print("NO")

for i in t10:
    print(i, end=" ")
print('\n')
for i in t10:
    if i == ' ':
        continue
    print(i, end=" ")
print('\n')
t11 = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
print(t11, id(t11))
t11[4][0] = 'new'
t11[4].append("hello")
print(t11, id(t11))

t12 = (1, 2, 3)
# x = t12[0]
# y = t12[1]
# z = t12[2]
x, y, z = t12
print(x, y, z, end=' ')
print("\n")

a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

l = [1, 2, 3, "hello", ["test", 10], "world", True]
names = ['Bob', "Tom", "John"]

print(l)
print(len(l))
print(names[0])
print(l[4][0])
print(l[0:3])

l[2] = 'world'
print(l)

l[:2] = [10, 15]
print(l)

l.append("new")
print(l)
l.extend([5, 7])
print(l)

l2 = ['hi', 12]
l += l2
print(l)

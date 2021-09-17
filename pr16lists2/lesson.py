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

l.insert(1, 'test')
print(l)

l.remove('world')
print(l)

el = l.pop()
el2 = l.pop(1)
print(l, el, el2)

pos1 = l.index("hello")
print(pos1)

l.insert(2, 'world')
print(l.count("world"))

l3 = ['hello', 'hi', 'David', 'test']
l3.sort()
print(l3)

l4 = [1, 2, 3, 4, 5, 6, 7]
l4.reverse()
print(l4)
l5 = l4.copy()
print(l5)
l4.clear()
print(l4)
print('h' > 'a')
l5 = sorted(l5)
print(l5)

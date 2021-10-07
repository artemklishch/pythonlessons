s1 = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(type(s1))
print(s1)

s2 = set("hello")
print(s2)

s3 = {i for i in range(1, 11)}
print(s3)

s4 = {5, 3, 10, 1, 9}
print(s4)

s5 = {}
s6 = set()
print(type(s5))
print(type(s6))

nums = [1, 2, 3, 3, 2, 5]
nums2 = set(nums)
nums3 = list(nums2)
print(nums2)
print(nums3)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

c = a - b  # вычитаем из "а" все буквы, которые есть в "b"
print(c)  # {'r', 'd', 'b'}

d = a | b  # объединение
print(d)

e = a & b  # пересечение - буквы, к-е есть и в "а" и в "b"
print(e)

f = a ^ b  # множество из элементов - буквы в "а" или "b", но не в обоих
print(f)


print('\n')
# set.copy() - возвращает копию множества
# set.add(elem) - добавляет элемент в множество
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует
# set.discard(elem) - удаляет элемент, если он находится в множестве
# set.pop() - возвращает и удаляет первый элемент из множества;
# так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым
# set.clear() - очистка множества

s7 = {"apple", "orange", "apple", "pear", "orange", "banana"}
s71 = set.copy(s7)
print(s71)
s7.add("coca cola")
print(s7)
s7.remove("coca cola")
print(s7)
s7.discard("pear")
print(s7)
var1 = s7.pop()
print(var1)
print(s7)
s7.clear()
print(s7)

print('\n')

s8 = frozenset('hello') # нелдьзя изменить
print(s8)

for i in s71:
    print(i)

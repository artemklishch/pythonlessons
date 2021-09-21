words = ["мадам", "топот", "test", "madam", "word"]
my_str = ["Око за око", "А роза упала на лапу азора", "Около Миши молоко"]

words2 = []
for i in words:
    l = [i for i in i]
    l.reverse()
    str1 = "".join(l)
    if i == str1:
        words2.append(str1)
print(words2)


words3 = []
for word in words:
    if word == word[::-1]:
        words3.append(word)
print(words3)

print([word for word in words if word == word[::-1]])


my_str2 = []
for i in my_str:
    l1 = [i for i in i if i != " "]
    l2 = l1.copy()
    l2.reverse()
    str1 = "".join(l1).lower()
    str2 = "".join(l2).lower()
    if str1 == str2:
        my_str2.append(i)
print(my_str2)

my_str3 = []
for str2 in my_str:
    str_r = str2.replace(" ", "").lower()
    if str_r == str_r[::-1]:
        my_str3.append(str2)
print(my_str3)

l1 = list(range(1,10))
l2 = list("hello")
print(l1)
s = "-".join(map(str, l1))
print(s)

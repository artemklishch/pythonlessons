# dict.clear() - очищает словарь
# dict.copy() - возвращает копию словаря
# dict.get(key[,default]) - возвращает значение ключа, но если его нет,
# не бросает исключение, а возвращает default (по умолчанию None)
# dict.items() - возвращает пары (ключ, значение)
# dict.keys() - возвращает ключи словаря
# dict.pop(key[,default]) - удаляет ключ и возвращает значение;
# если ключа нет, возвращает default (по умолчанию бросает исключение)
# dict.popitem() - удаляет и возвращает пару (ключ, значение); если словарь пуст, бросает исключение
# dict.setdefault(key[,default]) - возвращает значение ключа;
# если ключа нет, не бросает исключение, а создает ключ со значением defaul (по умолчанию None)
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other;
# существующие ключи перезаписываются; возвращает None (не новый словарь)
# dict.values() - возвращает значения словаря

product1 = {'title': "Sony", 'price': 100}
print(product1.items())
print(product1.keys())
print(product1.pop('title2', 'No'))
# print(product1.popitem())
print('\n')
print(product1)
product1.setdefault('type')
print(product1)
product1.update({'test': 'value'})
print(product1)
print(product1.values())

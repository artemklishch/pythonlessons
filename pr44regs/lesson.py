import re
s1 = "Это просто строка текста. А это еще одна строка текста."
pattern = 'строка'
# print(s1.find(pattern))
# print(pattern in s1)

if re.search(pattern, s1):
    print('Matched')
else:
    print('No match')

match = re.search(pattern, s1)
print(match)
print(match.span())
print(match.start())
print(match.end())
print(re.match(pattern, s1))  # смотрит в начале строки
print(re.findall(pattern, s1))
print(re.split(r'\.', s1))
print(re.split(r'\.', s1, 1))  # разделение только 1 раз

s2 = '''Это просто строка текста
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ۳, ۶, ९, 10
Ф это строка с разными символами: "!", "@", "-", "&", "?", "_"
a\\b\tc
test string
'''
pattern2 = r'\w'
pattern3 = r'\w+'
pattern4 = r'[тэ]'
pattern5 = r'[тэ]+'
pattern6 = r'[а-я0-9]+'
pattern7 = r'[а-яё]+'
pattern8 = r'[0-9]+'
pattern9 = r'\d+'
pattern10 = r'[\d-]+'
pattern11 = r'[\da-]+'
pattern12 = r'a\\b\tc'
print(re.findall(pattern2, s2))
print(re.findall(pattern3, s2))
print(re.findall(pattern4, s2))
print(re.findall(pattern5, s2))
print(re.findall(pattern6, s2))
print(re.findall(pattern7, s2, flags=re.IGNORECASE))
print(re.findall(pattern8, s2))
print(re.findall(pattern9, s2))
print(re.findall(pattern10, s2))
print(re.findall(pattern11, s2))
print(re.findall(pattern12, s2))


# mail@mail.com
# name@bank
# email@google.com.ua

def validate_email(email):
    return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email)


print(validate_email("mail@mail.com"))
print(validate_email("name@bank"))
print(validate_email("email@google.com.ua"))

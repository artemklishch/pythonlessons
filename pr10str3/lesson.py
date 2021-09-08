s1 = 'hello world'
s2 = '1234'
s3 = 'helloworld'
print(len(s1))
print(s1.capitalize())
print(s1.center(20))
print(s1.center(20, '!'))
print(s1.count('l'))
print(s1.count('l', 0, 3))
print(s1.find('l'))
print(s1.find('a'))
print(s1.replace('l', 't'))
print(s1.split(' '))
print(s1.split())
print(s1.split(','))
print(s1.isdigit())
print(s2.isdigit())
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())

print(s3.isalnum())
print(s3.islower())
print(s3.isupper())

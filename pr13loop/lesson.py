i = 1

while i <= 10:
    print(i, end=' ')
    i += 1

print('hello', 'world')
print('hello', 'world', sep="!", end=" ")
print('hello', 'world', sep="!")
print('hello2', 'world2')

s = "Hello world"
for l in s:
    if l == ' ':
        continue
    print(f'"{l}"', end=' ')

str = 'hello world'
iterator = 0
for l in str:
    if l == ' ':
        break
    print(l, end='\n')
else:
    print('\nNo spaces')

year = 1900
while year <= 2021:
    print(year)
    year += 1
else:
    print("Done")

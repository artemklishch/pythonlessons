name = 'John'
age = 30

print('My name is ' + name + ". I'm " + str(age) + ' years')
print("My name is %(name)s. I'm %(age)d years" %{"name": name, "age": age})

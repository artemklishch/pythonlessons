name = 'John'
age = 30

print('My name is ' + name + ". I'm " + str(age) + ' years')
print("My name is %(name)s. I'm %(age)d years" % {"name": name, "age": age})
print("My %(age)d name is %(name)s. I'm %(age)d years" %
      {"name": name, "age": age})
print("My name is %s. I'm %d years" % (name, age))
print("My name is %s. I'm %d years" % ("David", age))
print("Title: %s, Price: %f" % ("Sony", 40))
print("Title: %s, Price: %.2f" % ("Sony", 40))

print("My name is {}. I'm {} years".format(name, age))
print("My name is {0}. I'm {1} years".format(name, age))
print("My {1} name is {0}. I'm {1} years".format(name, age))
print("My name is {name}. I'm {age} years".format(name=name, age=age))
print(f"My name is {name}. I'm {age} years")
print(f"My name is {name}. I'm {age + 5} years")
print("5+2 = {}".format(5+2))
print(f"5+2 = {5+7}")

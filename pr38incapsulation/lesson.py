from classes import Person
# import classes

person1 = Person("Tom")
person1.print_info()

person2 = Person("Bob")

# person2.__age = 30 # just creates the new proprety,
# and not changes the '__age' property in the object

# print(person2.__age) # this is impossible
# print(person2._Person__age) # access to '__age' properry

# print(person2.get_age())
# person2.set_age(-10)

print(person2.age)
person2.age = 35
person2.print_info()

from classes import Person, Employee

person1 = Person("Tom", 30)
person1.print_info()

print(person1.age)
person1.age = 35
person1.print_info()

employee1 = Employee("Bob", 35, "Soccer")
employee1.print_info()
employee1.more_info()

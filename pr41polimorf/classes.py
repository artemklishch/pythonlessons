class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # def get_age(self):
    #     return self.__age

    # def set_age(self, value):
    #     if value in range(1, 100):
    #         self.__age = value
    #     else:
    #         print("Wrong page")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 100):
            self.__age = value
        else:
            print("Wrong page")

    def __str__(self):
        # return f'Name is {self.name}'
        return 'Class ' + self.__class__.__name__


class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def more_info(self):
        print(f'{self.name} works in {self.company}.')

    def print_info(self):
        # print(
        #     f'Worker\'s name: {self.name}; age: {self.age}, company: {self.company}')
        super().print_info()
        print(f'Work is company: {self.company}')

    # def __str__(self):
    #     # return f'Name is {self.name}'
    #     return 'Class ' + self.__class__.__name__

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


class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def more_info(self):
        print(f'{self.name} works in {self.company}. Company: {self.company}')

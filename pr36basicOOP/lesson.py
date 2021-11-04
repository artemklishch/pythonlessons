class A:
    property1 = 'Property 1'
    property2 = 'Property 2'

    # def say_hi(self, name='guest'):  # self - ключевое слово, указывает на объект
    #     return 'Hi, ' + name
    name = 'guest'

    def say_hi(self, name=''):  # self - ключевое слово, указывает на объект
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name


a = A()
b = A()
# a.property1 = 'Property 1'
# a.property2 = 'Property 2'
print(a)
print(a.property1)
print(a.property2)
print(a.say_hi("Bob"))
print(a.say_hi())

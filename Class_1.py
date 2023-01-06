class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print('Hi, How do yoy do ?', self.name)

p = Person('Michael')
p.sayHi()



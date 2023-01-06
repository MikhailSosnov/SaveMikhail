class Nikolay:
    def __init__(self, firstname = 'Николай', surname = 'Токарев'):
        self.firstname = firstname
        self.surname = surname


    def name_age(self, age = 33):
        self.age = age
        if self.firstname != 'Николай':
            self.firstname = 'Все равно Николай'

        elif self.firstname == 'Николай':
            self.firstname = 'Николай'

        self.name_sur_age = self.firstname + ' ' + self.surname + ' ' + str(self.age) + ' лет'

        return(self.name_sur_age)

    def info(self):
        print(self.name_sur_age)


obj1 = Nikolay('Алексей', 'Крылов')
obj1.name_age(86)
obj1.info()

obj2 = Nikolay('Николай', 'Ослов')
obj2.name_age()
obj2.info()
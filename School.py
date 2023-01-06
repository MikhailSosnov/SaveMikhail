class SchoolMember:
    '''Представляет любого человека в щколе'''
    def __init__(self, name = 'Хрюкасий', age = 0.4):
        self.name = name
        self.age = age
        print('(Создан SchoolMeber: {0})'. format(self.name))

    def tell(self):
        '''Вывести информацию'''
        print('Имя: "{0}" Возраст: "{1}"'.format(self.name, self.age), end = ' ')

class Teacher(SchoolMember):
    '''Представление преподавателя'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher:{0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата:"{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представление студента'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student:{0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки:"{0:d}"'.format(self.marks))

# SM1 = SchoolMember('Афанасий', 0.3)
# SchoolMember().tell()
# SM1.tell()
t = Teacher('Мистер Куравлев', 41, 22000)
s = Student('Азамат Салехов', 25, 75)

print()

# t.tell()
# s.tell()

members = [t, s]

for member in members:
    member.tell()







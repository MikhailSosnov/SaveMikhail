class Robot:
    '''Представляет работу с именами.'''
    # Переменная класса, содержащай количество роботов
    population = 0

    def __init__(self, name):
        '''Инициализация данных'''
        self.name = name
#         print(self.name, Robot.population)
# proba1 = Robot
# proba1('Dum')
        print('(Инициализация {0})'.format(self.name))
        # При создании этой личности робот добавляется к пееменной 'ppulation'
        Robot.population += 1

    def __del__(self):
        ''' Я умираю '''
        print ('{0} уничтожается !'.format(self.name))

        Robot.population -=1

        if Robot.population == 0:
            print('{0} ,был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов. '.format(Robot.population))

    def sayHi(self):
        '''Приветствие робота'''
        print('Приветствую! Мои хозяйва наывают меня {0}'.format(Robot.population))

    def howMany():
        '''Выводит численность роботов'''
        print('У нас {0:d} роботов. '.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2 - D2')
droid1.sayHi()
Robot.howMany()

print('\nЗдесь роботы могут проделать какую-то работу.\n')

print('Роботы закончили свою аработу. Давайте уничтожим их.')
droid2 = Robot('CCC')
del droid1
del droid2

Robot.howMany()







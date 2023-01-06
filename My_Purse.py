class Purse:

    def __init__(self, valuta, name='Patrik'):

        self.money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.money = self.money + howmany
        print(self.money, self.valuta, 'владелец', self.name)

    def in_rub (self, kurs = 60.5):
        # kurs = input('Введите курс валюты:')
        self.kurs = float(input('Введите курс валюты:'))
        print('Рублей о курсу:', self.money * self.kurs)
# print(self.money, self.valuta, 'владелец', self.name, 'по курсу',
        #       self.curs, 'за один', self.valuta, '=' self.money * self.kurs)

    def info(self):
        print(self.money)

x = Purse('EUR')
x.top_up_balance(100)
x.in_rub(50)
x.info()
x.money = 1000

x.info()



# print(self.money)
# y = Purse ('Usd', 'greg')



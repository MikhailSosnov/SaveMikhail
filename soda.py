class Class_soda():
    '''описание класса газировки'''
    def __init__(self, add_soda):
         if isinstance(add_soda, str):
            self.add_soda = add_soda
         else:
             self.add_soda = None

    def napitok(self):

        if self.add_soda:
            print('Газировка с добавкой', self.add_soda)
        else:
            print('Обычная газировка')

obj1 = Class_soda ('лимона')
obj1.napitok()
x = 'hh'
x = str(type(type(x)))
print(x)
obj2 = Class_soda (x)
obj2.napitok()


        # self.familia = familia
        # self.spesies = spesies
        # self.life_lenth = 0
        # self.height = 0
        # self.weit = 0
        # self.place = ' '
        # self.cantry = ' '

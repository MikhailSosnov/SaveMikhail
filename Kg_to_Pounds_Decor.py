class Kg_to_pounds():

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        # print(self.__kg * 2.25)
        self.__kg *= 2.205

    @property
    def decor_weit(self):
        return self.__kg

    @decor_weit.setter
    def decor_weit(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
            return self.__kg
        else:
            raise ValueError('Килограммы задаются только числаи')

    def info (self):
        print('Фунты:',self.__kg)

obj1 = Kg_to_pounds(15)

print(obj1.decor_weit)

obj1.decor_weit = 10
print(obj1.decor_weit)

obj1.to_pounds()
obj1.info()
# print(print(obj1.set_kg(10)))




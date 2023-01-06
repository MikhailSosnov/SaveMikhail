class First:
    def heelo(self):
        print('Hello')

class CastleBravo:
    '''Испытание водородной бомбы'''
    def h_bomb(self):
        print('Castl Bravo - 15 мегатонн')

class Second(First):
    pass

class Bikini(CastleBravo):
    '''Изгаженный рай'''
    pass

b1 = Bikini()
print(Bikini.__mro__)
print(CastleBravo.__mro__)
print(CastleBravo.__doc__)
# print(CastleBravo.__doc__)
print(b1.__doc__)
print(Bikini.__bases__)
print(CastleBravo.__bases__)

print(Bikini.__dict__)
print(CastleBravo.__dict__)\

print(Bikini.__module__)
print(CastleBravo.__module__)
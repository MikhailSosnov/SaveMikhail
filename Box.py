class Box:
    '''Constraction'''
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, a=3, b=4, c=5):
        self.a = a
        self.b = b
        self.c = c
        volume = self.a * self.b * self.c
        print(volume)

b1 = Box(10, 20, 30)
b1(2, 3, 4)
b1()

print(b1.__doc__)
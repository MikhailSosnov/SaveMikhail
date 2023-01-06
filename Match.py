class Match:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def addition(self):
        print('addition ', self.a + self.b)

    def division(self, a = 3, b = 2):
        self.a = a
        self.b = b
        print('division ', self.a / self.b)


m1 = Match(100, 1000)
m1.addition()

m2 = Match(10, 2)
m2.division(1000, 25)
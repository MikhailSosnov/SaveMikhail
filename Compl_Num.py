class ComplNum:
    def __init__(self, x=0, y=0):
        if type(x) == ComplNum:
            self.Re = x.Re
            self.Im = x.Im
        else:
            self.Re = x
            self.Im = y

    def show(self):
        print('Re =', self.Re)
        print('Im =', self.Im)

c1 = ComplNum()
c2 = ComplNum(1,2)
c3 = ComplNum(c2)

c1.show()
c2.show()

c1.Re = 10
c1.Im = 20
c3.show()
c2.show()



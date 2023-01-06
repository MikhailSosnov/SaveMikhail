class Base:
    def __init__(self, x =12, y = 33):
        self.x = x
        self.y = y

    def get_v(self):
        # return self.x, self.y
        print('Pigs')
        # pass

    def set_v(self):
        self.x += 5
        self.y += 10

    def show(self):
        print(self.x, self.y)

class Chaild(Base):
    def __init__(self, z, v):
        self.z = z
        self.v = v

        def set_v(self):
            self.x -= 10
            self.y += 100

        def show(self):
            print(self.x, self.y)

# Base().get_v()

# b1 = Base()
c1 = Chaild(2, 3)
c1.get_v()

# b1 = Base()
# print(b1.x, b1.y)
#
# b2 = Base(1, 4)
# print(b2.x, b2.y)
#
# # b1.show(2, 70)
#
# b1.show()
#
# b2.show()
#
# b3 = Base(20, 40)
# b3.set_v()
# b3.show()

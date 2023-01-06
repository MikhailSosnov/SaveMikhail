class Point:
    MaxCoord = 121
    MinCoord = 3

    def __init__(self, x, y):
        # if self.MinCoord <= x <= self.MaxCoord:
        #     self.x = x
        #     self.y = y
        # else:
        #     self.x = 3
        #     self.y = y
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MinCoord <= x <= self.MaxCoord:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MinCoord = left

    def __getattribute__(self, item):
        print('__getattribute__')
        object.__getattribute__(self, item)

pt1 = Point(4, 120)
print(pt1.x, pt1.y)

pt2 = Point(2, 10)
print(pt2.x, pt2.y)

print(Point.__dict__)
print(pt2.__dict__)

# pt1.set_bound(-100)
# print(pt1.x, pt1.y)

print(pt1.__dict__)
print(Point.__dict__)

a = pt1.x




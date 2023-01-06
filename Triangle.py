class Triangle_check():
    def __init__(self, size):
        self.size = size

    def check_tr(self):
        if all(isinstance(size, (int, float)) for size in self.size):
            self.size.sort()
            if len(self.size) != 3:
                print('введено неверное число сторон')
            elif self.size[0] <= 0:
                print('как минимум одно число отрицательное или равно нулю')
            elif (self.size[0] + self.size[1]) <= self.size[2]:
                print('при таких длиннах сторон треугольник не может быть построен')
            elif (self.size[0] +self.size[2]) > self.size[2]:
                print('треугольник может быть построен')
        else:
            print('не все значения цифровые')

        print(self.size)



triangle1 = Triangle_check([43, 14, 15])
triangle1.check_tr()
triangle2 = Triangle_check([12, 13, 10])
triangle2.check_tr()
triangle3 = Triangle_check([-43, 14, 15])
triangle3.check_tr()
triangle4 = Triangle_check([7, 14, 15, 18])
triangle4.check_tr()
triangle5 = Triangle_check(['н', 14, 15])
triangle5.check_tr()

# c = [2, 8, 1, -1, 12]
#
# # c.sort(reverse=True)
# c.sort()
#
# print(c)

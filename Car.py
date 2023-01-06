class Car:
    property1 = 'good'

    def __init__(self, color = 'red', type = 'ford', year = '2022'):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
       self.string = 'Автомобиль заведен'

    def stop(self):
        self.string = 'Автомобиль заглушен'

    def production_year(self, year=2021):
        self.year= year
        self.string = 'Production - ' + str(year)

    def car_type(self, type = 'Audi'):
        self.type = type
        self.string = 'Mark - ' + str(type)

    # def car_type(self):
    #     self.string = 'Mark - ' + self.type

    def car_color(self, color = 'black'):
        self.string = 'Color - ' + str(color)

    def property(self, property1):
        self.property1 = property1
        self.string = property1

    def info(self):
        print(self.string)

c1 = Car()
# print(c1.year)
c1.start()
c1.info()
c1.stop()
c1.info()
c1.production_year(2019)
c1.info()
c1.car_type('VW')
c1.info()
c1.car_color('white')
c1.info()
c1.property('bad')
c1.info()

c2 = Car('green', 'mazda', '2007')
print(c2.color, c2.type, c2.year)


print(Car.property1)
class Myclass:
    def __init__(self, name = 'Afonasij'):
        self.name = name

    def __str__(self):
        return self.name

    def _setattr__(self, attr=2, val=100):
        if attr == 'name':
            self.__dict__[attr] = val
        else:
            print('Operation not resolution')

    def __getattr__(self, attr):
        return 'This field do not exist'

    def __delattr__(self, attr):
        print("the feelds do not erase")


m1 = Myclass()
print(m1)

m1.name = 100
print(m1.name)

del m1.name
print(m1))

# print(m1.name)
# print(m1)
